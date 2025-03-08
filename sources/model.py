class QuizModel:
    def __init__(self):
        self.score = 0
        self.buttons_list = []
        self.current_question = 0
        self.questions = ["In cate zile se sarbatoreste Craciunul?",
                          "Care sunt culorile Craciunului?",
                          "Ce culori aveau hainele lui Mos Craciun initial?",
                          "Unde locuieste Mos Craciun?",
                          "Ce se sarbatoreste in a 3-a zi de Craciun?",
                          "In ce tara/tari se sarbatoreste Craciunul?",
                          "Care este cea mai faimoasă bomboană în perioada Crăciunului?",
                          "Care dintre următoarele NU este un cântec de Crăciun?",
                          "Moș Crăciun a fost inspirat de care persoană reală?",
                          "Ce simbolizează culoarea roșie în Crăciun?"]
        self.options = ["3", "1", "4", "2",
                        "rosu, verde, alb", "rosu, galben, albastru", "rosu, verde", "rosu, argintiu",
                        "Albastre", "Portocalii", "Rosii", "Verzi",
                        "Peste tot", "La Polul Nord", "In New York", "In Laponia, Finlanda",
                        "Ajunul Craciunului", "Sfantul Stefan", "Craciunul", "Mos Nicolae",
                        "Romania", "In tarile musulmane", "China", "In tarile crestine",
                        "Mints", "Ouă de ciocolată", "Turta-dulce", "Bastoane de zahar",
                        "Frosty the Snowman", "Twelve Days of Christmas", "Five Little Turkeys", "Jingle Bells",
                        "Iisus", "Sfantul Nicolae", "Sfântul Francisc", "Dumnezeu",
                        "Sangele lui Iisus", "Dragoste", "Coca-Cola", "Pericol"]
        self.correct_answers = ["3",
                                "rosu, verde",
                                "Albastre",
                                "In Laponia, Finlanda",
                                "Sfantul Stefan",
                                "In tarile crestine",
                                "Bastoane de zahar",
                                "Five Little Turkeys",
                                "Sfantul Nicolae",
                                "Sangele lui Iisus"]
        self.correct_answers_index = [1, 3, 1, 4, 2, 4, 4, 3, 2, 1]

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
        return answer == self.correct_answers_index[self.current_question]

    def get_current_question_text(self):
        return self.questions[self.current_question]

    def update_question_text(self, new_question_name, new_question_index):
        self.questions[new_question_index] = new_question_name

    def update_answers_text(self, new_answers_name, new_question_index):
        for i in range(4):
            each_answer = new_answers_name[i]
            self.options[new_question_index * 4 + i] = each_answer

    def get_correct_answer_index(self, question_index):
        return self.correct_answers_index[question_index]-1

quiz_model = QuizModel()