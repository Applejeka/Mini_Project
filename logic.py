import customtkinter

def create_el_logic():
    username = entry_username.get()
    password = entry_password.get()
    
    if username and password:
        credentials.append((username, password))
        print("Добавлено:", username, password)
        entry_username.delete(0, ctk.END)
        entry_password.delete(0, ctk.END)
    else:
        print("Пожалуйста, введите логин и пароль.")
