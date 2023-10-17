from getpass import getpass
from mysql.connector import connect, Error

create_friends_table_query = """
CREATE TABLE friends (
    name VARCHAR(50) PRIMARY KEY,
    major VARCHAR(50),
    year INT
)
"""

def add_friend(friend_name, friend_major, friend_year):
    record = (friend_name, friend_major, friend_year)
    query = """INSERT INTO friends 
                VALUES ('%s', '%s', '%s')
            """ % record
    print(query)
    try:
        with connect(
            host="localhost",
            user="wesley", #input("Enter username: "),
            password="password", #getpass("Enter password: "),
            database = "potd_5",
        ) as connection:
            with connection.cursor() as cursor:
                #print(friend_name, friend_major, friend_year)
                cursor.execute(query)
                connection.commit()
    except Error as e:
        print(e)
    
def select_friend():
    query = """SELECT * FROM friends"""
    #print(query)
    try:
        with connect(
            host="localhost",
            user="wesley", #input("Enter username: "),
            password="password", #getpass("Enter password: "),
            database = "potd_5",
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                for row in result:
                    print(row)
    except Error as e:
        print(e)