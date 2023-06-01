"""
CS 412 Tiling Problem Visualizer
Author: Molloy (Feb 2023)

Input: from stdin the matrix of tiles

Output: produces a visualization of the tiling

NOTE: This program assigns tiles a random color.  It is
possible that the color of two adj tiles will be very similar.
"""

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

import random


def stdinToMatrix():
    """
    Read in the matrix from stdin and return a 2D list
    """
    matrix = []

    row = input().split()
    rowsize = len(row)  # compute # of rows (since numrows == numcols)
    matrix.append([int(i) for i in row])

    for _ in range(rowsize - 1):
        matrix.append([int(i) for i in input().split()])
    
    return matrix


def draw_tiling(matrix):
    """
    Compute and display the plot
    """
    
    # create set of unique tile numbers
    tiling_indices = set([x for row in matrix for x in row])

    colorlist = [(0,0,0)]  # initial empty space

    """
    Adjacent tiles were sometimes too close in color.  The first two colors
    in the RGB tuple are now "seeded" by the tile number in hopes of
    reducing the likelihood of "close" colors being adjacent.
    """
    for tile in tiling_indices:
        if tile != -1:
            newColor = ((tile*17)%255 + 10, (tile*37)%255 + 10,random.randint(10,255))
            colorlist.append(newColor)
    
    cmap = colors.ListedColormap(colorlist)

    bounds = [-1] + list(range(len(tiling_indices))) # map tilenumbers to colors
    fig, ax = plt.subplots()

    ax.imshow(matrix, cmap=cmap)
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
    
    ax.set_xticks(np.arange(-.5, len(matrix[0]), 1));
    ax.set_yticks(np.arange(-.5, len(matrix[0]), 1));

    plt.show()

if __name__ == "__main__":
    matrix = stdinToMatrix()
    draw_tiling(matrix)
