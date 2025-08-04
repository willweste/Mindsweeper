import math
import random
import tkinter as tk
from cell import Cell


class Application(tk.Frame):
    def __init__(self, master=None, row=10, col=10):
        super().__init__(master)
        self.row = row
        self.col = col
        self.quitButton = None
        self.grid()
        self.createWidgets()
        self.cells = self.createGrid()

    def createWidgets(self):
        return

    def createGrid(self):
        grid = []
        for i in range(self.row):
            row = []
            for j in range(self.col):
                random_seed = math.floor(random.random() * 2)
                btn = Cell(f'{random_seed}')
                btn.button.config(text="")
                btn.grid(row=i, column=j)
                row.append(btn)
            grid.append(row)
        return grid

    def placeBombs(self):
        seed = str(math.floor(random.random() * 2))
        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                cell = self.cells[row][col]
                if cell.button_value == seed:
                    cell.button.config(text='BOMB')
                    cell.isBomb = True


if __name__ == '__main__':
    app = Application(None, 4, 4)
    # Set the window size to 400x300 pixels
    # app.master.geometry("400x300")
    # Prevent the window from being resized by the user
    app.master.resizable(True, True)
    app.placeBombs()
    app.mainloop()  # Keep this at the bottom
