class QuizModel:
    def __init__(self):
        self.score = 0
        self.buttons_list = []

    def store_questions_label(self, label):
        self.questions_label = label

    def get_questions_label(self):
        return self.questions_label

    def increase_score(self):
        self.score = self.score + 1

    def store_answer_button(self, button):
        self.buttons_list.append(button)

quiz_model = QuizModel()