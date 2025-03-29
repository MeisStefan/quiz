
class QuizQuestion:
    def __init__(self, question, answers, correct_answer, correct_answer_index):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer
        self.correct_answer_index = correct_answer_index

    def to_dict(self):
        return {
            "question": self.question,
            "answers": self.answers,
            "correct_answer": self.correct_answer,
            "correct_answer_index": self.correct_answer_index
            }
