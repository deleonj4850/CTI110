
import random

def generate_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def display_question(num1, num2, operation):
    if operation == 'add':
        print(f"\n  {num1}\n+ {num2}\n")
    elif operation == 'subtract':
        print(f"\n  {num1}\n- {num2}\n")

def math_quiz(operation):
    
    guesses = 0

    num1, num2 = generate_numbers()

    while True:
    
        display_question(num1, num2, operation)

        user_answer = int(input("Enter your answer: "))
 
        if operation == 'add' and user_answer == num1 + num2:
            guesses += 1
            print(f"Congratulations!!! Your answer is correct.\nNumber of guesses: {guesses}")
            break
        else:
            guesses += 1
            if user_answer < num1 + num2:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        if operation == 'subtract' and user_answer == num1 - num2:
            guesses += 1
            print(f"Congratulations!!! Your answer is correct.\nNumber of guesses:")
            break
        else:
            guesses += 1
            if operation == 'subtract':
                if user_answer < num1 - num2:
                    print("Too low! Try again.")
                else:
                    print("Too high! Try again.")

    
    return guesses

def instructions():
    print("Instructions:")
    print("You will be presented with a simple math problem.")
    print("Enter your answer, and the program will provide feedback.")
    print("You can continue guessing until you get the correct answer.")
    print("The program will track the number of guesses.")

def main():
    while True:
        print("\nWelcome to the Math Quiz:")
        print()
        print("MAIN MENU")
        print("-" * 20)
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        
        choice = input("Please choose one of the menu options: ")

        if choice == '1':
            guesses = math_quiz('add')
            print(f"Number of guesses: {guesses}")
        elif choice == '2':
            guesses = math_quiz('subtract')
            print(f"Number of guesses: {guesses}")
        elif choice == '3':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
