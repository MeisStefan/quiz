from controller import *

from model import *

# am folosit lambda pentru a transmite parametru functiei select_answer care, la randul ei, are transmisa ca parametru command
def start_quiz():
    myLabel2 = Label(root, text="In cate zile se sarbatoreste Craciunul?", font="Arial 20")
    myLabel2.pack()
    global quiz_model
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
    startButton.pack_forget()
    startLabel.pack_forget()


from tkinter import *
root = Tk()
root.title("Christmas Quiz")
root.geometry("600x300")
startLabel = Label(root, text="Christmas Quiz", font="Arial 25")
startLabel.pack()
startButton = Button(root, text="Start", font="Arial 25", command=start_quiz)
startButton.pack()
menubar = Menu(root)
root.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(label='Exit', command=root.destroy)
file_menu.add_command(label='Restart', command=restart_quiz)
menubar.add_cascade(label="Menu", menu=file_menu)

root.mainloop()