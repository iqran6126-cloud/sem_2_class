class BankAccount:
    def __init__(self):
        self.name=input('enter the name of the acc holder:')
        self.balance=int(input('enter the balance'))
b1=BankAccount()

print(b1.name)
print(b1.balance)