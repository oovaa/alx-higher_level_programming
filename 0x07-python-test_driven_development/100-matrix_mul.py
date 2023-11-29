#!/usr/bin/python3

def matrix_mul(m_a, m_b):

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

    result = [[0 for _ in range(len(m_b[0]))] for i in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
