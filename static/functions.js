
// import jquery
var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.3.min.js'; // Check https://jquery.com/ for the current version
document.getElementsByTagName('head')[0].appendChild(script);

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
