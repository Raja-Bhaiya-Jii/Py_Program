"""Program 13: Tic Tac Toe
A classic two-player Tic Tac Toe game played on the command line.
Players take turns marking X and O on a 3x3 grid. First to get three in a row wins.
"""
import random


def print_board(board):
    """Display the current board state."""
    print()
    print(f"  {board[0]} | {board[1]} | {board[2]} ")
    print(" ---+---+---")
    print(f"  {board[3]} | {board[4]} | {board[5]} ")
    print(" ---+---+---")
    print(f"  {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    """Check if the given player has three in a row."""
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   # columns
        [0, 4, 8], [2, 4, 6],               # diagonals
    ]
    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


def is_board_full(board):
    """Check if the board is completely filled."""
    return all(cell != " " for cell in board)


def get_player_move(board, player):
    """Ask the player for their move and validate it."""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if 1 <= move <= 9 and board[move - 1] == " ":
                return move - 1
            elif 1 <= move <= 9:
                print("That cell is already taken. Try again.")
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")


def get_computer_move(board, player, opponent):
    """Simple AI: win if possible, block if needed, otherwise pick a strategic cell."""
    # Try to win
    for i in range(9):
        if board[i] == " ":
            board[i] = player
            if check_winner(board, player):
                return i
            board[i] = " "
    # Block opponent
    for i in range(9):
        if board[i] == " ":
            board[i] = opponent
            if check_winner(board, opponent):
                board[i] = " "
                return i
            board[i] = " "
    # Pick center, then corners, then edges
    preferred = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    for i in preferred:
        if board[i] == " ":
            return i
    return -1


def play_game():
    """Run a single game of Tic Tac Toe."""
    board = [" "] * 9
    print()
    print("=== Tic Tac Toe ===")
    print("Positions are numbered 1-9, left to right, top to bottom:")
    print("  1 | 2 | 3 ")
    print(" ---+---+---")
    print("  4 | 5 | 6 ")
    print(" ---+---+---")
    print("  7 | 8 | 9 ")

    mode = input("\nPlay mode - (1) Two Player  (2) vs Computer: ").strip()
    vs_computer = mode == "2"

    current = "X"
    while True:
        print_board(board)

        if vs_computer and current == "O":
            print("Computer's turn...")
            move = get_computer_move(board, "O", "X")
        else:
            move = get_player_move(board, current)

        board[move] = current

        if check_winner(board, current):
            print_board(board)
            if vs_computer and current == "O":
                print("Computer wins!")
            else:
                print(f"Player {current} wins!")
            return

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            return

        current = "O" if current == "X" else "X"


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
