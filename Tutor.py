import User


class Tutor(User.User):
    count_id = 1000

    def __init__(self, username, password, first_name, last_name, date_of_birth, email, gender, postal_code, race,
                 phone, subject):
        super().__init__(username, password)
        Tutor.count_id += 1
        self.__tutorId = Tutor.count_id
        super().__init__(username, password)
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__email = email
        self.__gender = gender
        self.__postal_code = postal_code
        self.__race = race
        self.__phone = phone
        self.__subject = subject

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_email(self):
        return self.__email

    def get_gender(self):
        return self.__gender

    def get_postal_code(self):
        return self.__postal_code

    def get_race(self):
        return self.__race

    def get_phone(self):
        return self.__phone

    def get_subject(self):
        return self.__subject

    def get_tutorId(self):
        return self.__tutorId

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def set_email(self, email):
        self.__email = email

    def set_gender(self, gender):
        self.__gender = gender

    def set_postal_code(self, postal_code):
        self.__postal_code = postal_code

    def set_race(self, race):
        self.__race = race

    def set_phone(self, phone):
        self.__phone = phone

    def set_subject(self, subject):
        self.__subject = subject

    def set_tutorId(self, tutorID):
        self.__tutorId = tutorID
