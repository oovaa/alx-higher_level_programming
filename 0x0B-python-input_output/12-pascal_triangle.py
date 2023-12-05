#!/usr/bin/python3

"""Task 12: Pascal's Triangle"""


def pascal_triangle(n):
    """Create a Pascal's Triangle.

    Args:
        n (int): The number of rows of the triangle to generate.

    Returns:
        list: A list of lists, where each inner list represents a row.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # The first row is always [1]

    for i in range(1, n):
        row = [1]  # Every row starts with 1
        for j in range(1, i):
            # Add the sum of the two numbers above this position.
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Every row ends with 1
        triangle.append(row)

    return triangle
