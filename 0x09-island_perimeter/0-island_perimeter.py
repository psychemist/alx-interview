#!/usr/bin/python3
"""
5-island perimeter module calculates perimeter of an island
"""


def island_perimeter(grid):
    """
    Returns:
        (int): perimeter of the island described in grid

    Args:
        grid (matrix): list of list of integers
    """
    rows = len(grid)
    columns = len(grid[0])
    count = 0

    for row in range(rows):
        for col in range(columns):
            if grid[row][col] == 1:
                count += 4
                if row + 1 < rows and grid[row + 1][col] == 1:
                    count -= 2
                if col + 1 < columns and grid[row][col + 1] == 1:
                    count -= 2

    return count
