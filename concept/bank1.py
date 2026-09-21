class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance = self.balance - amount
        else:
            print("insufficient balance")

    def check_balance(self):
        return self.balance


account = BankAccount()

account.deposit(500)

print(account.check_balance())
account.withdraw(600)
print(account.check_balance())