import customtkinter as ctk
from psycopg2 import sql
from database import connect_db

def add_data(connect_db, username, password):
    if username and password:
        conn = connect_db()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    sql.SQL('INSERT INTO users (username, password) VALUES (%s, %s)'),
                    (username, password)
                )
                conn.commit()
                print("Данные добавлены:", username)
            conn.close()
    else:
        print("Пожалуйста, введите логин и пароль.")

