from tkinter import Label, Button
from tkinter.constants import DISABLED, NORMAL
from model import *
from timer import *

def disable_buttons():
   global quiz_model
   for button in quiz_model.buttons_list:
        button.config(state = DISABLED)

def display_question():
    next_question()
    global quiz_model
    global quiz_timer
    show_current_question(quiz_model)

    current_question_index = quiz_model.get_current_question()
    current_question = quiz_model.questions_list[current_question_index]
    current_question_answers = current_question.answers

    for i in range(len(current_question_answers)):
        current_button = quiz_model.buttons_list[i]
        current_button.config(text = current_question_answers[i])
        current_button.config(state = NORMAL)
        current_button.config(disabledforeground = "gray")

    question_label = quiz_model.get_questions_label()
    question_label.config(text = quiz_model.get_current_question_text())

    reset_timer()
    if current_question_index <= len(quiz_model.questions_list) - 1:
        start_timer()
    else:
        quiz_timer.hide_timer()

def display_result():
    number_of_options = 4
    global quiz_model
    quiz_model.get_current_question_label().pack_forget()
    for i in range(number_of_options):
        current_button = quiz_model.buttons_list[i]
        current_button.pack_forget()
    questions_label = quiz_model.get_questions_label()
    score = quiz_model.score
    label_text = "Your score is "
    questions_label.pack_forget()
    score_label = Label(text= label_text + str(score) + "/" + str(len(quiz_model.questions_list)), font="Arial 30")
    score_label.pack()
    quiz_model.store_score_label(score_label)
    quiz_model.get_file_menu().entryconfig("Admin", state=NORMAL)

def select_answer(answer):
    global quiz_model
    selected_button = quiz_model.buttons_list[answer - 1]
    if quiz_model.is_correct_answer(answer):
        # daca raspunsul e corect
        selected_button.config(disabledforeground="green")
        quiz_model.increase_score()
    else:
        selected_button.config(disabledforeground="red")

    disable_buttons()
    stop_timer()
    if quiz_model.get_current_question() < len(quiz_model.questions_list):
        selected_button.after(2000, display_question)
    else:
        selected_button.after(2000, display_result)

def next_question():
    global quiz_model
    if quiz_model.get_current_question() < len(quiz_model.questions_list)-1:
        quiz_model.increment_current_question()
    else:
        display_result()

def restart_quiz(root, quiz_model, create_start_screen):
    quiz_model.get_current_question_label().pack_forget()
    for i in range(4):
        current_button = quiz_model.buttons_list[i]
        current_button.pack_forget()
    current_label = quiz_model.get_questions_label()
    current_label.pack_forget()
    quiz_model.restart()
    create_start_screen(root, quiz_model)
    stop_timer()
    reset_timer()
    quiz_timer.hide_timer()
    quiz_model.get_file_menu().entryconfig("Admin", state=NORMAL)

def start_timer():
    global quiz_timer
    timer = quiz_timer.get_timer()
    timer.config(text=quiz_timer.get_current_timer_seconds())
    quiz_timer.decrement_current_timer_seconds()
    if quiz_timer.get_current_timer_seconds()==0:
        timer.config(text="Time's up!")
        timer_id = timer.after(1000, display_question)
    else:
        timer_id = timer.after(1000, start_timer)
    quiz_timer.store_timer_ID(timer_id)

def stop_timer():
    global quiz_timer
    quiz_timer.cancel_timer()

def reset_timer():
    global quiz_timer
    quiz_timer.reset_timer()

def show_current_question(quiz_model):
    text = "Question "
    yeeayv = str(quiz_model.get_current_question()+1)
    quiz_model.get_current_question_label().config(text= text + yeeayv + "/" + str(len(quiz_model.questions_list)), font="Arial 15")