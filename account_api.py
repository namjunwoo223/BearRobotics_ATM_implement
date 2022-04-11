# -*- coding: utf-8 -*-
import os
import pandas as pd

class AccountAPI:
    def __init__(self):
        self.loadAccountData()
        #print(self.__user)
        print("init data")
        
    def _createAccount(self, card_number, input_PIN):
        user_total_number = self.__user["number"].tolist()

        assert int(card_number) not in user_total_number, "The account number already exists. Please set it to a different number."
        new_data = {'number': [card_number], 'PIN': [input_PIN], 'balance': [0]}
        self.__user = pd.concat([self.__user, pd.DataFrame(new_data)])
        self.__user.to_csv("database.csv", index = None)
        
        self.loadAccountData()
        
    def loadAccountData(self):
        if os.path.isfile("database.csv"):
            self.__user = pd.read_csv("database.csv")
        else:
            data = pd.DataFrame(columns=["number", "PIN", "balance"], )
            data.to_csv("database.csv", index = None)
            self.__user = pd.read_csv("database.csv")
                
    def isPINok(self, card_number, PIN):
        user_data = self.__user[self.__user["number"] == int(card_number)]
        return int(PIN) == user_data["PIN"].values[0]
    
    def transaction(self, tasks, *args):
        if tasks == "0" : #see balance
            trg_index = self.__user[self.__user["number"] == int(args[0])].index.values[0]
            return self.__user.iloc[trg_index]["balance"]
            
        if tasks == "1": # Deposit
            trg_index = self.__user[self.__user["number"] == int(args[0])].index.values[0]
            self.__user.iloc[trg_index]["balance"] += args[1]
            self.__user.to_csv("database.csv", index = None)
            self.loadAccountData()
            

        elif tasks == "2": #Withdraw
            req_user_index = self.__user[self.__user["number"] == int(args[0])].index.values[0]
            
            user_total_number = self.__user["number"].tolist()
            assert int(args[1]) in user_total_number, "Account number does not exist. Please check again."
            
            trg_user_index = self.__user[self.__user["number"] == int(args[1])].index.values[0]

            req_user = self.__user.iloc[req_user_index]
            assert req_user["balance"] - args[2] >= 0, "Your account balance is low."
            
            trg_user = self.__user.iloc[trg_user_index]
            
            trg_user["balance"] += args[2]
            req_user["balance"] -= args[2]

            self.__user.to_csv("database.csv", index = None)
            self.loadAccountData()
            
    #for debug
    #If you want to use this software, annotate this function
    def user(self):
        return self.__user
