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
    record = (user, pwd, first_name, last_name, email)
    query = """
        INSERT into Users 
        VALUES ('%s', '%s', '%s', '%s', '%s')
        """ % record

    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()

def get_all_users():
    query = """
    SELECT * FROM Users    
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    


    

