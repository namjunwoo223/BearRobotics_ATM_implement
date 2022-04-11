# -*- coding: utf-8 -*-
import account_api

class ATM:
    def __init__(self, card_number, PIN):
        self.API = account_api.AccountAPI()
        self.isVerify = self.API.isPINok(card_number, PIN)
        
        if self.isVerify:
            self.card_number = card_number
            self.PIN = PIN
            print("PIN Number is Collect!")
        else:
            assert False, "The PIN number is incorrect. Please check your PIN number"

    #See Balance/Deposit/Withdraw
    def Balance(self):
        self.balance = self.API.transaction("0", self.card_number)
        return print(f"Balance : {self.balance}")
    
    def Deposit(self, amount):
        return self.API.transaction("1", self.card_number, amount)
    
    def Withdraw(self, target_card_number, amount):
        return self.API.transaction("2", self.card_number, target_card_number, amount)
    