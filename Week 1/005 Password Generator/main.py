import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+"

print("Welcome to the Password Generator!")
countLetters = int(input("How many letters would you like in your password?\n"))
countNumbers = int(input("How many numbers would you like?\n"))
countSymbols = int(input("How many symbols would you like?\n"))

password = ""

for i in range(countLetters):
    password += random.choice(letters)

for i in range(countNumbers):
    password += random.choice(numbers)

for i in range(countSymbols):
    password += random.choice(symbols)

password = list(password)
random.shuffle(password)
password = "".join(password)

print(f"Your password is: {password}")