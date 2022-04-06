class bankaccount(object):
    def __init__(self,name,balance,acnumber):
        self.name = name
        self.balance = balance
        self.acnumber = acnumber
        print ("\n\nCongratualtions! your account is created\n\nAccount Name:",self.name,"\n\nAccount Number:",self.acnumber," \n\nCurrent Balance:",self.balance)
    
    def withdraw(self, wamount):
        if self.balance < wamount:
            print ("You have low balance!\nYour current balance is:%s"%(self.balance))
        elif wamount + self.balance == 0:
            print ("Your account had 0 balance")
        elif wamount == 0:
            print ("Enter amount between 1 to %s"%(self.balance))
        else:
            self.balance -= wamount
            print ("Withdrawn Rs.",wamount,"\nYour current balance is :",self.balance)
            
    def deposite(self,damount):
            print ("Your previous balance is:", self.balance)
            print ("Deposite amount: %s" %(damount))
            self.balance += damount
            print ("Your current balance is:", self.balance)
import random
name=input("Enter a account name:")
acno=random.randint(1,5000000)
bal=int(input("Enter the initial deposite amount:"))

ac1 = bankaccount(name,bal,acno)