#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(a, list) for a in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(a, list) for a in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if not all(all(isinstance(b, (int, float))for b in x) for x in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(all(isinstance(b, (int, float))for b in x) for x in m_b):
        raise TypeError("m_b should contain only integers or floats")

    if len(set([len(x) for x in m_a])) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set([len(x) for x in m_b])) != 1:
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for r in range(len(m_b[0])):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        inverted_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
