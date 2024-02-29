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
    if not list_of_integers:
        return None

    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]
    elif length == 2:
        return max(list_of_integers)

    mid = length // 2
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid-1] and peak > list_of_integers[mid+1]:
        return peak
    elif peak < list_of_integers[mid-1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid+1:])
