from getpass import getpass
from mysql.connector import connect, Error
import queries


try:
    connection = connect(
        host="mysql01.cs.virginia.edu",
        user="pws3ms",
        password="Fall2023",
        database="pws3ms_c",
    )

except Error as e:
    print(e)


def add_new_user(user, pwd, first_name, last_name, email):
    query = """
        INSERT into Users (user_name, pwd, first_name, last_name, email)
        VALUES (%s, %s, %s, %s, %s)
        """

    with connection.cursor() as cursor:
        cursor.execute(query, (user, pwd, first_name, last_name, email))
        connection.commit()

def get_all_users():
    query = """
    SELECT * FROM Users    
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    

def describe_table():
    query = """DESC Users"""
    with connection.cursor(buffered=True) as cursor:
        cursor.execute(query)
        return cursor.fetchall()

def get_user(user):
    query = """
    SELECT * FROM Users WHERE user_name = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (user,))
        result = cursor.fetchall()
        return result
    
def get_password(user):
    query = """
    SELECT pwd FROM Users WHERE user_name = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (user,))
        result = cursor.fetchall()
        return result
# def update_password():
#     query = """
#     alter table Users modfiy first_name varchar(255) not null algorithm=copy;
#     """
    
#     with connection.cursor() as cursor:
#         cursor.execute(query)
#         connection.commit()
    


### ~~~~~~~~~~~~~~~~~~~~~~~~ DATA ADDING Functions ~~~~~~~~~~~~~~~~~~~~~~~~ ###
def create_new_post(category, time_posted, likes, post_text, user_name):
    query = """INSERT INTO Post (category, time_posted, likes, post_text, user_name)
    VALUES(%s, %s, %s, %s, %s)"""
    with connection.cursor() as cursor:
        cursor.execute(query, (category, time_posted, likes, post_text, user_name))
        connection.commit()

def add_like(user, post_id):
    query = """
    INSERT INTO Likes_Post (user_name, post_id)
    VALUES (%s, %s)
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (user, post_id))
        connection.commit()

def send_request(user1, user2):
    query = """
    INSERT INTO Sends_Request_To (user_name1, user_name2)
    VALUES (%s, %s)
    """

    with connection.cursor() as cursor:
        cursor.execute(query, (user1, user2))
        connection.commit()


def add_friends(user1, user2):
    query = """
    INSERT INTO Is_Friends_With (user_name1, user_name2)
    VALUES (%s, %s)
    """ 

    with connection.cursor() as cursor:
        cursor.execute(query, (user1, user2))
        connection.commit()

    with connection.cursor() as cursor:
        cursor.execute(query, (user2, user1))
        connection.commit()
    
### ~~~~~~~~~~~~~~~~~~~~~~~~ REMOVE FROM TABLE QUERIES ~~~~~~~~~~~~~~~~~~~~~~~~ ###

def remove_like(user, post_id):
    query = """
    DELETE FROM Likes_Post
    WHERE user_name = %s AND post_id = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (user, post_id))
        connection.commit()


def delete_request(user1, user2):
    query = """
    DELETE FROM Sends_Request_To
    WHERE user_name1 = %s AND user_name2 = %s
    """

    with connection.cursor() as cursor:
        cursor.execute(query, (user1, user2))
        connection.commit()

### ~~~~~~~~~~~~~~~~~~~~~~~~ DATA FILTERING Functions ~~~~~~~~~~~~~~~~~~~~~~~~ ###
# EDIT THIS TO USE A QUERY THAT GETS POSTS FROM THE USERS FRIENDS
def get_user_homepage(user):
    query = """
    SELECT category, time_posted, likes, post_text, user_name, post_id 
    FROM Post JOIN Is_Friends_With ON Post.user_name = Is_Friends_With.user_name2
    WHERE user_name1 = %s 
    ORDER BY post_id DESC; 
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (user,))
        result = cursor.fetchall()
        return result
    

def get_all_vibes():
    query = """
    SELECT * FROM Post ORDER BY post_id DESC
    """

    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    

def get_filtered_vibes(category):
    query = """
    SELECT * FROM Post WHERE category = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (category,))
        result = cursor.fetchall()
        return result
    
def get_user_posts(user):
    query = queries.display_user_posts_query()
    with connection.cursor() as cursor:
        cursor.execute(query, (user,))
        result = cursor.fetchall()
        return result
    
