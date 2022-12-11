import Expenses


class Rental(Expenses.Expenses):
    def __init__(self, Invoice_Code, Date_Rental, Payment_Amount, Status):
        super().__init__(Invoice_Code, Date_Rental, Payment_Amount, Status)
