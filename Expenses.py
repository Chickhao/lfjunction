class Expenses():
    count_id = 0

    def __init__(self, Invoice_Code, Date_Rental, Payment_Amount, Status):
        Expenses.count_id += 1
        self.__id = Expenses.count_id
        self.__Invoice_Code = Invoice_Code
        self.__Date_Rental = Date_Rental
        self.__Payment_Amount = Payment_Amount
        self.__Status = Status

    def get_id(self):
        return self.__id

    def get_Status(self):
        return self.__Status

    def get_Payment_Amount(self):
        return self.__Payment_Amount

    def get_Date_Rental(self):
        return str(self.__Date_Rental)

    def get_Invoice_Code(self):
        return self.__Invoice_Code

    def set_Invoice_Code(self, Invoice_Code):
        self.__Invoice_Code = Invoice_Code

    def set_Status(self, Status):
        self.__Status = Status

    def set_Payment_Amount(self, Payment_Amount):
        self.__Payment_Amount = Payment_Amount

    def set_Date_Rental(self, Date_Rental):
        self.__Date_Rental = str(Date_Rental)
