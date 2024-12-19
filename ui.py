import customtkinter as ctk
from logic import add_data
from logic import delete_data
from logic import fetch_users
from database import connect_db

def on_submit(entry_username, entry_password, connect_db):
    username = entry_username.get()
    password = entry_password.get()
    add_data(connect_db, username, password)
    entry_username.delete(0, ctk.END)
    entry_password.delete(0, ctk.END)
    
def on_delete(entry_username, entry_password, connect_db):
    username = entry_username.get()
    password = entry_password.get()
    delete_data(connect_db, username, password)
    entry_username.delete(0, ctk.END)
    entry_password.delete(0, ctk.END)

def create_main_window():
    root = ctk.CTk()
    root.title('Password manager')
    root.geometry('800x500')
    root.grid_columnconfigure(4, weight=1)
    root.grid_rowconfigure(1, weight=1)
    frame = ctk.CTkFrame(root)
    frame.grid(row=1,column=0,padx=1, pady=1, sticky="ew")
    create_header(frame)
    # create_left_side(root)
    user_list(frame)
    # create_right_side(root)
    root.mainloop()

#Header/Add-Delete_login
def create_header(frame):#HEADER
    header = ctk.CTkFrame(frame)
    header.grid_columnconfigure(5, weight=10)
    header.grid_rowconfigure(2, weight=10)
    login_label = ctk.CTkLabel(header, text="Login")
    login_label.grid(row=0,column=0,padx=10, pady=10)
    password_label = ctk.CTkLabel(header, text="Password")
    password_label.grid(row=0,column=2,padx=10, pady=10)
    #Поля логина и пороля
    entry_username = ctk.CTkEntry(header)
    entry_username.grid(row=0, column=1,padx=10, pady=10) #Login GRID
    entry_password = ctk.CTkEntry(header, show="*")
    entry_password.grid(row=0, column=3,padx=10, pady=10) #Password GRID
    #Кнопка добавления
    button = ctk.CTkButton(header, text="Добавить", command=lambda: on_submit(entry_username, entry_password, connect_db))
    button.grid(row=0, column=4,padx=10, pady=10)
    #Кнопка удаления
    button = ctk.CTkButton(header, text="Удалить", command=lambda: on_delete(entry_username, entry_password, connect_db))
    button.grid(row=0, column=5,padx=10, pady=10)
    header.grid(row=0, column=0,padx=10, pady=10, sticky="ew")

#Center/User_list
def show_users(user_list):
    users = fetch_users(connect_db)
    user_list.delete(1.0, ctk.END)
    for username, password in users:
        user_list.insert(ctk.END, f"Username: {username}, Password: {password}\n")
#CENTER
def user_list(frame):
    center = ctk.CTkFrame(frame)
    button = ctk.CTkButton(center, text="Показать Пороли", command=lambda: show_users(user_list))
    button.grid(row=1, column=1,padx=10, pady=10)

    user_list = ctk.CTkTextbox(center, width=400, height=300)
    user_list.grid(row=1, column=0,padx=10, pady=10)

    center.grid(row=1, column=0,padx=10, pady=10, sticky="nsw")