

# checks for an integer more than 0 (allows <enter>)
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

def instruction():
    print('''
    
To begin, choose the number of rounds and either customise
 the game parameters or go with the default game (where the
 secret number will be between 1 and 100).
 
 Then choose how many rounds you;d like to play <enter> for infinite mode.
 
 Your goal is to try to guess the secret number without
 running out of guesses.
 
 Good luck.
 
 ''')

#Main Routine Starts here

# Initialize game variables
mode = "regular"
rounds_played = 0

print()
print("⬆️⬆️⬆️ Welcome to the Higher Lower Game⬇️⬇️⬇️ ")
print()

#loop  for testing purposes

want_instructions = yes_no("Do you want to read the instructions?")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

print("program continues")
