#!/usr/bin/env python
# coding: utf-8

# In[5]:


class BankAccount:
    _amount = 0
    _notfreezedAcount = True
    def __init__(self, amount):
        self.amount = amount
    
    def withdraw(self, amount):
        if (amount <= -1):
            amount = amount * -1
        if(self._notfreezedAcount):
            if (self.amount - amount > -1000):
                self.amount -= amount
            elif(self.amount - amount <= -1000):
                self.amount = -1000
                self.freezeAccount()
        else:
            print("Your account is frozen")
    
    def deposit(self, amount):
        if (amount <= -1):
            amount = amount * -1
        if(self._notfreezedAcount):
            self.amount += amount
        
    
    def freezeAccount(self):
        print("Your account is frozen")
        self._notfreezedAccount = False
    
    def showBankBalance(self):
        print("Your Credit: %s" %(self.amount))


# In[6]:


exit = "false"
choice = 0
account = BankAccount(2000)
while(exit != "true"):
    account.showBankBalance()
    print("If you want to deposit write '1' if you want to whitdraw write '0'")
    choice = int(input())
    if choice == 1:
        account.deposit(int(input("Input your deposit: ")))
    else :
        account.withdraw(int(input("Input your withdraw: ")))
    
    exit = input("If you want to exit write 'true' ")
    
    
    
    
    

