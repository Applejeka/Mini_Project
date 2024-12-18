import customtkinter

def create_main_window():
    root = customtkinter.CTk()
    root.title('Password manager')
    root.geometry('900x600')
    root.grid_columnconfigure(3, weight=1)
    root.grid_rowconfigure(0, weight=1)
    frame = customtkinter.CTkFrame(root)
    frame.grid()
    create_left_side(root)
    create_right_side(root)
    create_center(root)
    create_header(root)
    root.mainloop()

def create_left_side(root):#LEFT SIDE
    left_side = customtkinter.CTkFrame(root)
    left_label = customtkinter.CTkLabel(left_side, text="Left side")
    left_label.grid(row=0,column=1,padx=10, pady=10)
    left_side.grid(row=0, column=0,padx=10, pady=10, sticky="nsw")

def create_right_side(root):#RIGHT SIDE
    right_side = customtkinter.CTkFrame(root)
    right_label = customtkinter.CTkLabel(right_side, text="Right side")
    right_label.grid(row=0,column=3,padx=10, pady=10)
    right_side.grid(row=0, column=0,padx=10, pady=10, sticky="nse")

def create_center(root):#CENTER
    center = customtkinter.CTkFrame(root)
    center_label = customtkinter.CTkLabel(center, text="center side")
    center_label.grid(row=0,column=2,padx=10, pady=10)
    center.grid(row=0, column=0,padx=10, pady=10, sticky="ns")

def create_header(root):#HEADER
    header = customtkinter.CTkFrame(root)
    header_label = customtkinter.CTkLabel(header, text="Left side")
    header_label.grid(row=0,column=0,padx=10, pady=10)
    header.grid(row=0, column=0,padx=10, pady=10, sticky="ns")