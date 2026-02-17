
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


# Main routine

like_cs = yes_no("Do you like computer Science? ")
print(f"You chose {like_cs}")

like_coffe = yes_no("Like coffee? ")
print(f"You said {like_coffe} to coffee")

print("we done")
