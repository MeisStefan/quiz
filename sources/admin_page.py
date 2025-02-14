from tkinter import *

def create_admin_page(quiz_model):

    admin_window = Tk()
    admin_window.title("Admin page")
    admin_window.geometry("900x900")
    quiz_questions = quiz_model.questions
    original_question = quiz_questions[0]
    explicative_label_modified_question = Label(admin_window, text="Modify the question below:", font="Arial 25")
    explicative_label_modified_question.pack()
    modified_questions_Entry = Entry(admin_window, font="Arial 25", bd=5, fg="black", width=20)
    modified_questions_Entry.insert(0, original_question)
    modified_questions_Entry.pack()
    explicative_label_new_question = Label(admin_window, text="Insert the new question below:", font="Arial 25")
    explicative_label_new_question.pack()
    new_questions_Entry = Entry(admin_window, font="Arial 25", bd=5, fg="black", width=20)
    new_questions_Entry.pack()
