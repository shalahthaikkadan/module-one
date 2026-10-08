#Write a function check_even_odd(num) that takes a number and prints whether its even or odd. 

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


number = int(input("Enter a number: "))

print(even_or_odd(number))