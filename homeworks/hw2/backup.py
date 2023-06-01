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
# keep track of current tile count
curr = -1


def fill_grid(grid, x, y, n):
    global curr
    # base case (smallest sub-grid can be)
    if n == 2:
        # update current tile count
        curr += 1
        for i in range(n):
            for j in range(n):
                # location for part of L-shape
                # open cell, insert tile 
                if (grid[i + x][j + y] is None):
                    grid[i + x][j + y] = curr
        return

    mid = n // 2
    # missing cell in top left
    if (x < mid and y < mid):
        # fill all center cells but top left 
        curr += 1
        grid[mid][mid] = curr           # BR
        grid[mid - 1][mid] = curr       # TR
        grid[mid][mid - 1] = curr       # BL
    # missing cell in top right
    elif (x < mid and y >= mid):
        # fill all center cells but top right
        curr += 1
        grid[mid][mid] = curr           # BR
        grid[mid][mid - 1] = curr       # BL
        grid[mid - 1][mid - 1] = curr   # TL
    # missing cell in bottom left
    elif (x >= mid and y < mid):
        # fill all center cells but bottom left
        curr += 1
        grid[mid][mid] = curr           # BR
        grid[mid - 1][mid] = curr       # TR
        grid[mid - 1][mid - 1] = curr   # TL
    # missing cell in bottom right
    elif (x >= mid and y >= mid):
        # fill all center cells but bottom right
        curr += 1
        grid[mid - 1][mid] = curr       # TR
        grid[mid][mid - 1] = curr       # BL
        grid[mid - 1][mid - 1] = curr   # TL
        
    fill_grid(grid, x + mid, y + mid, mid)              # TL
    fill_grid(grid, x + mid, y, mid)                    # TR
    fill_grid(grid, x, y + mid, mid)                    # BL
    fill_grid(grid, x, y, mid)                          # BR
    
        
def main():
    # grid size
    n = pow(2, int(input()))
    # initial missing cell location
    coord = input().split()
    x = int(coord[0])
    y = int(coord[1])
    # build matrix
    grid = [[None for i in range(n)] for j in range(n)]
    # remove initial cell
    grid[x][y] = -1
    fill_grid(grid, x, y, n) 
    for i in range(n):
        for j in range(n):
            if j != n-1:
                # print("{:02d}".format(grid[i][j]), end=" ")
                print(grid[i][j], end=" ")
            else:
                # print("{:02d}".format(grid[i][j]))
                print(grid[i][j])
          

if __name__ == "__main__":
    main()
