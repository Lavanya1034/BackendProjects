# bank account class


class BankAccount:
    def __init__(self, accNo, name, balance):
        self.accountNumber = accNo
        self.name = name
        self.balance = balance[1:]

    def deposit(self, depositAmt):
        self.balance = int(self.balance) + depositAmt

    def withdrawal(self, withdrawAmt):
        self.balance = int(self.balance) - withdrawAmt

    def display(self):
        print(f"Account Number : {self.accountNumber}")
        print(f"Account Name :  {self.name}")
        print(f"Account Balance :  {self.balance} $")


# creating an object

accNumber = 2178514584
accHolderName = "Tony"
bal = "$29800"

acc1 = BankAccount(accNumber, accHolderName, bal)
acc1.withdrawal(100)  # if we do withdrawal, the balance is calculated respectively.
acc1.display()
