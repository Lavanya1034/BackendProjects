# abstraction


class Bank:
    def bank_info(self):
        print("Welcome to the bank")

    # abstract class
    def interest(self):
        pass


# child classes


class Sbi(Bank):
    def interest(self):
        print("In sbi bank 5 rupees interest")


class Axis(Bank):
    def interest(self):
        print("In Axis bank 8 rupees interest")


# object instances of class

sbi1 = Sbi()
axis1 = Axis()

sbi1.bank_info()
sbi1.interest()
axis1.bank_info()
axis1.interest()
