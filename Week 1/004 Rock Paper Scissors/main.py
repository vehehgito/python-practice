import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = input("Welcome to Rock, Paper, Scissors!\nType '0' for rock, '1' for paper, or '2' for scissors to play: ")

print("You chose:")
match choice:
    case "0":
        print(rock)
    case "1":
        print(paper)
    case "2":
        print(scissors)
    case _:
        print("Invalid choice. Please try again.")
        exit()

print("Computer chose:")
computer_choice = str(random.randint(0,2))
match computer_choice:
    case "0":
        print(rock)
    case "1":
        print(paper)
    case "2":
        print(scissors)

if choice == "0" and computer_choice == "2":
    print("You win!")
elif choice == "1" and computer_choice == "0":
    print("You win!")
elif choice == "2" and computer_choice == "1":
    print("You win!")
elif choice == computer_choice:
    print("It's a draw!")
else:
    print("You lose!")

