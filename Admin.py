import User


class Admin(User.User):
    count_id = 10000

    def __init__(self, username, password, first_name, last_name):
        super().__init__(username, password)
        Admin.count_id += 1
        self.__adminId = Admin.count_id
        self.__first_name = first_name
        self.__last_name = last_name

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_adminId(self):
        return self.__adminId

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_email(self, email):
        self.__email = email

