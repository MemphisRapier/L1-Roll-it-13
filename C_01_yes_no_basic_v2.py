
# functions go here

def yes_no(question):
    while True:

        want_instructions = input(question).lower()

        # check the user say yes / no / y / n

        if want_instructions == "yes" or want_instructions == "y" :
            return "yes"
        elif want_instructions == "no" or want_instructions == "n" :
            return "no"
        else:
            print("please enter yes / no")

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

like_cs = yes_no("Do you like computer Science? ")
print(f"You chose {like_cs}")

like_coffe = yes_no("Like coffee? ")
print(f"You said {like_coffe} to coffee")

print("we done")
