### ~~~~~~~~~~~~~~~~~~~~~~~~ CREATE TABLE QUERIES ~~~~~~~~~~~~~~~~~~~~~~~~ ###

#User(user_name, password, first_name, last_name, email)
create_user_table = """
CREATE TABLE User (
    user_name VARCHAR(50) PRIMARY KEY,
    password VARCHAR(50),
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    email VARCHAR(50)
)
"""

#Post(post_id, user_name, category, timestamp, text)
create_post_table = """
    CREATE TABLE Post (
        post_id INT AUTO_INCREMENT PRIMARY KEY,
        user_name REFERENCES User(user_name),
        category VARCHAR(30),
        timestamp VARCHAR(16),
        likes INT,
        text VARCHAR(280),
    )
"""

#Comment(comment_id, post_id, user_name, timestamp, likes, comment_text)
create_comment_table = """
    CREATE TABLE Comment (
    comment_id INT AUTO_INCREMENT PRIMARY KEY,
    post_id REFERENCES Post(post_id),
    user_name REFERENCES User(user_name),
    comment_text VARCHAR(280)

    )
"""

#Post_Comments(post_id, comment_id)
create_post_comments_table = """
    CREATE TABLE Post_Comments (
        post_id INT AUTO_INC REFERENCES Post(post_id),
        comment_id INT AUTO_INC REFERENCES Comment(comment_id)
    )
"""

#Is_Friends_With(user_name1, user_name2)
create_is_friends_with_table = """
    CREATE TABLE Is_Friends_With (
        user_name1 VARCHAR(50) REFERENCES User(user_name),
        user_name2 VARCHAR(50) REFERENCES User(user_name),
        PRIMARY KEY (user_name1, user_name2)
    )
"""


#Sends_Request_To(user_name1, user_name2)
create_request_table = """
    CREATE TABLE Sends_Request_To (
        user_name1 VARCHAR(50) REFERENCES User(user_name),
        user_name2 VARCHAR(50) REFERENCES User(user_name),
        PRIMARY KEY (user_name1, user_name2),
    )
"""


#Likes_Comment(user_name, comment_id)
create_likes_comment_table = """
    CREATE TABLE Likes_Comment (
        user_name VARCHAR(50) PRIMARY KEY REFERENCES User(user_name),
        comment_id INT AUTO_INC REFERENCES Comment(comment_id)
    )
"""


#Likes_Post(user_name, post_id)
create_likes_post_table = """
    CREATE TABLE Likes_Post (
        user_name VARCHAR(50) PRIMARY KEY REFERENCES User(user_name),
        post_id INT AUTO_INC REFERENCES Post(post_id)
    )
"""


#Replies(comment_id, reply_num user_name, timestamp, likes, comment_text, post_id)
create_replies_table = """
    CREATE TABLE Replies(
        comment_id INT AUTO_INC REFERENCES Comment(comment_id),
        reply_num INT AUTO_INC,
        user_name VARCHAR(50) REFERENCES User(user_name),
        timestamp VARCHAR(16),
        PRIMARY KEY (comment_id, reply_num)
    )
"""

### ~~~~~~~~~~~~~~~~~~~~~~~~ ADD TO TABLE QUERIES ~~~~~~~~~~~~~~~~~~~~~~~~ ###




### ~~~~~~~~~~~~~~~~~~~~~~~~ REMOVE FROM TABLE QUERIES ~~~~~~~~~~~~~~~~~~~~~~~~ ###




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
