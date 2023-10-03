import random

grid = []

for row in range(9):
    for col in range(9):
        grid.append(random.randint(1, 9))
print(len(grid))

