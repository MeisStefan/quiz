from controller import *

from model import *

from tkinter import *
root = Tk()
root.title("Christmas Quiz")
root.geometry("900x300")
startLabel = Label(root, text="Christmas Quiz", font="Arial 25")
startLabel.pack()
startButton = Button(root, text="Start", font="Arial 25", command=lambda: start_quiz(quiz_model, root, startLabel, startButton))
startButton.pack()
menubar = Menu(root)
root.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(label='Exit', command=root.destroy)
file_menu.add_command(label='Restart', command=lambda: restart_quiz(root, startLabel, startButton))
menubar.add_cascade(label="Menu", menu=file_menu)

root.mainloop()