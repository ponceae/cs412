"""Coding Homework 2: Recursive Grid Tiling.

    Recursive algorithm that fills a 2^n X 2^n
    grid with L's where initially a grid[n] slot
    is missing. 

    Name:  
        Adrien Ponce
    Honor Code and Acknowledgments: 
        This code complies with the JMU Honor Code.
        Help for initializing and declaring a Python 
        2D array taken from StackOverflow. 
        https://stackoverflow.com/questions/19044174/
        declaring-and-populating-2d-array-in-python
"""


def fill_grid(grid, missing, n, start, end, curr):
    # coordinates of missing cell
    x = missing[0]
    y = missing[1]
    # row and column bounds of sub-grid (2^n-1)
    row = (start + n // 2) 
    col = (end + n // 2) 
    # base case (smallest sub-grid can be)
    if n == 2:   
        curr += 1
        # iterate through sub-grid
        for i in range(row + 1):
            for j in range(col + 1):
                # cell open, insert tile
                if grid[i][j] is None:
                    grid[i][j] = curr
        return curr


    """Before splitting, we need to make sure each 
    sub-grid has a missing cell. In each block, we 
    need to store the missing coordinates so that the 
    base case knows which values are missing."""
    # missing cell in top left
    if (x < row and y < col):
        # add a missing cell to all
        # but top left 
        curr += 1
        TL = missing
        grid[row][col] = curr           # BR
        BR = (row, col)
        grid[row - 1][col] = curr       # TR
        TR = (row - 1, col)
        grid[row][col - 1] = curr       # BL
        BL = (row, col - 1)
    # missing cell in top right
    elif (x < row and y >= col):
        # add a missing cell to all
        # but top left 
        curr += 1
        TR = missing
        grid[row][col] = curr           # BR
        BR = (row, col)
        grid[row][col - 1] = curr       # BL
        BL = (row, col - 1)
        grid[row - 1][col - 1] = curr   # TL
        TL = (row - 1, col - 1)
    # missing cell in bottom left
    elif (x >= row and y < col):
        # add a missing cell to all
        # but bottom left 
        curr += 1
        BL = missing
        grid[row][col] = curr           # BR
        BR = (row, col)
        grid[row - 1][col] = curr       # TR
        TR = (row - 1, col)
        grid[row - 1][col - 1] = curr   # TL
        TL = (row - 1, col - 1)
    # missing cell in bottom right
    elif (x >= row and y >= col):
        # add a missing cell to all
        # but bottom right 
        curr += 1
        BR = missing
        grid[row - 1][col] = curr       # TR
        TR = (row - 1, col)
        grid[row][col - 1] = curr       # BL
        BL = (row, col - 1)
        grid[row - 1][col - 1] = curr   # TL
        TL = (row - 1, col - 1)
        
    """Now, we can recursively call each subgrid
    and fill it accordingly."""
    # fill top left sub-grid
    curr = fill_grid(grid, TL, n // 2, start, end, curr)        
    # fill top right sub-grid             
    curr = fill_grid(grid, TR, n // 2, start, end + n // 2, curr)   
    # fill bottom left sub-grid           
    curr = fill_grid(grid, BL, n // 2, start + n // 2, end, curr)   
    # fill bottom right sub-grid          
    curr = fill_grid(grid, BR, n // 2, start + n // 2, end + n // 2, curr)      
    # returns the current tile count 
    return curr     


def main():
    # grid size (2^n)
    n = pow(2, int(input()))
    # initial missing cell location
    coord = input().split()
    missing = (int(coord[0]), int(coord[1]))
    # build matrix
    grid = [[None for _ in range(n)] for _ in range(n)]
    # remove initial cell
    grid[missing[0]][missing[1]] = -1
    fill_grid(grid, missing, n, 0, 0, -1) 
    # output formatting
    for i in range(n):
        for j in range(n):
            if j != n-1:
                print("{:02d}".format(grid[i][j]), end=" ")
            else:
                print("{:02d}".format(grid[i][j]))
          

if __name__ == "__main__":
    main()
