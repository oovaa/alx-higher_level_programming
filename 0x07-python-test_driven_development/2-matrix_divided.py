#!/usr/bin/python3
"""Matrix Division Function.

This module defines a function that divides all elements of a matrix by a given divisor.

"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with elements rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists or if div is not an int or float.
        ZeroDivisionError: If div is 0.

    Examples:
        >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> matrix_divided(matrix, 2)
        [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0], [3.5, 4.0, 4.5]]

        >>> matrix = [[1.5, 2.5, 3.5], [4.5, 5.5, 6.5], [7.5, 8.5, 9.5]]
        >>> matrix_divided(matrix, 3)
        [[0.5, 0.83, 1.17], [1.5, 1.83, 2.17], [2.5, 2.83, 3.17]]

    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) and all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    rlen = len(matrix[0])
    if not all(len(x) == rlen for x in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        result.append(new_row)

    return result
