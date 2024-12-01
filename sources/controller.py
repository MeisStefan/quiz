from tkinter.constants import DISABLED

from model import *

current_question = 0

questions = ["Care este capitala Egiptului?", "Cand a inceput al doilea Razboi Mondial?", "Cine este Fernando Magellan?", "Cand a avut loc revolutia din '89?"]

options = ["Cairo", "Paris", "Berlin", "Roma", "1954", "1345", "1939", "1945","Un navigator", "Un extremist", "Un lider comunist", "Un lider fascist", "88", "1979", "2000", "89"]

correct_answers = ["Cairo", "1939", "Un navigator", "89"]

correct_answers_index = [1, 3, 1, 4]


def disable_buttons():
   global buttons_list
   for button in buttons_list:
        button.config(state=DISABLED)


def display_question():
    next_question()
    # shimb numele butoanelor cu noile optiuni
    global current_question
    global options
    start = 4 * current_question
    end = start + 4
    current_question_options = options[start:end:]
    print(current_question_options)

    global buttons_list
    for i in range(4):
        current_button = buttons_list[i]
        current_button.config(text = current_question_options[i])

    # schimb numele intrebarii
    # reactivez butoanele
    # decolorez toate butoanele



def display_result():

    pass


def select_answer(answer):
    global buttons_list
    selected_button = buttons_list[answer - 1]
    if answer == correct_answers_index[current_question]:
        # daca raspunsul e corect
        selected_button.config(disabledforeground="green")
    else:
        selected_button.config(disabledforeground="red")
    disable_buttons()
    selected_button.after(2000, display_question)

def next_question():
    global current_question
    current_question += 1


def restart_quiz():

    pass


def start_timer():

    pass


def stop_timer():

    pass