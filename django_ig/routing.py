from channels.routing import route
from feeds.consumers import ws_message

channel_routing = [
    route("websocket.receive", ws_message),
]
