$(document).ready(function() {
  // scroll instantly to bottom of messages on load
  $(window).scrollTop($(document).height());
  if ($(window).width() < 768) {
    $('#main-nav').remove();
  }

  var sessionKey = $('#sessionKey').text();
  socket = new WebSocket("ws://" + window.location.host + "/chat" + window.location.pathname);

  socket.onmessage = function(message) {
      console.log(message);
      var data = JSON.parse(message.data);
      var currentUser = $('#chatData #user').text();

      var html;
      if (data.user == currentUser) {
        html = "<div class='message-sent'><div class='text'>" + data.text + "</div></div>";
      } else {
        html = "<div class='message-received'><div class='sender'>" + data.user + "</div><div class='text'>" + data.text + "</div></div>";
      }
      $("#messages").append(html);

      // scroll instantly to bottom of page upon new message receival
      $(window).scrollTop($(document).height());
  }

  socket.onopen = function() {
      console.log("socked opened");
  }

  // Call onopen directly if socket is already open
  if (socket.readyState == WebSocket.OPEN) socket.onopen();

  $("#messageInput").on('keypress', function(e) {
    if (e.which == 13) {
      var message = {
          user: $('#user').text(),
          message: $('#messageInput').val()
      }

      socket.send(JSON.stringify(message));
      $(this).val('');

      return false;
    }
  });
});
