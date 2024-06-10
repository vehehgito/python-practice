import random

EASY_GUESSES = 10
HARD_GUESSES = 5

def choose_difficulty():
    """Choose the difficulty of the game."""

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_GUESSES
    elif difficulty == "hard":
        return HARD_GUESSES
    else:
        print("Invalid input. Please type 'easy' or 'hard'.")
        choose_difficulty()

def game():
    """Starts the High-Low game."""

    print("Welcome to the High Low Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    guesses = choose_difficulty()

    number = random.randint(1, 100)
    
    while guesses > 0:
        print(f"You have {guesses} guesses remaining.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            return
        elif guess > number:
            print("High")
        else:
            print("Low")
        guesses -= 1
    
    print(f"You ran out of guesses. The answer was {number}.")

def main():
    """Main function."""

    game()
    
    play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    
    while play_again == "yes":
        game()
        play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    
    print("Thanks for playing!")

main()