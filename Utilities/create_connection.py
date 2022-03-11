import os

from psycopg import connect, OperationalError



def create_connection():
    try:
        conn = connect(
            host="",
            dbname="",
            user="",
            password="",
            port="",
        )
        return conn
    except OperationalError:
        return "Could not connect to server"

    connection = create_connection()

    print(connection)


