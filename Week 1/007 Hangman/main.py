import random

words = ["ultrakill", "yakuza", "terraria", "minecraft", "fallout", "skyrim", "portal", "bioshock", "dota", "csgo"]

word = random.choice(words)

blanks = "_" * len(word)

guesses = 6

print("Welcome to Hangman! Video Game Edition")
print("Here is your word: " + blanks)

def hangman_ascii(guesses):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]

    return stages[guesses]

while guesses > 0:
    print("You have " + str(guesses) + " guesses left.")

    print(hangman_ascii(guesses))

    letter = input("Guess a letter: ")

    if letter in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == letter:
                blanks = blanks[:i] + letter + blanks[i + 1:]
        print(blanks)
    else:
        print("Incorrect!")
        guesses -= 1

    if blanks == word:
        print("Congratulations! You win!")
        break

if guesses == 0:
    print("You lose! The word was: " + word)