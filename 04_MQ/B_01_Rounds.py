
def int_check(question):

    error = "Please enter an integer that is 1 or more."

    while True:

        response = input(question)

        # Infinite mode
        if response == "":
            return "infinite"

        # Exit code
        if response.lower() == "xxx":
            return "exit"

        try:
            response = int(response)

            # Check number is 1 or higher
            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


def ask_question():

    a = 5
    b = 7
    answer = a + b

    user_input = input(f"What is {a} + {b}? ")

    # exit code if user chickens out
    if user_input.lower() == "xxx":
        return "exit"

    try:
        user_answer = int(user_input)

        if user_answer == answer:
            print("Correct!")
            return None

        else:
            print(f"Wrong! The answer was {answer}")
            return None

    except ValueError:
        print("Invalid input! Please enter a whole number.")
        return None


# Main Routine Starts Here

# Initialise game variables
mode = "regular"
rounds_played = 0

print("➕ Maths Quiz ➕")
print()

# Ask for rounds
num_rounds = int_check(
    "How many rounds would you like?\n"
    " Press <enter> for infinite mode: "
)

# Check for exit
if num_rounds == "exit":
    print("Game exited.")

else:

    # Infinite mode setup
    if num_rounds == "infinite":
        mode = "infinite"
        num_rounds = 5

    # Game loop
    while rounds_played < num_rounds:

        # Round headings
        if mode == "infinite":
            heading = f"\n♾ Round {rounds_played + 1} (Infinite Mode) ♾"

        else:
            heading = f"\n⭐ Round {rounds_played + 1} of {num_rounds} ⭐"

        print(heading)
        print()

        # Ask question
        result = ask_question()

        # Exit game
        if result == "exit":
            break

        rounds_played += 1

        # Extend infinite mode
        if mode == "infinite":
            num_rounds += 1

    print("\nGame Over")