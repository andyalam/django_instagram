

function create_comment(success_cb, error_cb) {
  var post_pk = $(this).siblings('.hidden-data').find('.post-pk').text();
  console.log(post_pk);

  $.ajax({
    type: "POST",
    url: '/like/',
    data: {
      post_pk: post_pk
    },
    success: function(data) { success_cb(data); },
    error: function(error) { error_cb(error); }
  });
}

function error_cb(error) {
  console.log(error);
}

function update_post_view(data) {
  console.log(data);
  if (data.result) {
    $('.submit-like').removeClass('fa-heart-o').addClass('fa-heart');
  } else {
    $('.submit-like').removeClass('fa-heart').addClass('fa-heart-o');
  }
}



$('.submit-like').on('click', function() {
  create_comment.call(this, update_post_view, error_cb);
});
