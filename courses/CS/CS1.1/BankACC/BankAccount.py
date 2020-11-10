from random import randrange
class BankAccount:
    balance = 0
    routing_number = 253000196



    def __init__(self, name):
        self.__ACCN = randrange(10000000,99999999,1)
        self.name = name
    def deposit(self, amount):
        self.balance += amount
        return (F"Amount Deposited: ${amount}")
    def withdraw(self, amount):
        if self.balance < amount:
            print("INSUFFICIENT FUNDS")
            self.balance -= 10
        self.balance -= amount
    def get_balance(self):
        print("Welcome to the Bank of Makeschool \n")
        return (F"{self.balance} is your balance")
    def add_interest(self):
        interest = self.balance*.00083
        self.balance += interest
    def print_receipt(self):
        ACCTN = str(self._BankAccount__ACCN)
        print(F""""                   {self.name} 
                    Account No.:****{ACCTN[4:]} 
                    Routing No.:{self.routing_number} 
                    Balance: {self.balance} \n"""
                    )

AJ = BankAccount("Ajani Levy")
AJ.deposit(50)
AJ.print_receipt()
MJ = BankAccount("Micheal Jordan")
MJ.deposit(90000000)
MJ.get_balance()
MJ.print_receipt()
KW = BankAccount("Kanye West")
KW.deposit(40000000)
KW.add_interest()
KW.add_interest()
KW.add_interest()
KW.add_interest()
KW.add_interest()
KW.add_interest()
KW.print_receipt()