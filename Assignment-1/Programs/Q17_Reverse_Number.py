#Write a function reverse_number(n) that returns the reverse of a number. 

def reverse_number(n):
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    return reverse


number = int(input("Enter a number: "))

result = reverse_number(number)

print("Reverse:", result)