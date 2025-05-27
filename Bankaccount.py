import os
import datetime
import pandas as pd

class BankAccount(object):
    def __init__(self, name, accountNumber, accountType, balance = 0):
        self.name = name
        self.accountType = accountType
        self.accountNumber = accountNumber
        self.balance = balance
        self.filename = str(self.accountNumber)+"_"+self.accountType+"_"+self.name+".txt"
        current_time = datetime.datetime.now()
        if not os.path.exists(self.filename):
            with open(self.filename,'w',encoding='utf-8') as self.IDfile:
                self.IDfile.write(f'''
                                  Account created.
                                  Date: {current_time.ctime()}
                                  Name: {name}
                                  Account Number/Type: {accountNumber}/{accountType}
                                  Balance: {balance}''')


    def deposit(self,money):
        self.balance +=money
        with open(self.filename,'a',encoding='utf-8') as f:
            f.write(f'\n {money} deposited. Current balance: {self.balance}.')

    def withdraw(self,money):
        if money > self.balance:
            print(f'The requested withdrawal amount exeeds the balance!')
        else:
            self.balance -= money
            with open(self.filename,'a',encoding='utf-8') as f:
                f.write(f'\n {self.balance} withdrawn. Current balance: {self.balance}.')

    def get_balance(self):
        return(f'Current balance: {self.balance}.')
    
    def get_ID(self):
        return(f'Account number: {self.accountNumber}.')
    
    def get_username(self):
        return(f'Account number: {self.name}.')
    
    def get_type(self):
        return(f'Account number: {self.accountType}.')
    
    def transaction_hist(self):
        with open(self.filename,'r') as fname:
            trans_hist = ''
            while True:
                temp_str = fname.read()
                trans_hist = f'{trans_hist}{temp_str}'
                if temp_str == '':
                    break
        return trans_hist


if __name__ == "__main__":
    bank_account = BankAccount('James Dean',10001,'saving')
    bank_account.deposit(1000)