def get_user_friends(user):
    query = queries.display_friends_query()
    with connection.cursor() as cursor:
        cursor.execute(query, (user,))
        result = cursor.fetchall()
        return result
    
def get_all_users():
    query = queries.display_all_users_query()
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    
def get_user_requests(user):
    query = """
    SELECT user_name1 FROM Sends_Request_To
    WHERE user_name2 = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (user,))
        result = cursor.fetchall()
        return result
    
def get_sent_requests(user):
    query = """
    SELECT user_name2 FROM Sends_Request_To
    WHERE user_name1 = %s
    """

    with connection.cursor() as cursor:
        cursor.execute(query, (user,))
        result = cursor.fetchall()
        return result


def get_user_likepost(user, post_id):
    query = queries.like_post_query()
    with connection.cursor() as cursor:
        cursor.execute(query, (user, post_id))
        result = cursor.fetchall()
        return result

def get_user_likecomment(user, comment_id):
    query = """
    SELECT * FROM Likes_Comment
    WHERE user_name = %s AND comment_id = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (user, comment_id))
        result = cursor.fetchall()
        return result

def add_like_comment(user, comment_id):
    query = """
    INSERT INTO Likes_Comment (user_name, comment_id)
    VALUES (%s, %s)
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (user, comment_id))
        connection.commit()

def remove_like_comment(user, comment_id):
    query = """
    DELETE FROM Likes_Comment
    WHERE user_name = %s AND comment_id = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (user, comment_id))
        connection.commit()

def increment_likes_comment(comment_id):
    query = """
    UPDATE Comment
    SET likes = likes + 1
    WHERE comment_id = %s
    """

    with connection.cursor() as cursor:
        cursor.execute(query, (comment_id,))
        connection.commit()

def decrement_likes_comment(comment_id):
    query = """
    UPDATE Comment
    SET likes = likes - 1
    WHERE comment_id = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (comment_id,))
        connection.commit()
        

def decrement_likes(post_id):
    query = """
    UPDATE Post
    SET likes = likes - 1
    WHERE post_id = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (post_id,))
        connection.commit()

def increment_likes(post_id):

    query = """
    UPDATE Post
    SET likes = likes + 1
    WHERE post_id = %s
    """

    with connection.cursor() as cursor:
        cursor.execute(query, (post_id,))
        connection.commit()

def get_user_likereply(user, reply_id):
    query = """
    SELECT * FROM likes_reply
    WHERE user_name = %s AND reply_id = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (user, reply_id))
        result = cursor.fetchall()
        return result

def add_like_reply(user, reply_id):
    query = """
    INSERT INTO likes_reply (user_name, reply_id)
    VALUES (%s, %s)
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (user, reply_id))
        connection.commit()

def remove_like_reply(user, reply_id):
    query = """
    DELETE FROM likes_reply
    WHERE user_name = %s AND reply_id = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (user, reply_id))
        connection.commit()

def increment_likes_reply(reply_id):
    query = """
    UPDATE Replies
    SET likes = likes + 1
    WHERE reply_id = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (reply_id,))
        connection.commit()

def decrement_likes_reply(reply_id):
    query = """
    UPDATE Replies
    SET likes = likes - 1
    WHERE reply_id = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (reply_id,))
        connection.commit()
    

def delete_post(post_id):
    query = """
    DELETE FROM Post
    WHERE post_id = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (post_id,))
        connection.commit()
        
    
def get_all_comments():
    query = """
    SELECT * FROM Comment
    ORDER BY post_id DESC, comment_id DESC
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        return result

def add_comment(user_name, post_id, comment_text, likes):
    query = """
    INSERT INTO Comment (user_name, post_id, comment_text, likes)
    VALUES (%s, %s, %s, %s)
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (user_name, post_id, comment_text, likes))
        connection.commit()
        
def add_reply(user_name, comment_id, reply_text,time_stamp, likes):
    query = """
    INSERT INTO Replies (user_name, comment_id, reply_text, time_stamp, likes)
    VALUES (%s, %s, %s, %s, %s)
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (user_name, comment_id, reply_text, time_stamp, likes))
        connection.commit()

def get_all_replies():
    query = """
    SELECT * FROM Replies
    ORDER BY comment_id DESC, reply_id DESC
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        return result