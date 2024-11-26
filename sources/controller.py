from tkinter import *


def start_quiz():
    root = Tk()
    root.title("General Knowledge Quiz")
    root.geometry("500x150")
    myLabel = Label(root, text="General Knowledge Quiz", font="Arial 25")
    myLabel.pack()
    myButton = Button(root, text="Start", font="Arial 25")
    myButton.pack()
    menubar = Menu(root)
    root.config(menu=menubar)
    file_menu = Menu(menubar, tearoff=False)
    file_menu.add_command(label='Exit', command=root.destroy)
    file_menu.add_command(label='Restart')
    menubar.add_cascade(label="Menu", menu=file_menu)
    root.mainloop()
    pass

def update_timer():
    # TODO
    pass


def disable_buttons():
    # TODO
    pass


def display_question():
    # TODO
    pass


def display_result():
    # TODO
    pass


def select_answer():
    # TODO
    pass


def next_question():
    # TODO
    pass


def restart_quiz():
    # TODO
    pass


def exit_quiz():
    # TODO
    pass
