$(document).ready(function() {
  $("#messageInput").on('keypress', function(e) {
    if (e.which == 13) {
      socket.send($(this).val());
      $(this).val('');
    }
  });

  // Note that the path doesn't matter right now; any WebSocket
  // connection gets bumped over to WebSocket consumers
  socket = new WebSocket("ws://" + window.location.host + "/chat/");
  socket.onmessage = function(e) {
      var message = e.data;
      console.log(message);
      $("#messages").append("<li>" + message + "</li>");
      console.log('test');
  }
  socket.onopen = function() {
      console.log("socked opened");
  }
  // Call onopen directly if socket is already open
  if (socket.readyState == WebSocket.OPEN) socket.onopen();

  // socket.send('test');
});
