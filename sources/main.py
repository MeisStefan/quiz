global quiz_model
from timer import *
from controller import *
from model import *
from tkinter import *
from admin_page import *
from quiz_page import *

mainWindow = Tk()
mainWindow.title("Christmas Quiz")
mainWindow.geometry("900x300")
create_start_screen(mainWindow, quiz_model)
menubar = Menu(mainWindow)
mainWindow.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(label='Exit', command=mainWindow.destroy)
file_menu.add_command(label='Restart', command=lambda: restart_quiz(mainWindow, quiz_model))
file_menu.add_command(label="Admin", command=lambda: create_admin_page(quiz_model))
menubar.add_cascade(label="Menu", menu=file_menu)
timer = Label()
timer.place(relx = 0.5, rely= 1.0, anchor = "s")
quiz_timer.store_timer(timer)
mainWindow.mainloop()