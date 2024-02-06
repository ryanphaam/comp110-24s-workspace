"""EX01 - Simple Battleship - A cute step toward Battleship."""
 
__author__ = "730710909"
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

number_str: str = input("Pick a secret boat location between 1 and 4:")
number = int(number_str)

if (number <= 0):
    print(f"Error! {number} too low!")
    exit()
if (number >= 5):
    print(f"Error! {number} too high!")
    exit()

opponent_str: str = input("Guess a number between 1 and 4:")
opponent = int(opponent_str)
result: str = BLUE_BOX
boat: str = BLUE_BOX * 4

if (opponent == number):
    result = RED_BOX
else:
    result = WHITE_BOX

if (opponent == 1):
    boat = (result + BLUE_BOX + BLUE_BOX + BLUE_BOX)
if (opponent == 2):
    boat = (BLUE_BOX + result + BLUE_BOX + BLUE_BOX)
if (opponent == 3):
    boat = (BLUE_BOX + BLUE_BOX + result + BLUE_BOX)
if (opponent == 4):
    boat = (BLUE_BOX + BLUE_BOX + BLUE_BOX + result)

if (opponent <= 0):
    print(f"Error! {opponent} too low!")
    exit()
if (opponent >= 5):
    print(f"Error! {opponent} too high!")
    exit()

if (opponent == number):
    print(boat + "Correct! You hit the ship.")
else:
    print(boat + "Incorrect! You missed the ship.")