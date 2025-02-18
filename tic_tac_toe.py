import tkinter as tk
from tkinter import messagebox

def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_draw():
    return all(board[row][col] != " " for row in range(3) for col in range(3))

def on_click(row, col):
    global turn
    if board[row][col] == " " and not winner:
        board[row][col] = players[turn % 2]
        buttons[row][col].config(text=players[turn % 2])
        result = check_winner()
        if result:
            messagebox.showinfo("Game Over", f"Player {result} wins!")
            reset_board()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
        else:
            turn += 1

def reset_board():
    global board, turn, winner
    board = [[" " for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=" ")
    turn = 0
    winner = None

root = tk.Tk()
root.title("Tic Tac Toe")

players = ["X", "O"]
turn = 0
winner = None

board = [[" " for _ in range(3)] for _ in range(3)]
buttons = [[tk.Button(root, text=" ", font=('Arial', 24), width=5, height=2,
                      command=lambda r=row, c=col: on_click(r, c)) 
            for col in range(3)] for row in range(3)]

for row in range(3):
    for col in range(3):
        buttons[row][col].grid(row=row, column=col)

reset_button = tk.Button(root, text="Reset", font=('Arial', 14), command=reset_board)
reset_button.grid(row=3, column=0, columnspan=3)

root.mainloop()
