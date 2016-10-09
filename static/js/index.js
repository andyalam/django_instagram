/*
 *
 *    Likes
 *
 */

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


function like_update_view(data) {
  console.log(data);
  var $hiddenData = $('.hidden-data.' + data.post_pk);

  if (data.result) {
    $hiddenData.siblings('.submit-like').removeClass('fa-heart-o').addClass('fa-heart');
  } else {
    $hiddenData.siblings('.submit-like').removeClass('fa-heart').addClass('fa-heart-o');
  }
}



$('.submit-like').on('click', function() {
  create_comment.call(this, like_update_view, error_cb);
});









/*
 *
 *    Comments
 *
 */

function enterPressed(e) {
  if (e.key === "Enter") { return true; }
  return false;
}


function addComment(input, success_cb, error_cb) {
  comment = $(this).val();
  $.ajax({
    type: "POST",
    url: '/comment/',
    data: {
      comment: comment
    },
    success: function(data) { success_cb(data); },
    error: function(error) { error_cb(error); }
  });
}


$('.add-comment').on('keyup', function(e) {
  if (enterPressed(e)) {
    addComment.call(this, comment_update_view, error_cb);
  }
});
