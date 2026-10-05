#Write a Python program that checks whether a given string is a palindrome  or not.

x=(input("Enter the string: "))
if x == x[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")