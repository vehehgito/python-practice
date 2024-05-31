def main():  
    import os

    def add(n1, n2):
        """Takes two numbers and returns the sum."""
        return f"{n1} + {n2} = " + str(n1 + n2)

    def subtract(n1, n2):
        """Takes two numbers and returns the difference."""
        return f"{n1} - {n2} = " + str(n1 - n2)

    def multiply(n1, n2):
        """Takes two numbers and returns the product."""
        return f"{n1} * {n2} = " + str(n1 * n2)

    def divide(n1, n2):
        """Takes two numbers and returns the quotient."""
        return f"{n1} / {n2} = " + str(n1 / n2)

    def modulo(n1, n2):
        """Takes two numbers and returns the remainder."""
        return f"{n1} % {n2} = " + str(n1 % n2)

    status = input("Welcome to the simple calculator. Press any key to continue or press 'q' to quit. ")

    if status == 'q':
        exit()
    else:
        num1 = float(input("What's the first number?: "))
        print("+\n-\n*\n/\n%")
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        
        match operation:
            case '+':
                print(add(num1, num2))
            case '-':
                print(subtract(num1, num2))
            case '*':
                print(multiply(num1, num2))
            case '/':
                print(divide(num1, num2))
            case '%':
                print(modulo(num1, num2))
            case _:
                print("Invalid operation. Please try again.")

        os.system('cls' if os.name == 'nt' else 'clear')
        main()

main()