#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # Check if a queen can be placed at board[row][col] without attacking any other queens
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def print_board(board):
        for row in board:
            print("".join("Q" if x == 1 else "." for x in row))

    def solve_util(board, col):
        if col >= N:
            print_board(board)
            print()
            return

        for i in range(N):
            if is_safe(board, i, col, N):
                board[i][col] = 1
                solve_util(board, col + 1)
                board[i][col] = 0

    board = [[0] * N for _ in range(N)]
    solve_util(board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

