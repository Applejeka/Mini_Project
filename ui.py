import customtkinter as ctk
from logic import add_data
from database import connect_db

def on_submit(entry_username, entry_password, connect_db):
    username = entry_username.get()
    password = entry_password.get()
    add_data(connect_db, username, password)
    entry_username.delete(0, ctk.END)
    entry_password.delete(0, ctk.END)

def create_main_window():
    root = ctk.CTk()
    root.title('Password manager')
    root.geometry('900x600')
    root.grid_columnconfigure(4, weight=1)
    root.grid_rowconfigure(1, weight=1)
    frame = ctk.CTkFrame(root)
    frame.grid()
    create_header(root)
    # create_left_side(root)
    create_center(root)
    # create_right_side(root)
    root.mainloop()

def create_header(root):#HEADER
    header = ctk.CTkFrame(root)
    header.grid_columnconfigure(4, weight=10)
    header.grid_rowconfigure(2, weight=10)

    header_label = ctk.CTkLabel(header, text="Login")
    header_label.grid(row=0,column=0,padx=10, pady=10)
    header_label = ctk.CTkLabel(header, text="Password")
    header_label.grid(row=0,column=2,padx=10, pady=10)
    #Поля логина и пороля
    entry_username = ctk.CTkEntry(header)
    entry_username.grid(row=0, column=1,padx=10, pady=10) #Login GRID
    entry_password = ctk.CTkEntry(header, show="*")
    entry_password.grid(row=0, column=3,padx=10, pady=10) #Password GRID
    #Кнопка добавления
    button = ctk.CTkButton(root, text="Добавить", command=lambda: on_submit(entry_username, entry_password, connect_db))
    button.grid(row=0, column=3,padx=10, pady=10)
    #Кнопка удаления
    button = ctk.CTkButton(root, text="Удалить", command=lambda: on_submit(entry_username, entry_password, connect_db))
    button.grid(row=0, column=4,padx=10, pady=10)

    header.grid(row=0, column=0,padx=10, pady=10, sticky="ew")

# def create_left_side(root):#LEFT SIDE
#     left_side = ctk.CTkFrame(root)
#     left_label = ctk.CTkLabel(left_side, text="Left side")
#     left_label.grid(row=0,column=0,padx=10, pady=10)
#     left_side.grid(row=1, column=0,padx=10, pady=10, sticky="nsw")

def create_center(root):#CENTER
    center = ctk.CTkFrame(root)
    center_label = ctk.CTkLabel(center, text="Center side")
    center_label.grid(row=0,column=0,padx=10, pady=10)
    center.grid(row=1, column=1,padx=0, pady=10, sticky="nsew")

# def create_right_side(root):#RIGHT SIDE
#     right_side = ctk.CTkFrame(root)
#     right_label = ctk.CTkLabel(right_side, text="Right side")
#     right_label.grid(row=0,column=0,padx=10, pady=10)
#     right_side.grid(row=1, column=2,padx=10, pady=10, sticky="nse")