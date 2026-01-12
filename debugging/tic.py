#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)

def check_winner(board):
    # Rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def board_full(board):
    return all(cell != " " for row in board for cell in row)

def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")
        except (EOFError, KeyboardInterrupt):
            print()
            raise

def get_valid_move(board, player):
    while True:
        try:
            row = read_int(f"Enter row (0, 1, or 2) for player {player}: ")
            col = read_int(f"Enter column (0, 1, or 2) for player {player}: ")
        except (EOFError, KeyboardInterrupt):
            return None, None

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Out of bounds. Row/column must be 0, 1, or 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        return row, col

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        row, col = get_valid_move(board, player)
        if row is None:  # user aborted (Ctrl+C / Ctrl+D)
            return

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            return

        if board_full(board):
            print_board(board)
            print("It's a draw!")
            return

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
