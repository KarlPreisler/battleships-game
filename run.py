from random import randint
 
scores = {"computer": 0, "player": 0}
 

class Board:
    """
    Main board class. set board size, the number of ships,
    The players name and the board type (player board or computer board)
    Has methods for adding ships and guesses and printing the board
    """
 
    def __init__(self, size, num_ships, name, type):
        self.size = size
 
        # Initializes grid in one line
        self.board = [["." for x in range(size)] for y in range(size)]
       
        self.num_ships = num_ships
        self.name = name
        self.type = type
 
        # Stores guesses against board.
        self.guesses = []
       
        # Stores coordinates for ships on the board.
        self.ships = []
       
 
    def print(self):
        for row in self.board:
            print(" ".join(row))
 
    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"
        # "X" Indicates guesses
 
        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"
        # "*" indicates a hit
 
    def add_ships(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: your cannot add any more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"
                # "@" indicates player ships
 
 
def random_point(size):
    """
    Helper function to return a random integer between 0 and size
    returns random integer between 0-4.
    """
    return randint(0, size - 1)
 
 
def populate_board(board):
    """
    Populates board for round
    """
    print(Board)
    
   
def play_game(computer_board, player_board):
    print("Guess a row: ")
    
 

def make_guess(board):
    """
    Processes the guesses
    if its a computer guess it does same thing as populating board,
    picking a random row and column for ships.
    if player guess it promts for input
    """
 

def new_game():
    """
    Starts a new game. Sets board size and number of ships, resets the
    scores and initialises the boards.
    """
    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 35)
    player_name = input("Please enter your name: ")
 
    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")
    # Creates two class instances for computer & player
 
    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)
        # runs number of ships(4) which populates board for player and comp
    
    play_game(computer_board, player_board)
 

new_game()
