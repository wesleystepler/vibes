from getpass import getpass
from mysql.connector import connect, Error
import queries


try:
    connection = connect(
        host="mysql01.cs.virginia.edu",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="pws3ms_c",
    )

except Error as e:
    print(e)

query = queries.create_user_table
with connection.cursor() as cursor:
    cursor.execute(query)
    connection.commit()
    

