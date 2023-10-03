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
    two_pos = [row_index, col_index]
    #check if the cell is occupied by '1'
    while [row_index, col_index] == one_pos:
        row_index = random.randint(0, 2)
        col_index = random.randint(0, 2)

    grid[row_index, col_index] = 2

    return two_pos

def set_three(grid, two_pos):
    row_index = random.randint(0, 2)
    col_index = random.randint(0, 2)
    three_pos = [row_index, col_index]
    #check if the cell is occupied by '2'
    while [row_index, col_index] == two_pos:
        row_index = random.randint(0, 2)
        col_index = random.randint(0, 2)

    grid[row_index, col_index] = 3

    return grid

def generate_grid():
    grid = set_grid()
    one_pos = set_one(grid)
    two_pos = set_two(grid)
    set_three(grid, two_pos)

    return grid

grid = generate_grid()
print(grid)

