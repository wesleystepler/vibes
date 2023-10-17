from getpass import getpass
from mysql.connector import connect, Error

create_friends_table_query = """
CREATE TABLE friends (
    name VARCHAR(50) PRIMARY KEY,
    major VARCHAR(50),
    year INT
)
"""

show_friends_query = """
    DESCRIBE friends
"""

try:
    with connect(
        host="localhost",
        user="wesley", #input("Enter username: "),
        password="password", #getpass("Enter password: "),
        database = "potd_5",
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(show_friends_query)
            # Fetch rows from last executed query
            result = cursor.fetchall()
            for row in result:
                print(row)

except Error as e:
    print(e)