import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Function to evaluate the current state of the board for the Minimax algorithm
def evaluate_board(board):
    if check_winner(board, 'X'):
        return -1
    elif check_winner(board, 'O'):
        return 1
    elif is_board_full(board):
        return 0
    else:
        return None

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate_board(board)

    if score is not None:
        return score

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the AI player using Minimax
def find_best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Main game loop
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        # Human player's move
        while True:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("Invalid move. Try again.")

        # Check if human player won
        if check_winner(board, 'X'):
            print_board(board)
            print("Congratulations! You won!")
            break

        # Check if it's a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # AI player's move
        print("AI player is making a move...")
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = 'O'

        # Check if AI player won
        if check_winner(board, 'O'):
            print_board(board)
            print("AI player wins! Better luck next time.")
            break

        # Check if it's a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

# Run the game
play_game()
