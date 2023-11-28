#!/usr/bin/python3
"""
N Queens puzzle solution
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at position (row, col)
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, n, solutions):
    """
    Recursively solve the N-Queens problem
    """
    if row == n:
        solution = [[i, board[i]] for i in range(n)]
        solutions.append(solution)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)


def print_solutions(solutions):
    """
    Print the solutions in the specified format
    """
    for solution in solutions:
        print(solution)


def main():
    """
    Main function to handle command-line arguments and solve the N-Queens
    """
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
