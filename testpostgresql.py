import psycopg2
from config import host, user, password, db_name, port

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name,
)

cursor = connection.cursor()

with connection.cursor() as cursor:
    cursor.execute("""SELECT * FROM Spec;""")
    print(f"Server version1: {cursor.fetchone()}")

