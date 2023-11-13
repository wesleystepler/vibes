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



### ~~~~~~~~~~~~~~~~~~~~~~~~ DATA FILTERING Functions ~~~~~~~~~~~~~~~~~~~~~~~~ ###
def get_user_homepage(user):
    query = queries.display_homepage_query(user)
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    
def get_user_posts(user):
    query = queries.display_user_posts_query(user)
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    
def get_user_friends(user):
    query = queries.display_friends_query(user)
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    
def get_all_users():
    query = queries.display_all_users_query()
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        return result




    

    

