#!/usr/bin/python3
"""Module 12-pascal_triangle finds the pascal triangle representation of n rows
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing a Pascal’s Triangle

    Args:
        n (int): number of rows in pascal triangle

    Returns:
        1. List representation of pascal's triangle of n
        2. Empty list if n <= 0
    """
    triangle = []

    if n > 0:
        # Iterate over triangle height
        for line in range(n):
            # Create new empty list to hold ints
            nums = []
            # Loop through row size (number of columns)
            for num in range(line + 1):
                # Append 1 at beginning and end of row
                if num == 0 or num == line:
                    nums.append(1)
                # Get sum of prev row[[column - 1] + [column]] and append
                else:
                    nums.append(triangle[line - 1][num - 1] +
                                triangle[line - 1][num])
            # Append list of integers to triangle
            triangle.append(nums)

    return triangle
