#Write a function is_palindrome(word) that returns True if the word is palindrome. 


x=(input("Enter the string: "))
if x == x[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")