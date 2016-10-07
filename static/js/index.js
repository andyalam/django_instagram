function create_comment() {
  $.ajax({
    type: "POST",
    url: '/like',
    success: function(data) {
      console.log(data);
    },
    error: function(error) {
      console.log(data);
    }
  });
}

$('.submit-like').on('click', create_comment);
