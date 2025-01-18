from tkinter import Label, Button
from tkinter.constants import DISABLED, NORMAL
from model import *

def create_start_screen(root, quiz_model):
    startLabel = Label(root, text="Christmas Quiz", font="Arial 25")
    quiz_model.store_start_label(startLabel)
    startLabel.pack()
    startButton = Button(root, text="Start", font="Arial 25", command=lambda: start_quiz(quiz_model, root))
    quiz_model.store_start_button(startButton)
    startButton.pack()

# am folosit lambda pentru a transmite parametru functiei select_answer care, la randul ei, are transmisa ca parametru command
def start_quiz(quiz_model, root):
    myLabel2 = Label(root, text="In cate zile se sarbatoreste Craciunul?", font="Arial 20")
    myLabel2.pack()
    quiz_model.store_questions_label(myLabel2)
    myButton1 = Button(root, text="3", font="Arial 15", command=lambda: select_answer(1))
    quiz_model.store_answer_button(myButton1)
    myButton1.pack()
    myButton2 = Button(root, text="1", font="Arial 15", command=lambda: select_answer(2))
    quiz_model.store_answer_button(myButton2)
    myButton2.pack()
    myButton3 = Button(root, text="4", font="Arial 15", command=lambda: select_answer(3))
    quiz_model.store_answer_button(myButton3)
    myButton3.pack()
    myButton4 = Button(root, text="2", font="Arial 15", command=lambda: select_answer(4))
    quiz_model.store_answer_button(myButton4)
    myButton4.pack()
    quiz_model.get_start_label().pack_forget()
    quiz_model.get_start_button().pack_forget()
    start_timer()

def disable_buttons():
   global quiz_model
   for button in quiz_model.buttons_list:
        button.config(state = DISABLED)

def display_question():
    next_question()
    # shimb numele butoanelor cu noile optiuni
    global quiz_model
    number_of_options =4
    start = number_of_options * quiz_model.get_current_question()
    end = start + number_of_options
    current_question_options = quiz_model.options[start:end:]

    # reactivez butoanele
    for i in range(number_of_options):
        current_button = quiz_model.buttons_list[i]
        current_button.config(text = current_question_options[i])
        current_button.config(state = NORMAL)

        # decolorez toate butoanele
        current_button.config(disabledforeground = "gray")

    # schimb numele intrebarii
    question_label = quiz_model.get_questions_label()
    question_label.config(text = quiz_model.questions[quiz_model.get_current_question()])
    reset_timer()
    start_timer()

def display_result():
    number_of_options = 4
    global quiz_model
    for i in range(number_of_options):
        current_button = quiz_model.buttons_list[i]
        current_button.pack_forget()
    score_label = quiz_model.get_questions_label()
    score = quiz_model.score
    label_text = "Your score is "
    score_label.pack_forget()
    myLabel3 = Label(text= label_text + str(score) + "/" + str(len(quiz_model.questions)), font="Arial 30")
    myLabel3.pack()

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
    selected_button.after(2000, display_question)

def next_question():
    global quiz_model
    if quiz_model.get_current_question() < len(quiz_model.questions)-1:
        quiz_model.increment_current_question()
    else:
        display_result()

def restart_quiz(root, quiz_model):
    for i in range(4):
        current_button = quiz_model.buttons_list[i]
        current_button.pack_forget()
    current_label = quiz_model.get_questions_label()
    current_label.pack_forget()
    quiz_model.buttons_list.clear()
    create_start_screen(root, quiz_model)
    reset_timer()

def start_timer():
    global quiz_model
    timer = quiz_model.get_timer()
    timer.config(text=quiz_model.get_current_timer_seconds())
    quiz_model.decrement_current_timer_seconds()
    if quiz_model.get_current_timer_seconds()==0:
        timer.config(text="Time's up!")
        timer.after(1000, display_question)
    else:
        timer.after(1000, start_timer)

def stop_timer():
    pass

def reset_timer():
    global quiz_model
    quiz_model.reset_timer()