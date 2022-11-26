""" This file contains all code to play the battleships game
against the computer in the terminal window
""" 

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
        """ Method to display "X" for coordinates that are already guessed. """
        self.board[ship_row][ship_column] = "X"

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
        """Given a row number, check whether it is a valid row on the board.

        Args:
            row_number: int - The integer value to check.
        Returns:
            bool: Whether the row_number provided is a valid row on the board
        """

        return (ship_row >= 0 and ship_row < self.size)

    def valid_column(self, ship_column):
        return (ship_column >= 0 and ship_column < self.size)

    def point_empty(self, ship_row, ship_column):
    
        if (ship_row, ship_column) in self.guesses:
            return False
        else:
            return True


def random_point(size):
    """
    Helper function to return a random integer between 0 and size
    """
    return randint(0, size - 1)


def validate_guess(board, ship_row, ship_column):
    """
    Validate that players guess has not already been made
    and that it's inside the scope of the board
    """
    
    if (ship_row, ship_column) in board.guesses:
        print("Error: Already guessed, pick new row or col!\n")
    else:
        return True
    
    """
    try:
        board.board[ship_row][ship_column] in board.board

    except IndexError:
        print("Error: Input must be a number between 0-4!")
        return False
    """

# Add Score counting function
# add function for calculating winner


def populate_board(board):
    """
    Function to add ships to board and append to ships list
    """

    ship_row = random_point(board.size)
    ship_column = random_point(board.size)
    board.add_ship(ship_row, ship_column)


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
            if validate_guess(board, ship_row, ship_column):
                board.guesses.append((ship_row, ship_column))
                return ship_row, ship_column

        elif board.type == "player":
            ship_row = input("Guess a row: ")
            ship_column = input("Guess a column: ")
            print("-" * 37)
            if validate_guess(board, ship_row, ship_column):
                board.guesses.append((ship_row, ship_column))
                return ship_row, ship_column


def display_boards(computer_board, player_board):
    """
    Function for printing the player and computer's board
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

        elif computer_board.guess(ship_row, ship_column) == "Miss":
            print(f"{player_board.name} missed the target")

        # Get computer's guess and dislay guess
        ship_row, ship_column = make_guess(computer_board)
        computer_board.guesses.append((ship_row, ship_column))
        print(f"Computer guessed: {ship_row, ship_column}")

        # Define if player got a hit or miss on computer's board
        if player_board.guess(int(ship_row), int(ship_column)) == "Hit":
            print("Computer hit the target!")
        elif player_board.guess(ship_row, ship_column) == "Miss":
            print("Computer missed the target")

        display_boards(computer_board, player_board)


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
    print(f"\nBoard Size is {size}. Number of Ships are {num_ships}")
    print("\nTop left corner is row: 0, col: 0")
    print("-" * 37)
    print("Legend:\n")
    print('"@" = Players ship\n"X" = Already guessed\n"*" = A ship was hit')
    # Get the player's name, validate that user input is a string.
    while True:
        player_name = input('\nEnter your name: ').capitalize()
        if player_name.isalpha() and len(player_name) > 1 < 20:
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


new_game()
