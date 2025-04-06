from constants import QUIZ_QUESTIONS, QUESTIONS_FILE
import os
import json

from quiz_question import QuizQuestion


class QuizModel:
    def __init__(self):
        self.score = 0
        self.buttons_list = []
        self.current_question = 0
        self.questions_list = QUIZ_QUESTIONS

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
        return current_question.question

    def update_question_text(self, new_question_name, new_question_index):
        self.questions_list[new_question_index].question = new_question_name

    def update_answers_text(self, new_answers_name, new_question_index):
        for i in range(4):
            each_answer = new_answers_name[i]
            self.questions_list[new_question_index].answers[i] = each_answer

    def get_correct_answer_index(self, question_index):
        question = self.questions_list[question_index]
        return question.correct_answer_index-1

    def restart(self):
        self.buttons_list.clear()
        self.current_question = 0
        self.score = 0
        self.score_label.pack_forget()

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
            question=q["question"],
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

quiz_model = QuizModel()
quiz_model.load_questions()