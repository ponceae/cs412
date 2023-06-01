""" Coding Homework 7: Basic Graphs

    Parses through a matrix of 1s and 0s, where 1 is 
    land and 0 is water, to find the largest sized land 
    island in acres.

    Name:
        Adrien Ponce
    Honor Code:
        This code complies with the JMU Honor Code.
"""


def find_largest_island(matrix):

    def in_bounds(row, col):
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) 
    
    def search(row, col):
        if not in_bounds(row, col):
            return 0
        # current cell is water (or visited)
        if matrix[row][col] == 0:
            return 0
        # mark current cell as visited 
        matrix[row][col] = 0
        # visit current cell's horizontal and vertical neighbors
        return (1 + search(row - 1, col) + search(row, col - 1) 
                  + search(row + 1, col) + search(row, col + 1)) 
    result = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            # land cell found
            if matrix[row][col] == 1:
                count = search(row, col)
                result = max(count, result)
    return result

    
def main():
    n = int(input())
    matrix = []
    for _ in range(n):
        # append the row as a list of ints using list comprehension
        row = list(map(int, input().split()))
        matrix.append(row)
    print(find_largest_island(matrix))


if __name__ == "__main__":
    main()
