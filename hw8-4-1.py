# Author RTS 12/9/21

import random

num = random.randint(0, 50)

while True:
    number = input("Guess a number from 0-50. ")
    if number == "stop":
        print("The random number was " + str(num))
        break
    if int(number) > num:
        print("Guess lower")
        continue
    elif int(number) < num:
        print("Guess higher")
        continue
    elif int(number) == num:
        print("You guessed the correct number!")
        break
