class Account:

def __init__(self, name = "", Account_num=0, balance=0)
    self.name = name
    self.Account_num = Account_num
    self.balance = balance

def deposit(self, amount):
"""Method to make a deposit"""
    print "Deposited amount = " + amount
    self.balance = balance + amount
    return self.balance


def withdraw(self, amount):
"""Method to make a withdrawal"""
    if self.balance < amount:
        print "Insufficient funds"
    else:
        self.balance = balance - amount
        return self.balance

def get_balance(self)
"""Method to allow user to check their balance"""
    return self.balance

def transfer(self, amount, account_num_2transfer)
    if self.balance < amount:
        print "Insufficient funds in your account"
    else:
        else:
        self.balance = balance - amount
        return self.balance    


def main():
    Barbara = Account("Barbara", 5423, 5000000)
    Barbara.withdraw(300)


    Jimbo = Account("", 6532, 68834858)
    Jimbo.deposit(5000)


	
main()
