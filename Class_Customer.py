from Class_Account import Account


class Customer:
    def __init__(self, firstname, lastname, account):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__account = account

    def getFirst(self):
        return self.__firstname

    def getLast(self):
        return self.__lastname

    def getAccount(self):
        return self.__account

    def setAccount(self, account):
        self.__account = account

    def setCustomer(self, firstname, lastname, account):
        customer = Customer(firstname, lastname, account)
        return customer

    def getName(self):
        print("Customer:", self.__firstname, self.__lastname)
