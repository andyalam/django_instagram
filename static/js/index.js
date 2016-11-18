/*
 *
 *    Likes
 *
 */

function create_like(success_cb, error_cb) {
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

  // toggle heart
  var $hiddenData = $('.hidden-data.' + data.post_pk);
  if (data.result) {
    $hiddenData.siblings('.submit-like').removeClass('fa-heart-o').addClass('fa-heart');
  } else {
    $hiddenData.siblings('.submit-like').removeClass('fa-heart').addClass('fa-heart-o');
  }

  // update like count
  var difference = data.result ? 1 : -1;
  var $post = $('.view-update.' + data.post_pk);
  var $likes = $post.find('.likes');
  var likes = parseInt($likes.text());
  likes = likes + difference;

  console.log('likes', likes);

  if (likes == null || isNaN(likes)) {
    $likes.text('1 like');
  } else if (likes === 0) {
    $likes.text('');
  } else if (likes === 1) {
    $likes.text('1 like');
  } else {
    $likes.text(likes + ' likes');
  }
}



$('.submit-like').on('click', function() {
  create_like.call(this, like_update_view, error_cb);
});

$('.card__main-image').on('dblclick', function() {
  var $unlikedHeart = $(this).closest('.view-update').find('.fa-heart-o');
  if($unlikedHeart) {
    $unlikedHeart.click();
  }
})









/*
 *
 *    Comments
 *
 */

function enterPressed(e) {
  if (e.key === "Enter") { return true; }
  return false;
}


function validComment(text) {
  if (text == '') return false;
  return true;
}


function create_comment(success_cb, error_cb) {
  var comment_text = $(this).val();
  var post_pk = $(this).parent().siblings('.hidden-data').find('.post-pk').text();

  console.log(comment_text, post_pk);

  $.ajax({
    type: "POST",
    url: '/comment/',
    data: {
      comment_text: comment_text,
      post_pk: post_pk
    },
    success: function(data) { success_cb(data); },
    error: function(error) { error_cb(error); }
  });
}


function comment_update_view(data) {
  console.log(data);
  var $post = $('.hidden-data.' + data.post_pk);
  var commentHTML = '<li class="comment-list__comment"><a class="user" href="' + data.commenter_info.profile_url
                  + '">' + data.commenter_info.username + '</a> <span class="comment">'
                  + data.commenter_info.comment_text +'</span></li>'

  $post.closest('.view-update').find('.comment-list').append(commentHTML);
}


$('.add-comment').on('keyup', function(e) {
  if (enterPressed(e)) {
    if (validComment($(this).val())) {
      create_comment.call(this, comment_update_view, error_cb);
      $(this).val('');
    }
  }
});










/*
 *
 *    Follow/Unfollow
 *
 */

function follow_user(success_cb, error_cb, type) {
  var follow_profile_pk = $(this).closest('.follow__card').attr('id')
                        || $(this).attr('id');
  console.log(follow_profile_pk);

  $.ajax({
    type: "POST",
    url: '/follow_toggle/',
    data: {
      follow_profile_pk: follow_profile_pk,
      type: type
    },
    success: function(data) { success_cb(data); },
    error: function(error) { error_cb(error); }
  });
}

function update_follow_view(data) {
  console.log('data',data);
  var $button = $('.follow__card#' + data.follow_profile_pk
                + ' .btn, .profile .follow-toggle__container .btn');
  $button.addClass('unfollow-user').removeClass('follow-user');
  $button.text('Following');
}

function update_unfollow_view(data) {
  console.log('data',data);
  var $button = $('.follow__card#' + data.follow_profile_pk
                + ' .btn, .profile .follow-toggle__container .btn');
  $button.addClass('follow-user').removeClass('unfollow-user');
  $button.text('Follow');
}


$('.follow-toggle__container').on('click', '.follow-user', function() {
  follow_user.call(this, update_follow_view, error_cb, 'follow');
});

$('.follow-toggle__container').on('click', '.unfollow-user', function() {
  follow_user.call(this, update_unfollow_view, error_cb, 'unfollow');
});







/*
 *
 *    General
 *
 */

 // mobile back button
 $('.back-button').on('click', function() {
   window.history.back();
 })
