# Maths Quiz Game


# Checks if user enters yes or no
def yes_no(question):

    while True:

        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes / no")
            print()


# Displays instructions
def instructions():

    print('''

    📘 Instructions 📘

    This is a basic maths quiz game.

    You will answer questions involving:
    ➕ Addition
    ➖ Subtraction
    ✖ Multiplication
    ➗ Division

    • Type 'xxx' anytime to quit
    • Press <enter> for infinite mode

    Good luck 🙂
    ''')


# Checks user enters valid rounds
def int_check(question):

    error = "Please enter an integer that is 1 or more."

    while True:

        response = input(question)

        if response == "":
            return "infinite"

        if response.lower() == "xxx":
            return "exit"

        try:
            response = int(response)

            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)



# Asks random maths question
import random
def ask_question():

    # Random numbers
    a = random.randint(1, 20)
    b = random.randint(1, 20)

    # Random operator
    operator = random.choice(["+", "-", "*", "/"])

    # Addition
    if operator == "+":
        answer = a + b

    # Subtraction
    elif operator == "-":
        answer = a - b

    # Multiplication
    elif operator == "*":
        answer = a * b

    # Division
    else:

        # Makes division answers whole numbers
        answer = a
        b = random.randint(1, 10)
        a = answer * b

        answer = a // b

    # Ask question
    user_input = input(f"What is {a} {operator} {b}? ")

    # Exit code
    if user_input.lower() == "xxx":
        return "exit"

    try:
        user_answer = int(user_input)

        if user_answer == answer:
            print("✅ Correct!")

        else:
            print(f"❌ Wrong! The answer was {answer}")

    except ValueError:
        print("Please enter a whole number.")


# Main Routine

mode = "regular"
rounds_played = 0

print("➕ Welcome to the Maths Quiz ➕")
print()

want_instructions = yes_no(
    "Do you want to read the instructions? "
)

if want_instructions == "yes":
    instructions()

print()

num_rounds = int_check(
    "How many rounds would you like?\n"
    "Press <enter> for infinite mode: "
)

if num_rounds == "exit":

    print("\nGame exited.")

else:

    if num_rounds == "infinite":
        mode = "infinite"
        num_rounds = 5

    while rounds_played < num_rounds:

        if mode == "infinite":
            heading = (
                f"\n♾ Round {rounds_played + 1} "
                f"(Infinite Mode) ♾"
            )

        else:
            heading = (
                f"\n⭐ Round {rounds_played + 1} "
                f"of {num_rounds} ⭐"
            )

        print(heading)
        print()

        result = ask_question()

        if result == "exit":
            break

        rounds_played += 1

        if mode == "infinite":
            num_rounds += 1

    print("\n🏁 Game Over 🏁")