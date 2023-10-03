import random
import numpy as np

grid = []
row = []
col = []

def generate_grid():

    height = 9
    width = 9

    grid = np.zeros((height, width), dtype = int)

    return grid

#set 1 in a random position, then modify the method to
#generate 1 in a different row and col of the initial random position
def set_ones(grid):
    row_index = random.randint(0, 2)
    col_index = random.randint(0, 3)

    grid[row_index, col_index] = 1

    print(grid)

grid = generate_grid()
set_ones(grid)
