from data import MENU, resources

TOTAL_MONEY = 0


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def coin_to_usd():
    coins = {}

    denominations = {
        "pennies": 0.01,
        "nickels": 0.05,
        "dimes": 0.10,
        "quarters": 0.25
    }

    coins_value = 0

    for coin_name in denominations:
        coins[coin_name] = int(input(f"How many {coin_name} do you have? "))

    for coin_name, coin_count in coins.items():
        coins_value += coin_count * denominations[coin_name]

    return coins_value


def is_transaction_successful(user_choice):
    """Args: str(). Returns bool(). Calculates the cost of the beverage chosen by the customer."""
    cost = MENU[user_choice]["cost"]
    entered_money = coin_to_usd()

    if entered_money < cost:
        print("\nSorry that's not enough money. Money refunded.")  
        print("A " + user_choice + " costs $" + str(cost) + ". Please try again.")
        return False
    else:
        global TOTAL_MONEY
        TOTAL_MONEY += cost
        change = round(entered_money - cost, 2)
        print(f"Here is ${change} in change.")
        return True


def choice():
    """Makes the customer choose from the 3 beverage options (1, 2, 3)
    and the machine operator from 2 more options which either returns the current resources left in the machine (0),
    or turns off the machine. (-1)"""
    
    user_choice = int(input("""
What would you like to drink today?
1. espresso - $0.5
2. latte - $1.5
3. cappuccino - $2.0
(0 for report and -1 to quit.
   
"""))

    if user_choice == 0:
        for item in resources:
            print(f"{item}: {resources[item]}")
        print(f"Money: ${TOTAL_MONEY}")
    elif user_choice == -1:
        print("Bye bye! Shutting down.")
        exit()
    else:
        user_choice = list(MENU.keys())[user_choice - 1]

        drink = MENU[user_choice]

        if is_resource_sufficient(drink["ingredients"]):
            if is_transaction_successful(user_choice):
                for item in drink["ingredients"]:
                    resources[item] -= drink["ingredients"][item]
                print(f"Here is your {user_choice}. Enjoy!")
        else:
            print("Sorry, we don't have enough resources to make your drink.")


def main():
    choice()
    main()


main()
