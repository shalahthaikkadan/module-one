#Write a Python program to take a list of integers and 
#remove all duplicate elements while preserving the original order.

numbers = [1, 2, 3, 2, 4, 1, 5, 3]

result = []

for number in numbers:
    if number not in result:
        result.append(number)

print(result)