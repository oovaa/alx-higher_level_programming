#!/usr/bin/python3
"""
This script is used to find a peak element in a list of integers.

A peak element is an element that is greater than its neighbors.

Example:
    Input: [1, 2, 3, 1]
    Output: 3

"""


def find_peak(list_of_integers):
    """
    Finds and returns the peak element in a list of integers.

    Args:
        list_of_integers (list): A list of integers.

    Returns:
        int: The peak element in the list.

    Raises:
        ValueError: If the list is empty.

    Examples:
        >>> find_peak([1, 2, 3, 4, 5])
        5

        >>> find_peak([5, 4, 3, 2, 1])
        5

        >>> find_peak([1, 3, 2, 4, 5])
        3
    """
    for i, v in enumerate(list_of_integers):
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        if list_of_integers[-1] > list_of_integers[-2]:
            return list_of_integers[-1]

        for i in range(1, len(list_of_integers)-1):
            if list_of_integers[i] > list_of_integers[i + 1] and \
                    list_of_integers[i] > list_of_integers[i-1]:
                return list_of_integers[i]
