from tkinter import *

def create_admin_page(quiz_model):
    admin_window = Tk()
    admin_window.title("Admin page")
    admin_window.geometry("900x900")
    quiz_questions = quiz_model.questions
    for i in range(len(quiz_questions)):
        original_question = quiz_questions[i]
        display_quiz_question(quiz_model, admin_window, original_question, original_question_index=i)
    new_question_Button = Button(admin_window, text="Press for new question", font="Bolt 25", command=lambda:create_new_question(admin_window, new_question_Button))
    new_question_Button.grid(row=len(quiz_questions) * 4, column=0, columnspan=3)

def display_quiz_question(quiz_model, admin_window, original_question, original_question_index):
    label_question_index = str(original_question_index + 1)
    explicative_label_modified_question = Label(admin_window, text="Intrebarea " + label_question_index + ":", font="Arial 25")
    explicative_label_modified_question.grid(row=original_question_index * 4, column=0)
    question_title_Entry = Entry(admin_window, font="Arial 25", bd=5, fg="black", width=20)
    question_title_Entry.insert(0, original_question)
    question_title_Entry.grid(row=original_question_index * 4, column=1)
    quiz_options = quiz_model.options
    number_of_options = 4
    start = number_of_options * original_question_index
    end = start + number_of_options
    original_answers = quiz_options[start:end:]
    for i in range(4):
        answer_option_Entry = Entry(admin_window, font="Arial 25", bd=5, fg="black", width=20)
        answer_option_Entry.insert(0, original_answers[i])
        answer_option_Entry.grid(row=original_question_index * 4 + i, column=2)

def create_new_question(admin_window, new_question_button):
    explicative_label_new_question = Label(admin_window, text="New question & answers:", font="Arial 25")
    explicative_label_new_question.grid(row=4, column=0)
    new_question_Entry = Entry(admin_window, font="Arial 25", bd=5, fg="black", width=20)
    new_question_Entry.grid(row=4, column=1)
    for i in range(4):
        new_answer_Entry = Entry(admin_window, font="Arial 25", bd=5, fg="black", width=20)
        new_answer_Entry.grid(row=i + 4, column=2)
    new_question_button.grid_forget()