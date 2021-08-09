class BankAccount:
    NEXT_ACC_NUMBER = 1

    def __init__(self):
        self.cash = 0.0
        BankAccount.NEXT_ACC_NUMBER += 1


    def deposit_cash(self, amount):
        if not isinstance(amount, float) and amount <= 0.0:
            raise ValueError("Deposit can't be negative!")
        self.cash += amount
    
    
    def withdraw_cash(self,amount):
        if amount < 0.0:
            raise ValueError("Withdraw can't be negative")
        self.cash -= min(self.cash, amount)
        
        
    def __str__(self):
        return f'Account: {self.number}, balance: {self.cash}'

print(BankAccount.NEXT_ACC_NUMBER)
myAccount = BankAccount()
print(BankAccount.NEXT_ACC_NUMBER)
myAccount2 = BankAccount()
print(BankAccount.NEXT_ACC_NUMBER)


# myaccount = BankAccount(1496454578)
# print(myaccount)
# myaccount.deposit_cash(429)
# print(myaccount)
# myaccount.deposit_cash(156)
# print(myaccount)
# myaccount.withdraw_cash(1000)
# print(myaccount)
