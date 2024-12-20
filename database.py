import sqlite3

# def connect_db():
#     try:
#         connect = sqlite3.connect(
#             dbname='Password_manager',
#             user='postgres',
#             password='6813',
#             host='localhost'
#         )
#         return connect
#     except Exception as e:
#         print(f"Ошибка подключения к базе данных: {e}")
#         return None


def connect_db():
    try:
        connect = sqlite3.connect('/home/nuts/Documents/Database/Password_manager')
        return connect
    except Exception as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None