# Write a program to generate the first n Fibonacci numbers
# and print their sum.

n = int(input("Enter the number of terms: "))

a = 0
b = 1
total = 0

print("Fibonacci numbers:")

for i in range(n):
    print(a, end=" ")

    total = total + a

    a, b = b, a + b

print("\nSum of Fibonacci numbers:", total)