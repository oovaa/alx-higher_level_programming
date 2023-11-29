#!/usr/bin/python3
"""Module with a function that multiplies two matrices using NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    This function uses NumPy to perform matrix multiplication on two input
    `m_a` and `m_b`.

    Parameters:
    - m_a (list of lists): The first matrix.
    - m_b (list of lists): The second matrix.

    Returns:
    - np.ndarray: The resulting matrix after multiplication.

    Example:
    >>> m_a = [[1, 2], [3, 4]]
    >>> m_b = [[1, 2], [3, 4]]
    >>> lazy_matrix_mul(m_a, m_b)
    array([[ 1,  4],
           [ 9, 16]])
    """
    return (np.matmul(m_a, m_b))
