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

    

