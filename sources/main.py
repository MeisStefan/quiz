global quiz_model

from controller import *

from model import *

from tkinter import *


def create_start_screen(root, quiz_model):
    startLabel = Label(root, text="Christmas Quiz", font="Arial 25")
    quiz_model.store_start_label(startLabel)
    startLabel.pack()
    startButton = Button(root, text="Start", font="Arial 25", command=lambda: start_quiz(quiz_model, root))
    quiz_model.store_start_button(startButton)
    startButton.pack()

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