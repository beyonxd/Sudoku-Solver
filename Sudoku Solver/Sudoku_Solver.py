import numpy as np

sudoku = []
print("Please use 0 in place of blank spaces")
for i in range(9):
    row = list(input("Enter the elements of row {} whitout any spaces and commas: ".format(i+1)))   # {} - format specifier
    row = [int(i) for i in row]    # converting string into int.
    sudoku.append(row)
print(np.matrix(sudoku))

def possible(row,col,n):  # This function will return boolean value (True or False)
    global sudoku
    for i in range(0,9):
        if sudoku[row][i] == n:
            return False        # Number is already present in that row of  Sudoku
    for i in range(0,9):
        if sudoku[i][col] == n:
            return False        # Number is already present in that columm or Sudoku
    box_row = (row//3)*3     # Took a variable to check the row in the boxes
    box_col = (col//3)*3     # Took a variable to check the columm in the boxes  
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[box_row+i][box_col+j] == n:
                return False        # Number is already present in that row or columm of particular box
    return True   # Number is not present in that row or columm of particular box
    
def solve():
    for row in range(0,9):
        for col in range(0,9):
            if sudoku[row][col] == 0:
                for n in range(1,10):   # Inserting numbers from 1-9
                    if possible(row,col,n):
                        sudoku[row][col] = n
                        solve()             # Recursion
                        sudoku[row][col] = 0 # Bactracking
                return
    print()
    print("Solved Sudoku:")
    print(np.matrix(sudoku)) 
solve()
