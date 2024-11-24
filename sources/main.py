from tkinter import *
from controller import *

def createInterface(root):
    root.title("General Knowledge Quiz")
    root.geometry("500x150")
    myLabel = Label(root, text="General Knowledge Quiz", font="Arial 25")
    myLabel.pack()
    myButton = Button(root, text="Start", font="Arial 25")
    myButton.pack()
    menubar = Menu(root)
    root.config(menu=menubar)
    file_menu = Menu(menubar, tearoff=False)
    file_menu.add_command(label='Exit', command=root.destroy)
    file_menu.add_command(label='Restart', command=restart_quiz)
    menubar.add_cascade(label="Menu", menu=file_menu)

root = Tk()
createInterface(root)
root.mainloop()

