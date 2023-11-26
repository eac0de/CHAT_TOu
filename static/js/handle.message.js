let room_id = window.location.pathname.split('/')[2]
let chatSocket = new WebSocket(
    'ws://' + window.location.host + '/chat/' + room_id
);

chatSocket.onmessage = function (e) {
    console.log(e);
    let data = JSON.parse(e.data);
    console.log(data);
    let message_ = data['message'];
    let sender = data['sender'];
    let chat = document.getElementById('chat-content');
    let message = document.createElement('p');
    message.textContent = `${sender}: ${message_}`;
    message.classList.add('col', 'bg-primary', 'rounded-3', 'p-2', 'text-white');
    chat.appendChild(message);
    chat.scrollTop = chat.scrollHeight;
};

document.getElementById('chat-send').onclick = function () {
    let messageInputDom = document.getElementById('chat-input');
    let message = messageInputDom.value;
    let searchParams = new URLSearchParams(window.location.search);
    let user = searchParams.get('user_id');
    console.log(messageInputDom);
    chatSocket.send(JSON.stringify({
        'message': message,
        'user': user,
    }));
    messageInputDom.value = '';
};