import random


def ask_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    answer = a + b

    user_answer = int(input(f"What is {a} + {b}? "))

    if user_answer == answer:
        print("Correct!")
    else:
        print(f"Wrong! The answer was {answer}")



