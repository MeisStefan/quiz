from constants import QUIZ_QUESTIONS, QUESTIONS_FILE
import os
import json
from tkinter.constants import DISABLED
from quiz_question import QuizQuestion


class QuizModel:
    def __init__(self):
        self.score = 0
        self.buttons_list = []
        self.current_question = 0
        self.questions_list = QUIZ_QUESTIONS

    def store_main_window(self, main_window):
        self.main_window = main_window

    def get_main_window(self):
        return self.main_window

    def store_questions_label(self, label):
        self.questions_label = label

    def get_questions_label(self):
        return self.questions_label

    def increase_score(self):
        self.score = self.score + 1

    def store_answer_button(self, button):
        self.buttons_list.append(button)

    def store_start_label(self, label):
        self.start_label = label

    def get_start_label(self):
        return  self.start_label

    def store_start_button(self, button):
        self.start_button = button

    def get_start_button(self):
        return self.start_button

    def get_current_question(self):
        return self.current_question

    def increment_current_question(self):
        self.current_question +=1

    def is_correct_answer(self, answer):
        current_question = self.questions_list[self.current_question]
        return answer == current_question.correct_answer_index

    def get_current_question_text(self):
        current_question = self.questions_list[self.current_question]
        return current_question.question_title

    def update_question_text(self, new_question_name, new_question_index):
        self.questions_list[new_question_index].question_title = new_question_name

    def update_answers_text(self, new_answers_name, new_question_index):
        for i in range(4):
            each_answer = new_answers_name[i]
            self.questions_list[new_question_index].answers[i] = each_answer

    def get_correct_answer_index(self, question_index):
        question = self.questions_list[question_index]
        return question.correct_answer_index-1

    def change_correct_answer_index(self, question_title, new_correct_answer_index):
        for question_index in range(len(self.questions_list)):
            if self.questions_list[question_index].question_title == question_title:
                self.questions_list[question_index].correct_answer_index = new_correct_answer_index+1

    def restart(self):
        self.buttons_list.clear()
        self.score = 0
        if self.current_question+1==len(self.questions_list):
            self.score_label.pack_forget()
        self.current_question = 0
        self.file_menu.entryconfig("Restart", state= DISABLED)

    def load_questions(self):
        # load questions from file
        home_dir = os.path.expanduser("~")
        quiz_file_path = os.path.join(home_dir, QUESTIONS_FILE)
        # Verificăm dacă fișierul există
        if os.path.exists(quiz_file_path):
            with open(quiz_file_path, 'r', encoding='utf-8') as file:
                quiz_questions = json.load(file)
        else:
            # Dacă fișierul nu există, folosim lista default
            quiz_questions_dict = [q.to_dict() for q in QUIZ_QUESTIONS]
            # Salvăm lista default într-un fișier pentru viitor
            with open(quiz_file_path, 'w', encoding='utf-8') as file:
                json.dump(quiz_questions_dict, file, ensure_ascii=False, indent=4)

        self.questions_list = [QuizQuestion(
            question_title=q["question"],
            answers=q["answers"],
            correct_answer=q["correct_answer"],
            correct_answer_index=q["correct_answer_index"]
        ) for q in quiz_questions]

    def save_quiz_questions_to_file(self):
        # Transformăm fiecare obiect QuizQuestion într-un dicționar
        quiz_questions_dict = [q.to_dict() for q in self.questions_list]

        # Salvăm lista de dicționare într-un fișier JSON
        home_dir = os.path.expanduser("~")
        quiz_file_path = os.path.join(home_dir, QUESTIONS_FILE)
        with open(quiz_file_path, 'w', encoding='utf-8') as file:
            json.dump(quiz_questions_dict, file, ensure_ascii=False, indent=4)

    def store_score_label(self, label):
        self.score_label = label

    def store_file_menu(self, Menu):
        self.file_menu = Menu

    def get_file_menu(self):
        return self.file_menu

    def store_current_question_label(self, label):
        self.current_question_label = label

    def get_current_question_label(self):
        return self.current_question_label

quiz_model = QuizModel()
quiz_model.load_questions()