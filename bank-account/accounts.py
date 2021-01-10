class Account:

    def __init__(self, filepath):
        self._filepath = filepath
        with open(self._filepath, 'r') as readFile:
            self._balance = int(readFile.read())
    
    def getBalance(self):
        return self._balance

    def updateBalance(self):
        with open(self._filepath, 'w') as writeFile:
            writeFile.write(str(self._balance))
    
    def withdraw(self, amount):
        if amount > self._balance:
            print("withdrawal amount exceeds available balance")
            return
        self._balance = self._balance - amount
        self.updateBalance()

    def deposit(self, amount):
        self._balance = self._balance + amount
        self.updateBalance()


# MANUAL TESTS - Account
# account = Account('balance.txt')
# print(account.getBalance())
# account.withdraw(1200)
# print(account.getBalance())


class Checking(Account):
    """This class generates a checking account object"""
    type = "checking"

    def __init__(self, filepath):
        super().__init__(filepath)

    def transfer(self, amount, acctTo=None):
        self.withdraw(amount)
        if acctTo is not None:
            acctTo.deposit(amount)


# MANUAL TESTS - Checking
c = Checking("balance.txt")
c.transfer(110)
print(c.getBalance())
print(c.type)
print(c.__doc__)


"""
GLOSSARY

Class
Object instance
Instance variable
Class variable
Doc strings
Data member
Constructor
Methods
Instantiation
Inheritance
Attributes
"""