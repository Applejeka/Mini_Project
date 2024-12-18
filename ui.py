import customtkinter
#from logic import create_el_logic

def create_main_window():
    root = customtkinter.CTk()
    root.title('Password manager')
    root.geometry('900x600')
    root.grid_columnconfigure(2, weight=1)
    root.grid_rowconfigure(1, weight=1)
    #root.surf.grid_columnconfigure(0, weight=1)
    #root.surf.grid_columnconfigure(1, weight=1)
    frame = customtkinter.CTkFrame(root)
    frame.grid()
    create_header(root)
    create_left_side(root)
    create_center(root)
    create_right_side(root)
    root.mainloop()

def create_header(root):#HEADER
    header = customtkinter.CTkFrame(root)
    header_label = customtkinter.CTkLabel(header, text="Header")
    header_label.grid(row=0,column=0,padx=10, pady=10)
    #button = customtkinter.CTkButton(app, text="my button", command=button_callback)
    #utton.grid(row=0, column=0, padx=20, pady=20)
    header.grid(row=0, column=0,padx=10, pady=10, sticky="ew")
    

def create_left_side(root):#LEFT SIDE
    left_side = customtkinter.CTkFrame(root)
    left_label = customtkinter.CTkLabel(left_side, text="Left side")
    left_label.grid(row=0,column=0,padx=10, pady=10)
    left_side.grid(row=1, column=0,padx=10, pady=10, sticky="nsw")

def create_center(root):#CENTER
    center = customtkinter.CTkFrame(root)
    center_label = customtkinter.CTkLabel(center, text="Center side")
    center_label.grid(row=0,column=0,padx=10, pady=10)
    #create_element_btn = customtkinter.CTkButton(center, text="Create element", command=create_el_logic)
    #create_element_btn.grid(row=0, column=0, padx=10, pady=20)
    center.grid(row=1, column=1,padx=0, pady=10, sticky="ns")

def create_right_side(root):#RIGHT SIDE
    right_side = customtkinter.CTkFrame(root)
    right_label = customtkinter.CTkLabel(right_side, text="Right side")
    right_label.grid(row=0,column=0,padx=10, pady=10)
    right_side.grid(row=1, column=2,padx=10, pady=10, sticky="nse")