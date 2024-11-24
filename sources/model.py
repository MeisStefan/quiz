from tkinter import *
root = Tk()

class QuizInterface:
    def __init__(self, label, startButton):
        self.label = label
        self.startButton = startButton


interface = QuizInterface(Label(), Button())