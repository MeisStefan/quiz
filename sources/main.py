global quiz_model

from controller import *

from model import *

from tkinter import *

mainWindow = Tk()
mainWindow.title("Christmas Quiz")
mainWindow.geometry("900x300")
create_start_screen(mainWindow, quiz_model)
menubar = Menu(mainWindow)
mainWindow.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(label='Exit', command=mainWindow.destroy)
file_menu.add_command(label='Restart', command=lambda: restart_quiz(mainWindow, quiz_model))
menubar.add_cascade(label="Menu", menu=file_menu)
timer = Label(text="15")
timer.place(relx = 0.5, rely= 1.0, anchor = "s")
quiz_model.store_timer(timer)
mainWindow.mainloop()