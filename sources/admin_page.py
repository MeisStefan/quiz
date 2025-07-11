from functools import partial
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from model import *
from constants import *

def create_admin_page(quiz_model):
    admin_window = Tk()
    admin_window.title("Admin Page")
    admin_window.geometry("900x600")

    frame = Frame(admin_window)
    frame.pack(fill=BOTH, expand=True)

    tree = ttk.Treeview(frame, columns=("Question", "Option 1", "Option 2", "Option 3", "Option 4"), show="headings")

    column_titles = ("Question", "Option 1", "Option 2", "Option 3", "Option 4")
    for col in column_titles:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor=CENTER)

    scrollbar = Scrollbar(frame, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)

    scrollbar.pack(side=RIGHT, fill=Y)
    tree.pack(fill=BOTH, expand=True)

    for quiz_question in quiz_model.questions_list:
        tree.insert("", "end", values=(quiz_question.question_title, *quiz_question.answers))

    def edit_item(event):
        selected_item = tree.selection()[0]
        values = tree.item(selected_item, "values")
        edit_window = Toplevel()
        edit_window.title("Edit Question")
        edit_window.geometry("500x300")

        Label(edit_window, text="Question:", font="Arial 12").pack()
        question_entry = Entry(edit_window, font="Arial 12", width=50)
        question_entry.insert(0, values[0])
        question_entry.pack()

        def change_correct_answer_index_of_question(event, selected_correct_answer_index):
            quiz_model.change_correct_answer_index(values[0], selected_correct_answer_index)
            correct_answer_entry = answer_entries[selected_correct_answer_index]
            for i in range(len(answer_entries)):
                answer_entries[i].config(fg="black")
                correct_answer_entry.config(fg="green")

        answer_entries = []
        for current_answer_index in range(4):
            correct_answer_index = quiz_model.get_correct_answer_index(question_index=tree.index(tree.selection()))
            Label(edit_window, text=f"Option {current_answer_index + 1}:", font="Arial 12").pack()
            text_color_at_entry_creation = "black"
            if correct_answer_index == current_answer_index:
                text_color_at_entry_creation = "green"
            entry = Entry(edit_window, font="Arial 12",fg=text_color_at_entry_creation, width=50)
            entry.insert(0, values[current_answer_index + 1])
            entry.pack()
            entry.bind("<Button-3>", partial(change_correct_answer_index_of_question, selected_correct_answer_index=current_answer_index))
            answer_entries.append(entry)

        def save_edit():
            new_question_name = question_entry.get()
            new_question_index = tree.index(tree.selection())
            new_values = [new_question_name] + [entry.get() for entry in answer_entries]
            tree.item(selected_item, values=new_values)
            quiz_model.update_question_text(new_question_name, new_question_index)
            new_answers_name = [entry.get() for entry in answer_entries]
            quiz_model.update_answers_text(new_answers_name, new_question_index)
            edit_window.destroy()

        Button(edit_window, text="Save", font="Arial 12", command=save_edit).pack(pady=10)

    tree.bind("<Double-1>", edit_item)
    def delete_question(event):
        response = messagebox.askyesno(DELETE_QUESTION_CONFIRMATION_TITLE, DELETE_QUESTION_CONFIRMATION_MESSAGE, parent=admin_window)
        if response:
            selected_item = tree.identify_row(event.y)
            values = tree.item(selected_item, "values")
            question_title = values[0]
            quiz_model.delete_question(question_title)
            tree.delete(selected_item)
    tree.bind("<Button-3>", delete_question)

    new_question_button = Button(admin_window, text="Press for new question", font="Arial 16",
                                 command=lambda: create_new_question(tree))
    new_question_button.pack(pady=10)

    admin_window.mainloop()

correct_answer_index = 1

def create_new_question(tree):
    new_window = Toplevel()
    new_window.title("Add New Question")
    new_window.geometry("500x300")

    Label(new_window, text="Question:", font="Arial 12").pack()
    question_entry = Entry(new_window, font="Arial 12", width=50)
    question_entry.pack()

    def change_correct_answer_index(event, selected_correct_answer_index):
        global correct_answer_index
        correct_answer_index = selected_correct_answer_index+1

    answer_entries = []
    for i in range(4):
        Label(new_window, text=f"Option {i + 1}:", font="Arial 12").pack()
        entry = Entry(new_window, font="Arial 12", width=50)
        entry.pack()
        answer_entries.append(entry)
        entry.bind("<Button-3>", partial(change_correct_answer_index, selected_correct_answer_index=i))

    def save_question():
        question_title = question_entry.get()
        options = [entry.get() for entry in answer_entries]
        tree.insert("", "end", values=(question_title, *options))
        new_window.destroy()
        new_question = QuizQuestion(question_title, options, "0", correct_answer_index)
        quiz_model.questions_list.append(new_question)

    Button(new_window, text="Save", font="Arial 12", command=save_question).pack(pady=10)