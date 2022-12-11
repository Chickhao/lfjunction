import Expenses


class Salary(Expenses.Expenses):
    def __init__(self, Invoice_Code, Date_Rental, Payment_Amount, Status, name):
        super().__init__(Invoice_Code, Date_Rental, Payment_Amount, Status)
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
