class Quiz:
    def __init__(self, question_id, question, choice1, choice2, choice3, choice4, answer):
        self.__question_id = question_id
        self.__question = question
        self.__choice1 = choice1
        self.__choice2 = choice2
        self.__choice3 = choice3
        self.__choice4 = choice4
        self.__answer = answer

    def get_question_id(self):
        return self.__question_id

    def get_question(self):
        return self.__question

    def get_choice1(self):
        return self.__choice1

    def get_choice2(self):
        return self.__choice2

    def get_choice3(self):
        return self.__choice3

    def get_choice4(self):
        return self.__choice4

    def get_answer(self):
        return self.__answer

    def set_question_id(self, question_id):
        self.__question = question_id

    def set_question(self, question):
        self.__question = question

    def set_choice1(self, choice1):
        self.__choice1 = choice1

    def set_choice2(self, choice2):
        self.__choice2 = choice2

    def set_choice3(self, choice3):
        self.__choice3 = choice3

    def set_choice4(self, choice4):
        self.__choice4 = choice4

    def set_answer(self, answer):
        self.__answer = answer
