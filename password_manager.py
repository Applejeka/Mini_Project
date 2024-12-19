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

def delete_data(connect_db, username, password):
    if username and password:
        conn = connect_db()
        if conn:
            with conn.cursor() as cursor:
                # Проверка правильности пароля
                cursor.execute(
                    sql.SQL('SELECT password FROM users WHERE username = %s'),
                    (username,)
                )
                result = cursor.fetchone()
                
                if result and result[0] == password:

                    cursor.execute(
                        sql.SQL('DELETE FROM users WHERE username = %s'),
                        (username,)
                    )
                    conn.commit()
                    if cursor.rowcount != 0:
                        print("Логин удален:", username)
                    else:
                        print("Логин не найден:", username)
                else:
                    print("Неверный пароль логина:", username)
            conn.close()
    else:
        print("Пожалуйста, логин и пароль.")

def fetch_users(connect_db):
    users = []
    conn = connect_db()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT username, password FROM users")
            users = cursor.fetchall()
        conn.close()
    return users