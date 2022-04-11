# -*- coding: utf-8 -*-
import random

import atm
import account_api

if __name__ == '__main__':
    #card number register
    target_card_number = random.randint(100000000, 999999999)
    target_pin = random.randint(1000, 9999)
    
    card_number = random.randint(100000000, 999999999)
    pin = random.randint(1000, 9999)
    
    api = account_api.AccountAPI()

    print("create account")
    api._createAccount(card_number, pin)
    print(f"my account : {card_number} , pin number : {pin}")
    api._createAccount(target_card_number, target_pin)
    print(f"target account : {target_card_number} , pin number : {target_pin}")
    
    #ATM Card insert
    print("-------------insert Card -----------------")
    atm = atm.ATM(card_number, pin)
    
    print("-------- total user ----------")
    print(atm.API.user())
    
    #See Balance
    print("--------- my balance -----------")
    atm.Balance()
    
    #Deposit
    atm.Deposit(50000)
    
    print("--------- diposit -----------")
    atm.Balance()
    
    #Withdraw
    print("---------------before withdraw----------------")
    print(atm.API.user())
    atm.Withdraw(target_card_number, 50000)
    print("---------------after withdraw----------------")
    print(atm.API.user())

    
