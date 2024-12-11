global quiz_model

from controller import *

from model import *

from tkinter import *


root = Tk()
root.title("Christmas Quiz")
root.geometry("900x300")
create_start_screen(root, quiz_model)
menubar = Menu(root)
root.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(label='Exit', command=root.destroy)
file_menu.add_command(label='Restart', command=lambda: restart_quiz(root, quiz_model))
menubar.add_cascade(label="Menu", menu=file_menu)

root.mainloop()