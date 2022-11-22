battleship_grid = []

for i in range(0,5):
    battleship_grid.append(["."] * 5)


def print_grid(battleship_grid):
    """
    creates battleship grid for game
    """
    for row in battleship_grid:
        print(" ".join(row))

print_grid(battleship_grid)