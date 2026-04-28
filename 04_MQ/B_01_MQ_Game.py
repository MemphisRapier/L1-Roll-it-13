# checks if users enter yes (y) or no (n)
def yes_no(question):
    while True:

        want_instructions = input(question).lower()

        if want_instructions == "yes" or want_instructions == "y":
            return "yes"
        elif want_instructions == "no" or want_instructions == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    print(''' 

    There will math questions displayed on this quiz
    all on basic facts. 

    These could be simple basic facts like: Multiplication,
    Division, Addition, Subtraction.

     Take in mind that none of these questions will have
      a negative number so don't worry 🙂🙂 ''')


# Main Routine Starts here

print()
print("✖️Welcome to my Math Quiz➗ ")
print()

want_instructions = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

def string_checker(question, valid_ans):
    """Checks user enters a valid answer (full word or first letter)"""

    error = f"Please choose from {valid_ans}"

    while True:
        response = input(question).lower()

        for item in valid_ans:
            if response == item or response == item[0]:
                return item

        print(error)
        print()


def check_answer(num1, num2, question):
    """Asks math question and checks answer"""

    symbols = {
        "addition": "+",
        "subtraction": "-",
        "multiplication": "*",
        "division": "/"
    }

    # Work out correct answer
    if question == "addition":
        correct = num1 + num2
    elif question == "subtraction":
        correct = num1 - num2
    elif question == "multiplication":
        correct = num1 * num2
    elif question == "division":
        if num2 == 0:
            print("Cannot divide by zero")
            return
        correct = num1 / num2

    # Ask question
    user_input = input(f"What is {num1} {symbols[question]} {num2}? ")

    # Check answer
    try:
        if float(user_input) == correct:
            print("Correct!")
        else:
            print(f"Wrong! The answer was {correct}")
    except ValueError:
        print("Please enter a number.")


# Main program

valid_operations = ("addition", "subtraction", "multiplication", "division")

num1 = 10
num2 = 5

function = string_checker(
    "Choose: Addition (a), Subtraction (s), Multiplication (m), Division (d): ",
    valid_operations
)

check_answer(num1, num2, function)

