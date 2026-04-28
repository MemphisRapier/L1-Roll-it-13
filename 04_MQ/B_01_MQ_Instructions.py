


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

#Main Routine Starts here

print()
print("✖️Welcome to my Math Quiz➗ ")
print()


want_instructions = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if  want_instructions == "yes":
         instructions()

print("program continues")

