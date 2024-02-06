"""EX02 - One-shot Battleship - A less cute step toward Battleship."""

__author__ = "730710909"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

grid: int = 4
secret_row: int = 3
secret_column: int = 2
result: str = ""

guess_row: int = int(input("Guess a row: "))
while guess_row > grid or guess_row < 1:
    guess_row = int(input(f"The grid is only {grid} by {grid}. Try again: "))

guess_column: int = int(input("Guess a column: "))
while guess_column > grid or guess_column < 1:
    guess_column = int(input(f"The grid is only {grid} by {grid}. Try again: "))

if guess_row == secret_row and guess_column == secret_column:
    result = RED_BOX
else:
    result = WHITE_BOX

counter_row: int = 1
while counter_row <= grid:
    ocean: str = ""
    counter_column: int = 1
    while counter_column <= grid:
        if guess_row == counter_row and guess_column == counter_column:
            ocean += result
        else:
            ocean += BLUE_BOX
        counter_column += 1
    print(ocean)
    counter_row += 1

if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
else:
    print("Miss!")
