#!/usr/bin/python3
""" Rotate Matrix module """


def rotate_2d_matrix(matrix):
    """ Rotate a 2D matrix in place
    Args:
        (matrix): a non-empty, 2-Dimensional matrix
    Returns:
        Nothing
    """
    rotated_matrix = []

    for column in range(len(matrix)):
        matrix_row = []
        for row in range(len(matrix) - 1, -1, -1):
            matrix_row.append(matrix[row][column])
        rotated_matrix.append(matrix_row)

    for row in range(len(rotated_matrix)):
        for column in range(len(rotated_matrix[0])):
            matrix[row][column] = rotated_matrix[row][column]
