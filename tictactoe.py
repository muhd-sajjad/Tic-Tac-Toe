import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.current_player = "O"  # Starting with "O"
        self.buttons = [[None, None, None] for _ in range(3)]  # 3x3 grid

        self.create_buttons()
        self.root.mainloop()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text="", width=8, height=4, command=lambda i=i, j=j: self.on_button_click(i, j))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

    def on_button_click(self, row, col):
        if not self.buttons[row][col]["text"]:  # Check if the button is empty
            self.buttons[row][col]["text"] = self.current_player

            if self.check_winner(row, col):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.root.destroy()
            elif all(self.buttons[i][j]["text"] for i in range(3) for j in range(3)):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.root.destroy()
            else:
                self.current_player = "X" if self.current_player == "O" else "O"  # Switch player

    def check_winner(self, row, col):
        # Check the row
        if all(self.buttons[row][j]["text"] == self.current_player for j in range(3)):
            return True

        # Check the column
        if all(self.buttons[i][col]["text"] == self.current_player for i in range(3)):
            return True

        # Check diagonals
        if all(self.buttons[i][i]["text"] == self.current_player for i in range(3)) or \
                all(self.buttons[i][2 - i]["text"] == self.current_player for i in range(3)):
            return True

        return False

# Create an instance of the TicTacToe class
tic_tac_toe_game = TicTacToe()
