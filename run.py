battleship_grid = []

for i in range(0,5):
    battleship_grid.append(["0"] * 5)

def print_grid(battleship_grid):
    for i in battleship_grid:
        print(" ".join(i))

print_grid(battleship_grid)