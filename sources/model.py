class QuizModel:
    def __init__(self):
        self.score = 0

    def store_questions_label(self, label):
        self.questions_label = label

    def get_questions_label(self):
        return self.questions_label

    def increase_score(self):
        self.score = self.score + 1

buttons_list = []
quiz_model = QuizModel()