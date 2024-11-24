from model import *

def start_quiz():
    myLabel = Label(root, text="Cine e Michael Jackson?", font="Arial 20")
    myLabel.pack()
    myButton1 = Button(root, text="un om de stiinta", font="Arial 15")
    myButton1.pack()
    myButton2 = Button(root, text="un breakdancer", font="Arial 15")
    myButton2.pack()
    myButton3 = Button(root, text="un cantaret faimos", font="Arial 15")
    myButton3.pack()
    myButton4 = Button(root, text="un astronaut", font="Arial 15")
    myButton4.pack()
    interface.startButton.grid_forget()


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
