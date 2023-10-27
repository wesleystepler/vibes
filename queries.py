### ~~~~~~~~~~~~~~~~~~~~~~~~ ADD TO TABLE QUERIES ~~~~~~~~~~~~~~~~~~~~~~~~ ###




### ~~~~~~~~~~~~~~~~~~~~~~~~ REMOVE FROM TABLE QUERIES ~~~~~~~~~~~~~~~~~~~~~~~~ ###
#removing like, removing comment, delete user?, removing follow/friend



### ~~~~~~~~~~~~~~~~~~~~~~~~ DATA FILTERING QUERIES ~~~~~~~~~~~~~~~~~~~~~~~~ ###

# Display a User's home page
def display_homepage_query(user):
    return """
    SELECT * FROM 
    """

# Display a User's friends
def display_friends_query(user):
    data = (user)
    return """
        SELECT * FROM Is_Friends_With
        WHERE username1 = '%s'
    """ % data

# Display a specific User's posts
def display_user_posts_query(user):
    data = (user)
    return """
        SELECT * From Post
        WHERE user_name = '%s'
    """ % data

# Display a specific category of posts
def display_category_query(category):
    data = category
    return """
        SELECT * FROM Post
        WHERE category = '%s'
    """ % data

#Display a user's likes
def display_likes_query(user):
    return """
        SELECT * FROM Likes
        WHERE user_name = '%s'
    """ % user

#Display a user's comments
def display_comments_query(user):
    return """
    SELECT * FROM Comments
    WHERE user_name = '%s'
    """ % user
