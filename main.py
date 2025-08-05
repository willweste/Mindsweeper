import math
import random
import tkinter as tk
from cell import Cell
from logic import Logic


class Application(tk.Tk):
    def __init__(self, master=None, row=10, col=10):
        super().__init__(master)
        self.title('MindSweeper')
        self.board = Logic(self, row, col)
        self.board.pack()


if __name__ == '__main__':
    app = Application(row=4, col=4)
    app.mainloop()  # Keep this at the bottom
