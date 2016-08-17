class BankAccount(object):
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, cash_deposit):
        self.balance = self.balance + cash_deposit
        return self.balance
    def withdraw(self, cash_withdrawn):
        if cash_withdrawn > self.balance:
            return ("Invalid Transaction")
        else:
            self.balance = self.balance - cash_withdrawn
            return self.balance
            
class MinimunBalanceAccount(BankAccount):
    def __init__(self, balance):
        self.minimum_balance = balance
        
    def getminimumbalance(self):
        return self.minimum_balance

wysla = BankAccount(800)
print (wysla.balance)
wysla.deposit(900)
print (wysla.balance)
print (wysla.withdraw(2000))
print (wysla.balance)

            