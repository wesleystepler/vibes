### ~~~~~~~~~~~~~~~~~~~~~~~~ ADD TO TABLE QUERIES ~~~~~~~~~~~~~~~~~~~~~~~~ ###




### ~~~~~~~~~~~~~~~~~~~~~~~~ REMOVE FROM TABLE QUERIES ~~~~~~~~~~~~~~~~~~~~~~~~ ###
#removing like, removing comment, delete user?, removing follow/friend



### ~~~~~~~~~~~~~~~~~~~~~~~~ DATA FILTERING QUERIES ~~~~~~~~~~~~~~~~~~~~~~~~ ###

# Display a User's home page
def display_homepage_query():
    # We will return to this later and set it so that only a user's
    # friend's posts are selected here
    return """
    SELECT * FROM Post ORDER BY post_id DESC
    """

# Display All User's
def display_all_users_query():
    return """
    SELECT user_name, first_name, last_name FROM Users
    """

# Display a User's friends
def display_friends_query():
    return """
        SELECT user_name2 FROM Is_Friends_With
        WHERE user_name1 = %s
    """

# Display a specific User's posts
def display_user_posts_query():
    return """
        SELECT * From Post
        WHERE user_name = %s
    """ 

# Display a specific category of posts
def display_category_query():
    return """
        SELECT * FROM Post
        WHERE category = %s
    """ 

#Display a user's likes
def display_likes_query():
    return """
        SELECT * FROM Likes
        WHERE user_name = %s
    """

#Display a user's comments
def display_comments_query():
    return """
    SELECT * FROM Comments
    WHERE user_name = %s
    """

def like_post_query():
    return """
    SELECT * FROM Likes_Post
    WHERE user_name = %s AND post_id = %s
    """
    
