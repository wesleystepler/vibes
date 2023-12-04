
// import jquery
var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.3.min.js'; // Check https://jquery.com/ for the current version
document.getElementsByTagName('head')[0].appendChild(script);


function toggleCommentForm(postID) {
    event.preventDefault();
    var commentForm = $('#comment-form-' + postID);
    if (commentForm.css('display') == 'none') {
        commentForm.css('display', 'block');
    } else {
        commentForm.css('display', 'none');
    }
}

function toggleReplyForm(commentID) {
    event.preventDefault();
    var replyForm = $('#reply-form-' + commentID);
    if (replyForm.css('display') == 'none') {
        replyForm.css('display', 'block');
    }
    else {
        replyForm.css('display', 'none');
    }
}




function addLike(postID){
    console.log('postID:', postID)
    $.ajax({
        type: 'POST',
        url: '/like_post',
        contentType: 'application/json',
        data: JSON.stringify({post_id: postID}),
        success: function(response) {
            if (response.result == 'liked') {
                var likeCount = parseInt($('#like-count-' + postID).text());
                $('#like-count-' + postID).text(likeCount+1);
                
            } else if (response.result == 'unliked') {
                var likeCount = parseInt($('#like-count-' + postID).text());
                $('#like-count-' + postID).text(likeCount-1);
            }
        },
        error: function(error) {
          console.log('Error:', error);
        }
    });

}

function addReplyLike(replyID){
    console.log('replyID:', replyID)
    $.ajax({
        type: 'POST',
        url: '/like_reply',
        contentType: 'application/json',
        data: JSON.stringify({reply_id: replyID}),
        success: function(response) {
            if (response.result == 'liked') {
                var likeCount = parseInt($('#reply-like-count-' + replyID).text());
                $('#reply-like-count-' + replyID).text(likeCount+1);
                
            } else if (response.result == 'unliked') {
                var likeCount = parseInt($('#reply-like-count-' + replyID).text());
                $('#reply-like-count-' + replyID).text(likeCount-1);
            }
        },
        error: function(error) {
          console.log('Error:', error);
        }
    });

}

function addCommentLike(commentID){
    console.log('commentID:', commentID)
    $.ajax({
        type: 'POST',
        url: '/like_comment',
        contentType: 'application/json',
        data: JSON.stringify({comment_id: commentID}),
        success: function(response) {
            if (response.result == 'liked') {
                var likeCount = parseInt($('#comment-like-count-' + commentID).text());
                $('#comment-like-count-' + commentID).text(likeCount+1);
                
            } else if (response.result == 'unliked') {
                var likeCount = parseInt($('#comment-like-count-' + commentID).text());
                $('#comment-like-count-' + commentID).text(likeCount-1);
            }
        },
        error: function(error) {
          console.log('Error:', error);
        }
    });

}

function sendRequestTo(username) { 
    console.log('username', username);
    $.ajax({
        type: 'POST',
        url: '/send_request',
        contentType: 'application/json',
        data: JSON.stringify({user_name2: username}),
        success: function(response) {
            if (response.result == 'success') {

                $(`#add-${username}`).hide();
                $(`#request-sent-${username}`).show();
                var request = document.getElementById(username);
                request.remove();
                console.log("Success!");
            }
        },

        error: function(error) {
            console.log('Error', error);
        }

    });
}

function acceptRequest(username) { 
    console.log('username', username);
    $.ajax({
        type: 'POST',
        url: '/accept_request',
        contentType: 'application/json',
        data: JSON.stringify({requester: username}),
        success: function(response) {
            if (response.result == 'success') {
                // delete the request
                console.log("Success!");
                var request = document.getElementById(username);
                request.remove();

            }
        },

        error: function(error) {
            console.log('Error', error);
        }

    });
}


function rejectRequest(username) { 
    console.log('username', username);
    $.ajax({
        type: 'POST',
        url: '/reject_request',
        contentType: 'application/json',
        data: JSON.stringify({requester: username}),
        success: function(response) {
            if (response.result == 'success') {
                console.log("Success!");  
                var request = document.getElementById(username);
                request.remove();
            }
        },

        error: function(error) {
            console.log('Error', error);
        }

    });
}


function filterVibes(category) { 
    console.log('category', category);
    $.ajax({
        type: 'POST',
        url: '/filter',
        contentType: 'application/json',
        data: JSON.stringify({category: category}),
        success: function(response) {
            if (response.result == 'success') {
                console.log("Success!");  
            }
        },

        error: function(error) {
            console.log('Error', error);
        }

    });
}