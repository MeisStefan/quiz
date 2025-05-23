global quiz_model
from timer import *
from controller import *
from model import *
from tkinter import *
from admin_page import *
from quiz_page import *

main_window = Tk()
main_window.title("Quiz")
main_window.geometry("900x300")
create_start_screen(main_window, quiz_model)
menubar = Menu(main_window)
main_window.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)
quiz_model.store_file_menu(file_menu)
file_menu.add_command(label='Exit', command=main_window.destroy)
file_menu.add_command(label='Restart', command=lambda: restart_quiz(main_window, quiz_model, create_start_screen))
file_menu.add_command(label="Admin", command=lambda: create_admin_page(quiz_model))
file_menu.add_command(label="Save Quiz", command=lambda: quiz_model.save_quiz_questions_to_file())
file_menu.entryconfig("Restart", state= DISABLED)
menubar.add_cascade(label="Menu", menu=file_menu)
timer = Label()
timer.place(relx = 0.5, rely= 1.0, anchor = "s")
quiz_timer.store_timer(timer)
quiz_model.store_main_window(main_window)
main_window.mainloop()