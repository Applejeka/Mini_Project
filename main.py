from ui import create_main_window
from database import connect_db

if __name__ == "__main__":
    connect_db()
    create_main_window()