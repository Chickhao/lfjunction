import User

class Payment(User.User):
    count_id =  0
    def __init__(self, username, password, account_number, account_name, security, expiration_month, expiration_year):
        super().__init__(username, password)
        Payment.count_id += 1
        self.__payment_id = Payment.count_id
        self.__account_name = account_name
        self.__account_number = account_number
        self.__security = security
        self.__expiration_month = expiration_month
        self.__expiration_year = expiration_year

    def set_payment_id(self,payment_id):
        self.__payment_id = payment_id

    def set_account_name(self, account_name):
        self.__account_name = account_name

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_security(self, security):
        self.__security = security

    def set_expiration_month(self, expiration_month):
        self.__expiration_month = expiration_month

    def set_expiration_year(self, expiration_year):
        self.__expiration_year = expiration_year

    def get_payment_id(self):
        return self.__payment_id

    def get_account_name(self):
        return self.__account_name

    def get_account_number(self):
        return self.__account_number

    def get_security(self):
        return self.__security

    def get_expiration_month(self):
        return self.__expiration_month

    def get_expiration_year(self):
        return self.__expiration_year
