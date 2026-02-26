class BankAccount:
    def __init__(self,n,b):
        self.name=n
        self.balance=b
    def deposit(self,amt):
        if amt>0:
            self.balance+=amt
            return self.balance
        return 'invalid amount'

n=input('enter the name of the acc holder:')
b=int(input('enter the balance'))
b1=BankAccount(n,b)
print(b1.name)
print(b1.balance)