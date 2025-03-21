from constants import QUIZ_QUESTIONS


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

quiz_model = QuizModel()