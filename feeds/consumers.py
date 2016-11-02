from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Channel, Group
from channels.sessions import channel_session
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http

"""
@channel_session, provides message.chanel_session
"""

# Connected to websocket.connect
@channel_session_user_from_http
def ws_add(message):
    # Add them to the right group
    Group("chat-%s" % message.user.username[0]).add(message.reply_channel)

# Connected to websocket.receive
@channel_session_user
def ws_message(message):
    Group("chat-%s" % message.user.username[0]).send({
        "text": message['text'],
    })

# Connected to websocket.disconnect
@channel_session_user
def ws_disconnect(message):
    Group("chat-%s" % message.user.username[0]).discard(message.reply_channel)
