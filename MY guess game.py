# My guess game

import random

random_number = random.randint(1, 10)

guess = int(input("Enter your guess number in between 1 to 10 \n"))

print(f"You have guess the number as {guess} ")

for i in range(0, random_number + 10):
    if guess == random_number:
        print("You got it right Congratulations!\n")
        break
    elif int(random_number) > guess:
        print("oops your guess is Wrong! Get higher please\n ")
        guess = int(input("Guess other number \n"))
    else:
        print("oops Your guess is Wrong! Get lower please\n ")
        guess = int(input("Guess other number \n"))
