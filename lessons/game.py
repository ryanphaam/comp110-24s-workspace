"""Number guessing game."""
from random import randint

SECRET: int = randint(1,10)
correct: bool = False
value: str = "value"

while correct == False: # not correct
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"You got it right! {guess} is the secret number!")
        correct = True
    elif guess > SECRET:
        value = "high"
        print(f"{guess} is too {value}. Try again!")
    else:
        value = "low"
        print(f"{guess} is too {value}. Try again!")