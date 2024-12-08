from tkinter import Label
from tkinter.constants import DISABLED, NORMAL

from model import *

current_question = 0

questions = ["Care este capitala Egiptului?", "Cand a inceput al doilea Razboi Mondial?", "Cine este Fernando Magellan?", "Cand a avut loc revolutia din '89?"]

options = ["Cairo", "Paris", "Berlin", "Roma", "1954", "1345", "1939", "1945","Un navigator", "Un extremist", "Un lider comunist", "Un lider fascist", "88", "1979", "2000", "89"]

correct_answers = ["Cairo", "1939", "Un navigator", "89"]

correct_answers_index = [1, 3, 1, 4]


def disable_buttons():
   global quiz_model
   for button in quiz_model.buttons_list:
        button.config(state = DISABLED)


def display_question():
    next_question()
    # shimb numele butoanelor cu noile optiuni
    global current_question
    global options
    number_of_questions =len(questions)
    start = number_of_questions * current_question
    end = start + number_of_questions
    current_question_options = options[start:end:]

    # reactivez butoanele
    global quiz_model
    for i in range(number_of_questions):
        current_button = quiz_model.buttons_list[i]
        current_button.config(text = current_question_options[i])
        current_button.config(state = NORMAL)

        # decolorez toate butoanele
        current_button.config(disabledforeground = "gray")

    # schimb numele intrebarii
    question_label = quiz_model.get_questions_label()
    question_label.config(text = questions[current_question])



def display_result():
    number_of_questions = len(questions)
    global quiz_model
    for i in range(number_of_questions):
        current_button = quiz_model.buttons_list[i]
        current_button.pack_forget()
    score_label = quiz_model.get_questions_label()
    score = quiz_model.score
    label_text = "Your score is "
    score_label.pack_forget()
    myLabel3 = Label(text= label_text + str(score), font="Arial 30")
    myLabel3.pack()

def select_answer(answer):
    global quiz_model
    selected_button = quiz_model.buttons_list[answer - 1]
    if answer == correct_answers_index[current_question]:
        # daca raspunsul e corect
        selected_button.config(disabledforeground="green")
        quiz_model.increase_score()
    else:
        selected_button.config(disabledforeground="red")

    disable_buttons()
    selected_button.after(2000, display_question)

def next_question():
    global current_question
    global questions
    if current_question < len(questions)-1:
        current_question += 1
    else:
        display_result()

def restart_quiz():

    pass


def start_timer():

    pass


def stop_timer():

    pass