import random
import numpy as np

grid = []
row = []
col = []

def set_grid():

    height = 9
    width = 9

    grid = np.zeros((height, width), dtype = int)

    return grid

#set 1 in a random position, then modify the method to
#generate 1 in a different row and col of the initial random position
def set_one(grid):

    row_index = random.randint(0, 2)
    col_index = random.randint(0, 2)
    one_pos = [row_index, col_index]

    '''
    Search the grid for values of 0
    row_indice, col_indice = np.where(grid == 0)

    if len(row_indice) == 0:
        return grid
    '''

    grid[row_index, col_index] = 1

    #return the row and col position of 1
    return one_pos

def set_two(grid, one_pos):
    row_index = random.randint(0, 2)
    col_index = random.randint(0, 2)

    while [row_index, col_index] == one_pos:
        row_index = random.randint(0, 2)
        col_index = random.randint(0, 2)

    grid[row_index, col_index] = 2

    return grid

grid = set_grid()
def generate_grid():
    set_one(grid)
    set_two(grid)

generate_grid()

