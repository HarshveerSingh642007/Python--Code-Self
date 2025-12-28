#Number Guessing Game
import random

number = random.randint(1, 10)
guess = int(input("Guess number 1-10: "))

if guess == number:
    print("Correct! You win!")
else:
    print("Wrong. Number was", number)

input("Press Enter...")
