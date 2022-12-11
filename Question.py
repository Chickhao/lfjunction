import User


class Question(User.User):
    count_id = 0

    def __init__(self, first_name, last_name, message, date):
        super().__init__(first_name, last_name)
        Question.count_id += 1
        self.__question_id = Question.count_id
        self.__message = message
        self.__date = date

    def get_question_id(self):
        return self.__question_id

    def get_message(self):
        return self.__message

    def get_date(self):
        return self.__date

    def set_question_id(self, question_id):
        self.__question_id = question_id

    def set_message(self, message):
        self.__message = message

    def set_date(self, date):
        self.__date = date
