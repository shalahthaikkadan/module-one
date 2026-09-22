class BankAccount:

    def __init__(self, name, balance=0):
        self.balance = balance
        self.name = name

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Insufficient balance")

    def check_balance(self):
        return self.balance

    def calculate_interest(self):
        interest = self.balance * 0.02
        return interest


class Savings(BankAccount):

    def __init__(self, name, balance=0):
        super().__init__(name, balance)

    def calculate_interest(self):
        interest = self.balance * 0.03
        return interest
    
    def __private_method(self):
        print("This is a private method")
    

account = BankAccount("Shalah")
account.deposit(500)
print(account.check_balance())
account.withdraw(600)
print(account.check_balance())
print(account.calculate_interest())


account1 = Savings("Shalah", 1000)
print(account1.check_balance())
print(account1.calculate_interest())

account1._Savings__private_method()