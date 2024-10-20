import math

# Constants for players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Function to initialize the board
def initialize_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

# Function to display the board
def display_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Function to check for a win
def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None

# Function to check for a draw
def is_draw(board):
    return all(cell != EMPTY for row in board for cell in row)

# Minimax algorithm implementation
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == PLAYER_O:
        return 1  # AI wins
    elif winner == PLAYER_X:
        return -1  # Player wins
    elif is_draw(board):
        return 0  # Draw

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O  # AI's turn
                    score = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY  # Undo move
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X  # Player's turn
                    score = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY  # Undo move
                    best_score = min(score, best_score)
        return best_score

# Function to find the best move for the AI
def find_best_move(board):
    best_score = -math.inf
    best_move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O  # AI's turn
                score = minimax(board, 0, False)
                board[i][j] = EMPTY  # Undo move
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    
    return best_move

# Main function to run the game
def play_game():
    board = initialize_board()
    while True:
        display_board(board)

        # Player's turn
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_X
                    break
                else:
                    print("Cell already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column values between 0 and 2.")

        # Check for win or draw after player's move
        if check_winner(board):
            display_board(board)
            print("Congratulations! You win!")
            break
        if is_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        # AI's turn
        print("AI is making a move...")
        row, col = find_best_move(board)
        board[row][col] = PLAYER_O

        # Check for win or draw after AI's move
        if check_winner(board):
            display_board(board)
            print("AI wins! Better luck next time.")
            break
        if is_draw(board):
            display_board(board)
            print("It's a draw!")
            break
# Start
play_game()