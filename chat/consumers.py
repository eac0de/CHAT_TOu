# consumers.py
import json

from asgiref.sync import async_to_sync, sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from chat.models import Message, User, Room


class Consumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_id = None

    async def connect(self):
        self.room_id = str(self.scope['url_route']['kwargs']['room_id'])
        await self.channel_layer.group_add(self.room_id, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        self.channel_layer.group_discard(self.room_id, self.channel_name)

    async def receive(self, **kwargs):
        content = json.loads(kwargs.get('text_data'))
        message = content.get('message')
        room = await sync_to_async(Room.objects.get)(pk=self.room_id)
        sender = await sync_to_async(User.objects.get)(pk=content.get('user'))
        await sync_to_async(Message.objects.create)(room=room, message=message, sender=sender)
        await self.channel_layer.group_send(
            self.room_id,
            {
                "type": "chat.message",
                'sender': sender.username,
                'message': message
            })

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))
