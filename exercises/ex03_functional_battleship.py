"""EX03 - Functional Battleship - The least cute step toward Battleship."""

__author__ = "730710909"

import random


def input_guess(grid: int, row_column: str) -> int:
    """User input function to allow user to put in guesses."""
    assert row_column == "row" or row_column == "column"
    guess: int = int(input(f"Guess a {row_column}: "))  # waiting for player's row guess
    while (guess > grid or guess < 1):  # loop that checks that row guess is within the bounds of grid
        guess = int(input(f"The grid is only {grid} by {grid}. Try again: "))  # asks for new guess
    return guess


def print_grid(grid: int, guess_row: int, guess_column: int, correctness: bool) -> None:
    """Grid function produce grid string."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    result: str = ""
    if (correctness is True):
        result = RED_BOX
    else:
        result = WHITE_BOX
    counter_row: int = 1  # counter for the number of rows, later a column counter is used
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


def correct_guess(secret_row: int, secret_column: int, guess_row: int, guess_column: int) -> bool:
    """Function to see if guess is correct."""
    if (secret_row == guess_row and secret_column == guess_column):
        return True
    else:
        return False
    

def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Main function to run Battleship game."""
    turns_allowed: int = 5  # define initial game state variables
    current_turn: int = 1

    while current_turn <= turns_allowed:  # print current turn number
        print(f"=== Turn {current_turn}/{turns_allowed} ===")  # prompt user for row and column guesses
        guess_row = input_guess(grid_size, "row")
        guess_column = input_guess(grid_size, "column")
        correct = correct_guess(secret_row, secret_column, guess_row, guess_column)  # verify user's guess
        print_grid(grid_size, guess_row, guess_column, correct)  # codify the emoji results of user's guess
        if correct:  # check if user's guess is correct
            print(f"Hit! You won in {current_turn}/{turns_allowed} turns!")
            current_turn = turns_allowed + 1  # end game if user wins
        else:
            print("Miss!")  # continue to the next turn
            current_turn += 1
            if (current_turn > turns_allowed):  # checks if user has used up all turns
                print(f"X/{turns_allowed} - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))