from django.http import HttpResponse
from django.contrib.auth.models import User
from channels.handler import AsgiHandler
from channels import Channel, Group
from channels.sessions import channel_session
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http
from .models import Room, Message
import json

"""
@channel_session, provides message.chanel_session
"""

# Connected to websocket.connect
@channel_session_user_from_http
def ws_connect(message):
    path = message.content['path']
    room_label = path.replace('/chat/inbox/', '').replace('/', '')
    room = Room.objects.get(label=room_label)

    Group('chat-' + room_label).add(message.reply_channel)
    message.channel_session['room'] = room.label


# Connected to websocket.receive
@channel_session_user
def ws_receive(message):
    path = message.content['path']
    room_label = path.replace('/chat/inbox/', '').replace('/', '')
    room = Room.objects.get(label=room_label)
    data = json.loads(message['text'])
    username = data['user']
    text = data['message']

    sender = User.objects.get(username=data['user'])
    m = room.messages.create(sender=sender, text=text)

    context = {
        'text': m.text,
        'user': sender.username
    }
    Group('chat-'+ room_label).send({'text': json.dumps(context) })


# Connected to websocket.disconnect
@channel_session_user
def ws_disconnect(message):
    label = message.channel_session['room']
    Group('chat-'+label).discard(message.reply_channel)
