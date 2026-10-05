#Write a Python progran to calculate sum of the first 10 prime numbers
# without using inbuilt methods ?

count = 0
number = 2
total = 0

while count < 10:

    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number)
        total = total + number
        count = count + 1

    number = number + 1

print("Sum =", total)