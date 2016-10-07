function create_comment() {
  var post_pk = $(this).siblings('.hidden-data').find('.post-pk').text();

  $.ajax({
    type: "POST",
    url: '/like/',
    data: {
      post_pk: post_pk
    },
    success: function(data) {
      console.log(data);
    },
    error: function(error) {
      console.log(error);
    }
  });
}

$('.submit-like').on('click', create_comment);
