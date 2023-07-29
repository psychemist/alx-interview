#!/usr/bin/python3
"""Module 12-pascal_triangle finds the pascal triangle representation of n rows
"""


def factorial(n):
    """
    Returns the factorial of a number

    Args:
        n (int): nnumber to be factorized
    """
    if n < 2:
        return 1
    return n * factorial(n - 1)


def combination(n, k):
    """
    Calculates each triangle cell using the "n choose k" formula

    Args:
        n (int): index of cell row in triangle
        k (int): index of cell column in triangle
    """
    return (factorial(n) // (factorial(k) * factorial(n - k)))


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing a Pascal’s Triangle

    Args:
        n (int): number of rows in pascal triangle

    Returns:
        1. List comprehension representation of pascal's triangle of n
        2. Empty list if n <= 0
    """
    triangle = []

    if n > 0:
        triangle = [[combination(nums, num)
                     for num in range(nums + 1)] for nums in range(n)]
    return triangle
