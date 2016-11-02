from channels.routing import route
from channels import include
from feeds.consumers import ws_connect, ws_receive, ws_disconnect

chat_routing = [
    route("websocket.connect", ws_connect),
    route("websocket.receive", ws_receive),
    route("websocket.disconnect", ws_disconnect)
]

channel_routing = [
    include(chat_routing, path=r"^/chat")
]

"""
manage.py runserver --noworker
manage.py runworker

// Note that the path doesn't matter right now; any WebSocket
// connection gets bumped over to WebSocket consumers
socket = new WebSocket("ws://" + window.location.host + "/chat/");
socket.onmessage = function(e) {
    alert(e.data);
}
socket.onopen = function() {
    socket.send("hello world");
}
// Call onopen directly if socket is already open
if (socket.readyState == WebSocket.OPEN) socket.onopen();

"""
