class BankAccount(object):
    def __init__(self, name, accountNumber, accountType, balance = 0):
        self.name = name
        self.accountType = accountType
        self.accountNumber = accountNumber
        self.balance = balance
        self.filename = str(self.accountNumber)+"_"+self.accountType+"_"+self.name+".txt"
    def deposit(self,money):
