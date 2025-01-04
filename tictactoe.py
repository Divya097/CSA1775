def print_board(board):
    """Print the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Check if there's a winner."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_full(board):
    """Check if the board is full."""
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """Play a game of Tic Tac Toe."""
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        # Get valid input
        while True:
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter column (0, 1, 2): "))
                if board[row][col] == " ":
                    break
                else:
                    print("Cell is already occupied. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter numbers between 0 and 2.")

        # Make the move
        board[row][col] = current_player
        
        # Check for a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        
        # Check for a draw
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
tic_tac_toe()
