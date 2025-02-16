from tkinter import *

def create_admin_page(quiz_model):
    admin_window = Tk()
    admin_window.title("Admin page")
    admin_window.geometry("900x900")
    quiz_questions = quiz_model.questions
    original_question = quiz_questions[0]
    display_quiz_question(quiz_model, admin_window, original_question)

    new_question_Button = Button(admin_window, text="Press for new question", font="Bolt 25")
    new_question_Button.grid(row=4, column=0, columnspan=3)

def display_quiz_question(quiz_model, admin_window, original_question):
    explicative_label_modified_question = Label(admin_window, text="Intrebarea 1:", font="Arial 25")
    explicative_label_modified_question.grid(row=0, column=0)
    question_title_Entry = Entry(admin_window, font="Arial 25", bd=5, fg="black", width=20)
    question_title_Entry.insert(0, original_question)
    question_title_Entry.grid(row=0, column=1)
    quiz_options = quiz_model.options
    original_answers = quiz_options[0:4:1]
    for i in range(4):
        answer_option_Entry = Entry(admin_window, font="Arial 25", bd=5, fg="black", width=20)
        answer_option_Entry.insert(0, original_answers[i])
        answer_option_Entry.grid(row=i, column=2)