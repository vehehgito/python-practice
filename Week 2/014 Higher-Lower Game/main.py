import random

from game_assets import logo_art, vs_art, game_data

def get_random_data():
    """Get random data from the game_data list."""
    return random.choice(game_data)

def format_data(account):
    """Format account into printable format: name, description and country."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}"

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess and returns True if they got it right or False if they got it wrong.""" 
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
def game():
    """Starts the Higher-Lower game."""
    print(logo_art)
    score = 0
    game_should_continue = True
    account_a = get_random_data()
    account_b = get_random_data()
    
    while game_should_continue:
        account_a = account_b
        account_b = get_random_data()
        
        while account_a == account_b:
            account_b = get_random_data()
        
        print(f"Compare A: {format_data(account_a)}")
        print(vs_art)
        print(f"Against B: {format_data(account_b)}")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]

        is_correct = check_answer(guess, a_followers, b_followers)
        
        print("\n" + logo_art)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_should_continue = False

def main():
    """Main function."""
    game()

    play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    
    while play_again == "yes":
        game()
        play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    
    print("Thanks for playing!")

main()