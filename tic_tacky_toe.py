def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    
    while True:
        print_board(board)
        player = players[turn % 2]
        
        try:
            row, col = map(int, input(f"Player {player}, enter row and column (0-2, space-separated): ").split())
            if board[row][col] != " ":
                print("Cell already occupied! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter numbers between 0 and 2.")
            continue
        
        board[row][col] = player
        
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        turn += 1

if __name__ == "__main__":
    tic_tac_toe()
