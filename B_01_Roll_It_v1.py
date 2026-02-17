# functions go here

def yes_no(question):
    """Ask a yes/no question and return 'yes' or 'no'."""
    while True:
        response = input(question).strip().lower()

        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please answer yes or no.")


def instructions():
    """Display program instructions."""
    print()
    print("**** Instructions ****")
    print("This program demonstrates how to use functions.")
    print("You will be asked if you want to see the instructions.")
    print("Answer with yes or no.")
    print()


# Main routine

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
print("Program continues")

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
print("Program continues")

game_goal =int_check()
print (game_goal)
