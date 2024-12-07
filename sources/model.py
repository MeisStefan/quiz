class QuizModel:
    def __init__(self):
        self.data = []

    def store_questions_label(self, label):
        self.questions_label = label

    def get_questions_label(self):
        return self.questions_label

buttons_list = []
quiz_model = QuizModel()