from tkinter import *
from tkinter import ttk

def create_main_window():
    root = Tk()
    root.title('Password manager')
    root.geometry('900x600')
    frame = ttk.Frame(root)
    frame.pack()
    create_left_side()
    root.mainloop()

def create_left_side():
    left_side = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10],width=100,height=50)# внутренний padding
    left_label = ttk.Label(left_side, text="Left side")
    left_label.pack(anchor=NW)

    left_side.pack_propagate(0)
    left_side.pack(anchor=NW, fill=Y,padx=10, pady=10,side=LEFT)# внешний padding