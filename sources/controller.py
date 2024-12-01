from model import *

current_question = 0

questions = ["Care este capitala Egiptului?", "Cand a inceput al doilea Razboi Mondial?", "Cine este Fernando Magellan?", "Cand a avut loc revolutia din '89?"]

options = ["Cairo, Paris, Berlin, Roma", "1954, 1345, 1939, 1945","Un navigator, Un extremist, Un lider comunist, Un lider fascist", "88, 1979, 2000, '89"]

correct_answers = ["Cairo", "1939", "Un navigator", "89"]

correct_answers_index = [1, 3, 1, 4]


def disable_buttons():

    pass


def display_question():

    pass


def display_result():
    # TODO
    pass


def select_answer(answer):
    global buttons_list
    selected_button = buttons_list[answer]
    if answer == correct_answers_index[current_question]:
        # daca raspunsul e corect
        selected_button.config(fg="green")
    else:
        print("wrong")

def next_question():
    global current_question
    current_question += 1
    pass


def restart_quiz():

    pass


def start_timer():

    pass


def stop_timer():

    pass