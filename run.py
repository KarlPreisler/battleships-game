"""
This file contains all code to play the battleships game
against the computer in the terminal window.
"""
import sys
from random import randint

scores = {"computer": 0, "player": 0}
# Create scores dictionary


# Basic structure imported and modified from CI PP3 Sample project.
class Board:
    """
    Main board class. Sets board size, the number of ships,
    the player's name and the board type (player board or computer).
    Has methods for adding ships and guesses and printing the board

    Attributes:
    size = an integer representing the size of the board
    num_ships = an integer representing the number of ships that
    will be created
    name = takes string input from player or assigns computer name =
    "computer"
    type = a string indicating whether the type of player is computer or
    player
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [
            ["." for ship_row in range(size)] for ship_column in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        """ Method for printing board with blank spaces """
        for row in self.board:
            print("  ".join(row))

    def guess(self, ship_row, ship_column):
        """
        Method to display "X" for coordinates that are already guessed.
        If user guess is not a number between 0-4 it will display that the user
        completely missed the grid.
        """
        # Will display message to user if IndexError occurs
        try:
            self.board[ship_row][ship_column] = "X"
        except IndexError:
            print("Your shot is way off! Next time choose number between 0-4")

        # Display "*" if target is hit
        if (ship_row, ship_column) in self.ships:
            self.board[ship_row][ship_column] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, ship_row, ship_column, type="computer"):
        """
        Method for adding ships to player and computer board
        Mark ships as "@" on player board and hiding ships on computer board
        """
        self.ships.append((ship_row, ship_column))
        if self.type == "player":
            self.board[ship_row][ship_column] = "@"

    def valid_row(self, ship_row):
        """ Method for checking if given row number is a valid row
        on the board. Validate that the users guess for row
        is an integer.
        """
        try:
            (int(ship_row) >= 0 and int(ship_row) < 5)
        except IndexError:
            return False
        except ValueError:
            return False
        return True

    def valid_column(self, ship_column):
        """ Method for checking if given column number is a valid column
        on the board. Validate that the users guess for column
        is an integer.
        """
        try:
            (int(ship_column) >= 0 and int(ship_column) < 5)
        # Return false if value or index error is raised
        except IndexError:
            return False
        except ValueError:
            return False
        return True

    def point_empty(self, ship_row, ship_column):
        """
        Given a column and row guess, check if already guessed before
        """
        if (ship_row, ship_column) in self.guesses:
            return False
        return True


def random_point(size):
    """
    Helper function to return a random integer between 0 and size
    """
    return randint(0, size - 1)


def count_scores(scores, player_board, computer_board):
    """ Function to check if all ships are hit on a board
    and display who is the winner, if both player and computer
    hit last ship in the same round it will display that its a draw
    """
    # Checks if player and computer lost their last ship in same round
    if scores["player"] == computer_board.num_ships and \
       scores["computer"] == player_board.num_ships:
        print("It's a draw! Both teams lost all ships.")
        # Start a new game once winner is dislayed
        new_game()
    elif scores["player"] == computer_board.num_ships:
        print("You are the winner! All enemy ships are hit.")
        new_game()
    elif scores["computer"] == player_board.num_ships:
        print("You lost! All your ships are hit.\n")
        print("-" * 37)
        new_game()


def populate_board(board):
    """
    Function to add ships to board and append to ships list
    """

    ship_row = random_point(board.size)
    ship_column = random_point(board.size)
    board.add_ship(ship_row, ship_column)


def display_scores(player_board):
    """ Prints the scores after each round """
    print("The scores are\n")
    print(f"{player_board.name}: {scores['player']} Computer: \
{scores['computer']}")
    print("-" * 37)


def make_guess(board):
    """
    Function to get user guess and append it to guesses list,
    if computer guess, pick random coordinates and
    append to guess list
    """
    while True:
        if board.type == "computer":
            ship_row, ship_column = random_point(
                board.size), random_point(board.size)

            if board.point_empty(ship_row, ship_column):
                board.guesses.append((ship_row, ship_column))
                return ship_row, ship_column

        elif board.type == "player":
            ship_row = input("Guess a row: ")
            ship_column = input("Guess a column: ")
            print("-" * 37)

            if (not board.valid_row(ship_row)
                    or not board.valid_column(ship_column)):
                print("Error: No letters allowed! Enter a number between 0-4")

            elif board.point_empty(ship_row, ship_column):
                board.guesses.append((ship_row, ship_column))
                return ship_row, ship_column
            else:
                print("Error: Already guessed, pick new row or col!\n")


def display_boards(computer_board, player_board):
    """
    Function for printing boards in the terminal
    """
    print(f"\n{player_board.name}'s Board:")
    player_board.print()
    print("\nComputer's Board:")
    computer_board.print()
    print()
    print("-" * 37)


def play_game(computer_board, player_board):
    """
    Function for starting the game and controlling game logic.
    Appends guesses to player and computer board and checks
    if a guess is the same location as a ship, displaying
    hit or miss message depending on result.
    """

    while True:
        ship_row, ship_column = make_guess(player_board)
        ship_row, ship_column = int(ship_row), int(ship_column)
        # append players guess to board and display guess
        player_board.guesses.append((ship_row, ship_column))
        print(f"{player_board.name} guessed: {ship_row, ship_column}")

        # Define if computer got a hit or miss on player's board
        if computer_board.guess(ship_row, ship_column) == "Hit":
            print(f"{player_board.name} hit the target!")
            scores["player"] += 1
        elif computer_board.guess(ship_row, ship_column) == "Miss":
            print(f"{player_board.name} missed the target")

        # Get computer's guess and dislay guess
        ship_row, ship_column = make_guess(computer_board)
        computer_board.guesses.append((ship_row, ship_column))
        print(f"Computer guessed: {ship_row, ship_column}")

        # Define if player got a hit or miss on computer's board
        if player_board.guess(int(ship_row), int(ship_column)) == "Hit":
            print("Computer hit the target!")
            scores["computer"] += 1
        elif player_board.guess(ship_row, ship_column) == "Miss":
            print("Computer missed the target")

        display_boards(computer_board, player_board)
        display_scores(player_board)
        count_scores(scores, player_board, computer_board)

        # Provide player with option to restart or quit after each round
        resume_option = input('Press "Q" to quit the game, "R" to restart \
the game or "Enter" to continue to the next round\n')
        print("-" * 37)
        if resume_option.upper() == "Q":
            sys.exit("You quit the game")
        elif resume_option.upper() == "R":
            new_game()


def new_game():
    """
    Starts a new game. Set scores to 0
    Sets the board size and number of ships
    prints welcome message and asks for player name
    validates that name is string and initializes boards
    for computer and player.
    """
    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("\nWelcome to the Battleship Game!")
    print(f"\nBoard Size is {size}. Number of ships are {num_ships}")
    print("\nThe top left corner is row: 0, column: 0")
    print("-" * 37)
    print("Legend:\n")
    print('"@" = Players ship\n"X" = Already guessed\n"*" = A ship was hit')
    # Ask for users name, validate that input is a string between 1-20 letters.
    while True:
        player_name = input('\nEnter your name: ').capitalize()
        if player_name.isalpha() and len(player_name) >= 1 < 21:
            break
        else:
            print("Error: Please provide a valid name")
            print("Provide any alphabetical combination between 1-20")

    # Creates class instances for computer and player
    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    # Populates boards and adds ships, calls function for printing boards
    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)
    display_boards(computer_board, player_board)
    play_game(computer_board, player_board)


if __name__ == "__main__":
    new_game()

