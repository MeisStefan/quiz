from main import myLabel
from model import *
limit = 10
time = 0
global myButton1
global myButton2
global myButton3
global myButton4
questions = ["Care este capitala Egiptului?", "Cand a inceput al doilea Razboi Mondial?", "Cine este Fernando Magellan?", "Cand a avut loc revolutia din '89?"]

options = ["Cairo, Paris, Berlin, Roma", "1954, 1345, 1939, 1945","Un navigator, Un extremist, Un lider comunist, Un lider fascist", "88, 1979, 2000, '89"]

correct_answers = ["Cairo", "1939", "Un navigator", "89"]

def start_quiz():
    myLabel2 = Label(root, text="Care este capitala Egiptului?", font="Arial 20")
    myLabel2.pack()
    myButton1 = Button(root, text="Cairo", font="Arial 15")
    myButton1.pack()
    myButton2 = Button(root, text="Paris", font="Arial 15")
    myButton2.pack()
    myButton3 = Button(root, text="Berlin", font="Arial 15")
    myButton3.pack()
    myButton4 = Button(root, text="Roma", font="Arial 15")
    myButton4.pack()


def disable_buttons():

    pass


def display_question():

    pass


def display_result():
    # TODO
    pass


def select_answer():
    # TODO
    pass


def next_question():

    pass


def restart_quiz():
    myLabel.pack_hide()
    pass


def start_timer():

    pass


def stop_timer():

    pass