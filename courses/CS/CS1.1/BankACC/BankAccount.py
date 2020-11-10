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
        print("Welcome to the Bank of Makeschool")
        return (F"{self.balance} is your balance")
    def add_interest(self):
        interest = self.balance*.00083
        self.balance += interest
    def print_receipt(self):
        ACCTN = str(self._BankAccount__ACCN)
        print(F""""                   {self.name} 
                    Account No.:****{ACCTN[4:]} 
                    Routing No.:{self.routing_number} 
                    Balance: {self.balance}""")

AJ = BankAccount("Ajani Levy")
AJ.deposit(5000)
AJ.print_receipt()