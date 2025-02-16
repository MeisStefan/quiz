from tkinter import *

def create_admin_page(quiz_model):
    admin_window = Tk()
    admin_window.title("Admin page")
    admin_window.geometry("900x900")
    quiz_questions = quiz_model.questions
    #for i in range(len(quiz_questions)):
    original_question = quiz_questions[0]
    explicative_label_modified_question = Label(admin_window, text="Intrebarea 1:", font="Arial 25")
    explicative_label_modified_question.grid(row=0, column=0)
    modified_questions_Entry = Entry(admin_window, font="Arial 25", bd=5, fg="black", width=20)
    modified_questions_Entry.insert(0, original_question)
    modified_questions_Entry.grid(row=0, column=1)
    quiz_options = quiz_model.options
    #for i in range(len(quiz_options)):
    original_answers = quiz_options[0:1:3]
    modified_answer_Entry1 = Entry(admin_window, font="Arial 25", bd=5, fg="black", width=20)
    modified_answer_Entry1.insert(0, original_answers)
    modified_answer_Entry1.grid(row=0, column=2)
    modified_answer_Entry2 = Entry(admin_window, font="Arial 25", bd=5, fg="black", width=20)
    modified_answer_Entry2.insert(0, original_answers)
    modified_answer_Entry2.grid(row=1, column=2)
    modified_answer_Entry3 = Entry(admin_window, font="Arial 25", bd=5, fg="black", width=20)
    modified_answer_Entry3.insert(0, original_answers)
    modified_answer_Entry3.grid(row=2, column=2)
    modified_answer_Entry4 = Entry(admin_window, font="Arial 25", bd=5, fg="black", width=20)
    modified_answer_Entry4.insert(0, original_answers)
    modified_answer_Entry4.grid(row=3, column=2)
    new_question_Button = Button(admin_window, text="Press for new question", font="Bolt 25")
    new_question_Button.grid(row=4, column=0, columnspan=3)
