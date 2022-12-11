class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__userId = 0

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_userId(self):
        return self.__userId

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def set_userId(self, userID):
        self.__userId = userID
