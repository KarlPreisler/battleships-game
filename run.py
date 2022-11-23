board = []

for x in range(5):
    board.append(["O"] * 5)


def print_board(board):
    """ Function for printing computer and player board """
    for row in board:
        print(" ".join(row))


def start_game():
    """ Starts the game and gets player name """
    print("Welcome to Battleships!")
    player_name = str(input("Enter your name: "))

    print(f"{player_name}'s board: ")


start_game()
print_board(board)