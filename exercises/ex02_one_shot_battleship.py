"""EX02 - One-shot Battleship - A less cute step toward Battleship."""

__author__ = "730710909"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

grid: int = 4
secret_row: int = 3
secret_column: int = 2
result: str = ""

guess_row: int = int(input("Guess a row: "))  # waiting for player's row guess
while (guess_row > grid or guess_row < 1):  # loop that checks that row guess is within the bounds of grid
    guess_row = int(input(f"The grid is only {grid} by {grid}. Try again: "))  # asks for new guess

guess_column: int = int(input("Guess a column: "))  # does same thing as above but for column
while (guess_column > grid or guess_column < 1):
    guess_column = int(input(f"The grid is only {grid} by {grid}. Try again: "))

if (guess_row == secret_row and guess_column == secret_column):
    result = RED_BOX
else:
    result = WHITE_BOX

counter_row: int = 1  # ounter for the number of rows, later a column counter is used
while counter_row <= grid:  # makes sure that rows dont exceed grid number
    ocean_row_string: str = ""  # storing emojis in this string
    counter_column: int = 1 
    while counter_column <= grid:  # adds a box every loop, adds different colors if guess is right or wrong
        if guess_row == counter_row and guess_column == counter_column:
            ocean_row_string += result
        else:
            ocean_row_string += BLUE_BOX
        counter_column += 1
    print(ocean_row_string)  # prints line of string for one row
    counter_row += 1  # adds 1 to column so that it can reach the grid number as well, then repeats loop

if (guess_row == secret_row and guess_column == secret_column):  # these conditionals check if guess = secret location and prints different phrases depending on that
    print("Hit!")
elif (guess_row != secret_row and guess_column == secret_column):
    print("Close! Correct column, wrong row.")
elif (guess_row == secret_row and guess_column != secret_column):
    print("Close! Correct row, wrong column.")
else:
    print("Miss!")