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
    print("Roll the dice and try to win!.")
    print()

def int_check():
    """Checks users enter an integer more than /  equal to 13"""

    error = "Please enter an integer more than /  equal to 13. "
    while True:
        try:
             response = int(input("What is the game goal? "))


             if response < 13:
               print(error)
             else:
                 return response


        except ValueError:
              print(error)


# Main routine

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()



print()
game_goal =int_check()
print (game_goal)
