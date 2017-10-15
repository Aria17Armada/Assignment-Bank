from Class_Customer import Customer
from Class_Account import Account
import random
import sys


cusnames = []
money = random.randint(50000, 1000000)
balance = int(money)
Balance = Account(balance)


def menu():
    print("\nPlease choose one of these options:\n"
    "1.Get Customer\t"
    "2.Get number of customer\n"
    "3.Add customer\t"
    "4.Deposit\n"
    "5.Withdraw\t"
    "6.Check Balance\n"
    "7.Set Account\t"
    "8.Get Account\n"
    "9.Quit\n")


def accountcheck():
    global customer
    global firstname
    global lastname
    global account
    firstname = input("Please input your first name: ")
    lastname = input("Please input the last name: ")
    account = input("Please input the account type: ")
    customer = Customer(firstname, lastname, account)
    cusnames.append(customer.setCustomer(firstname, lastname, account))


def withd():
    alim = int(input("How much do you want withdraw?"))
    if alim > balance:
        print("Sorry,there isn't enough money on your account to do a withdrawal with")
        withd()
    else:
        Balance.withdraw(alim)
        print("Rp ", Balance.getBalance())
        main()


def main():
    menu()
    aleph = input("")
    if aleph == "1":
        print(customer.getName())
        main()
    if aleph == "2":
        print(len(cusnames))
        main()
    if aleph == "3":
        accountcheck()
        main()
    if aleph == "4":
        omega = int(input("how much do you want to deposit?"))
        Balance.deposit(omega)
        print("Rp ", Balance.getBalance())
        main()
    if aleph == "5":
        withd()
    if aleph == "6":
        print("Rp ", Balance.getBalance())
        main()
    if aleph == "7":
        account = input("please input the account")
        customer.setAccount(account)
        main()
    if aleph == "8":
        print(customer.getAccount())
        main()
    if aleph == "9":
        print("Thank you for visiting The Bank!")
        sys.exit()
    else:
        print("System error,please enter the correct commands")
        main()

accountcheck()
print("Welcome to The Bank,", firstname, lastname)
main()
