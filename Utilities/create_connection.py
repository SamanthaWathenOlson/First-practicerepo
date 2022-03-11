from psycopg import connect, OperationalError


def create_connection():
    try:
        conn = connect(
            host="os.environ.get[HOST]",
            dbname="os.environ.get[DATABASE]",
            user="os.environ.get[USERNAME]",
            password="os.environ.get[PASSWORD]",
            port="os.environ.get[PORT]",
        )
        return conn
    except OperationalError:
        return "Could not connect to server"

    connection = create_connection()

    print(connection)
