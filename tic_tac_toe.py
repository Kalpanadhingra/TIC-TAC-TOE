import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.current_player = 'X'
        self.board = [' ' for _ in range(9)]  # A list to hold the board state

        # Label to show the current player's turn
        self.label = tk.Label(self.root, text=f"Player {self.current_player}'s turn", font='Arial 14')
        self.label.grid(row=0, column=0, columnspan=3)

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text=' ', font='Arial 20', width=5, height=2,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i + 1, column=j)
                row.append(button)
            self.buttons.append(row)

    def on_button_click(self, i, j):
        index = i * 3 + j
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif ' ' not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        for row in self.buttons:
            for button in row:
                button.config(text=' ')
        self.label.config(text=f"Player {self.current_player}'s turn")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
