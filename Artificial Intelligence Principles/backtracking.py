#This function checks if its a valid move to insert x number in position
def is_valid_move(grid, row, col, num):
    #check if something is in the same column, row or block
    for x in range(9): #the 9x9 grid
        if grid[row][x] == num:
            return False
        
    for x in range(9):
        if grid[x][col] == num:
            return False
        
    #find the corners
    corner_row = row - row % 3
    corner_col = col - col % 3

    for x in range(3):
        for y in range(3):
            #if we have a number inside that 3x3 field return false
            if grid[corner_row + x][corner_col + y] == num:
                return False
    return True

#The backtracking function
#we pass in row and col to have a recursive call
def solve(grid, row, col):
    #the last column and row value is 8, if it reaches 9 that's the end
    if col == 9:
        if row == 8:
            return True
        #if the row is not equal to 8
        row += 1
        col = 0
    #if we go past the last column, then go to a new row and start with the first column again
    #unless we have reached the end of the grid  
    
    if grid[row][col] > 0:
        #if the cell has a value larger than zero then proceed to the next one
        #with a recursive call
        return solve(grid, row, col+1)
    #all individual responsibilities
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            #assumes this is the solution
            grid[row][col] = num
            if solve(grid, row, col+1):
                return True
            
        #if the move isnt valid then keep the value as 0 for the time being
        grid[row][col] = 0
    return False

#this is a valid sudoku grid, any alteration(wrong or right) can change the outcome

grid =[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

if solve(grid, 0, 0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
else:
    print("This sudoku puzzle is unsolvable.")

