from controller import *

from model import *

# am folosit lambda pentru a transmite parametru functiei select_answer care, la randul ei, are transmisa ca parametru command
def start_quiz():
    myLabel2 = Label(root, text="Care este capitala Egiptului?", font="Arial 20")
    myLabel2.pack()
    global quiz_model
    quiz_model.store_questions_label(myLabel2)

    myButton1 = Button(root, text="Cairo", font="Arial 15", command=lambda: select_answer(1))
    buttons_list.append(myButton1)
    myButton1.pack()
    myButton2 = Button(root, text="Paris", font="Arial 15", command=lambda: select_answer(2))
    buttons_list.append(myButton2)
    myButton2.pack()
    myButton3 = Button(root, text="Berlin", font="Arial 15", command=lambda: select_answer(3))
    buttons_list.append(myButton3)
    myButton3.pack()
    myButton4 = Button(root, text="Roma", font="Arial 15", command=lambda: select_answer(4))
    buttons_list.append(myButton4)
    myButton4.pack()
    startButton.pack_forget()
    startLabel.pack_forget()


from tkinter import *
root = Tk()
root.title("General Knowledge Quiz")
root.geometry("500x300")
startLabel = Label(root, text="General Knowledge Quiz", font="Arial 25")
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