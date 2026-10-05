#Create an abstract class Payment with abstract methods 
# make_payment() and payment_status(). Implement two concrete 
# classes CreditCardPayment and UPIPayment. Write a program where the 
# user chooses the payment method and the respective class handles the process.

from abc import ABC,abstractmethod

class Payment(ABC):
    
    @abstractmethod
    def make_payment(self):
        pass

    @abstractmethod
    def payment_status(self):
        pass

class CreditCardPayment(Payment):

    def make_payment(self):
        print("payment made by creadit card")

    def payment_status(self):
        print("payment transcation is done")

class UpiPayment(Payment):
    def make_payment(self):
        print("payment made by upi")
    def payment_status(self):
        print("payment transcation is done by upi")

paymentmethod=input("Enter a payment:1(1.CreditCardPayment 2.UpiPayment):")

if paymentmethod == "1":
    payment = CreditCardPayment()
    payment.make_payment()
    payment.payment_status()

elif paymentmethod == "2":
    payment = UpiPayment()
    payment.make_payment()
    payment.payment_status()

else:
    print("invalid payment method")



