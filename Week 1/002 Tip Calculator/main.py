bill = float(input("Welcome to the tip calculator!\nWhat was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total = bill * (1 + tip / 100)

each = round(total / people, 2)

print(f"Each person should pay: ${each}")
