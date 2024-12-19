import psycopg2

def connect_db():
    try:
        connect = psycopg2.connect(
            dbname='Password_manager',
            user='postgres',
            password='6813',
            host='localhost'
        )
        return connect
    except Exception as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None