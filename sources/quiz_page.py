from controller import *
from constants import *
from tkinter import *

def create_start_screen(root, quiz_model):
    startLabel = Label(root, text= QUIZ_PAGE_START_TEXT, font=QUIZ_PAGE_START_FONT)
    quiz_model.store_start_label(startLabel)
    startLabel.pack()
    startButton = Button(root, text= QUIZ_PAGE_START_BUTTON, font=QUIZ_PAGE_START_FONT, command=lambda: start_quiz(quiz_model, root))
    quiz_model.store_start_button(startButton)
    startButton.pack()

def start_quiz(quiz_model, root):
    myLabel2 = Label(root, text= quiz_model.questions[0], font= QUIZ_PAGE_TITLE_FONT)
    myLabel2.pack()
    quiz_model.store_questions_label(myLabel2)
    myButton1 = Button(root, text= quiz_model.options[0], font= QUIZ_PAGE_ANSWERS_FONT, command=lambda: select_answer(1))
    quiz_model.store_answer_button(myButton1)
    myButton1.pack()
    myButton2 = Button(root, text =quiz_model.options[1], font=QUIZ_PAGE_ANSWERS_FONT, command=lambda: select_answer(2))
    quiz_model.store_answer_button(myButton2)
    myButton2.pack()
    myButton3 = Button(root, text =quiz_model.options[2], font=QUIZ_PAGE_ANSWERS_FONT, command=lambda: select_answer(3))
    quiz_model.store_answer_button(myButton3)
    myButton3.pack()
    myButton4 = Button(root, text =quiz_model.options[3], font=QUIZ_PAGE_ANSWERS_FONT, command=lambda: select_answer(4))
    quiz_model.store_answer_button(myButton4)
    myButton4.pack()
    quiz_model.get_start_label().pack_forget()
    quiz_model.get_start_button().pack_forget()
    start_timer()
