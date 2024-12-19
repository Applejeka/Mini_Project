from ui import create_main_window
from database import connect_db
#from database import save_data

# def on_save(data):
#     save_data(data)

if __name__ == "__main__":
    connect_db()
    create_main_window()
