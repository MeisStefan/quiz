from tkinter import Label, Button
from tkinter.constants import DISABLED, NORMAL

from model import *

current_question = 0

questions = ["In cate zile se sarbatoreste Craciunul?",
             "Care sunt culorile Craciunului?",
             "Ce culori aveau hainele lui Mos Craciun initial?",
             "Unde locuieste Mos Craciun?",
             "Ce se sarbatoreste in a 3-a zi de Craciun?",
             "In ce tara/tari se sarbatoreste Craciunul?",
             "Care este cea mai faimoasă bomboană în perioada Crăciunului?",
             "Care dintre următoarele NU este un cântec de Crăciun?",
             "Moș Crăciun a fost inspirat de care persoană reală?",
             "Ce simbolizează culoarea roșie în Crăciun?"]

options = ["3", "1", "4", "2",
           "rosu, verde, alb", "rosu, galben, albastru", "rosu, verde", "rosu, argintiu",
           "Albastre", "Portocalii", "Rosii", "Verzi",
           "Peste tot", "La Polul Nord", "In New York", "In Laponia, Finlanda",
           "Ajunul Craciunului", "Sfantul Stefan", "Craciunul", "Mos Nicolae",
           "Romania", "In tarile musulmane", "China", "In tarile crestine",
           "Mints", "Ouă de ciocolată", "Turta-dulce", "Bastoane de zahar",
           "Frosty the Snowman", "Twelve Days of Christmas", "Five Little Turkeys", "Jingle Bells",
           "Iisus", "Sfantul Nicolae", "Sfântul Francisc", "Dumnezeu",
           "Sangele lui Iisus", "Dragoste", "Coca-Cola", "Pericol"]

correct_answers = ["3",
                   "rosu, verde",
                   "Albastre",
                   "In Laponia, Finlanda",
                   "Sfantul Stefan",
                   "In tarile crestine",
                   "Bastoane de zahar",
                   "Five Little Turkeys",
                   "Sfantul Nicolae",
                   "Sangele lui Iisus"]

correct_answers_index = [1, 3, 1, 4, 2, 4, 4, 3, 2, 1]

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

def disable_buttons():
   global quiz_model
   for button in quiz_model.buttons_list:
        button.config(state = DISABLED)


def display_question():
    next_question()
    # shimb numele butoanelor cu noile optiuni
    global current_question
    global options
    number_of_options =4
    start = number_of_options * current_question
    end = start + number_of_options
    current_question_options = options[start:end:]

    # reactivez butoanele
    global quiz_model
    for i in range(number_of_options):
        current_button = quiz_model.buttons_list[i]
        current_button.config(text = current_question_options[i])
        current_button.config(state = NORMAL)

        # decolorez toate butoanele
        current_button.config(disabledforeground = "gray")

    # schimb numele intrebarii
    question_label = quiz_model.get_questions_label()
    question_label.config(text = questions[current_question])



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
    myLabel3 = Label(text= label_text + str(score) + "/" + str(len(questions)), font="Arial 30")
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

def restart_quiz(root, quiz_model):
    for i in range(4):
        current_button = quiz_model.buttons_list[i]
        current_button.pack_forget()
    current_label = quiz_model.get_questions_label()
    current_label.pack_forget()
    quiz_model.buttons_list.clear()
    create_start_screen(root, quiz_model)


def start_timer():

    pass


def stop_timer():

    pass