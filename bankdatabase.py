import os
import datetime
import pandas as pd


class AccountDatabase:
    def __init__(self, db_directory):
        self.db_directory = db_directory
        if os.path.exists(db_directory):
            self.db = pd.read_csv(db_directory)
        else:
            self.db = pd.DataFrame(columns=["date", "name", "account_number", "account_type", "balance"], index=[])
            self.db.to_csv(db_directory, index=0)


    # create
    def insert(self, acc_info):
        
        acc_info = {self.db.columns[i]: acc_info[i] for i in range(len(self.db.columns))}
        if len(self.db[self.db["account_number"]==acc_info["account_number"]]) == 0:
            acc_info = pd.DataFrame(acc_info, index=[0])
            self.db = pd.concat([self.db, acc_info], ignore_index=True)
        else:
            print("The account number already exists in the database")

    
    # read
    def read(self, account_number):
        return self.db[self.db["account_number"]==account_number]


    # update
    def update(self, account_number, acc_info):
        acc_info = {self.db.columns[i]: acc_info[i] for i in range(len(self.db.columns))}
        mask = self.db["account_number"]==account_number
        row_index = mask[mask==True].index[0]
        acc_info = pd.DataFrame(acc_info, index=[row_index])
        self.db.update(acc_info)


    # delete
    def delete(self, account_number):
        mask = self.db["account_number"]==account_number
        row_index = mask[mask==True].index[0]
        self.db.drop(index=row_index, axis=0, inplace=True)


    def __del__(self):
        print("destructor called")
        self.db.to_csv(self.db_directory, index=0)


if __name__ == "__main__":
    db = AccountDatabase("data\db.csv")
    james_account = {
        "date": datetime.datetime.now(),
        "name": "James Dean",
        "account_number": 10001,
        "account_type": "savings",
        "balance": 0
    }
    db.insert(james_account)
