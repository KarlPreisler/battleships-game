from random import randint

battleship_grid = []

for i in range(0,5):
    battleship_grid.append(["."] * 5)


def print_grid(battleship_grid):
    """
    creates battleship grid for game
    """
    for row in battleship_grid:
        print(" ".join(row))


def random_row(battleship_grid):
    return randint(0, len(battleship_grid)-1)


def random_col(battleship_grid):
    return randint(0, len(battleship_grid)-1)


print(random_row(battleship_grid))
print(random_col(battleship_grid))
