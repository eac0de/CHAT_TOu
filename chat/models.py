from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):

    def __str__(self):
        return super().username


class Room(models.Model):
    name = models.CharField(max_length=50, verbose_name='name')
    users = models.ManyToManyField(User, related_name='rooms', verbose_name='users')
    host = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='host')
    description = models.CharField(max_length=200, verbose_name='description', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'room'
        verbose_name_plural = 'rooms'


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='room')
    message = models.TextField(verbose_name='message')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='sender')
    send_at = models.DateTimeField(default=timezone.now, verbose_name='send_at')

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
