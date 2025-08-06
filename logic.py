import tkinter as tk
import random
from cell import Cell
import math


class Logic(tk.Frame):
    def __init__(self, master=None, row=10, col=10):
        super().__init__(master)
        self.row = row
        self.col = col
        self.cells = self.createGrid()
        self.placeBombs()
        self.clicks = 0
        self.score = 0

    def createGrid(self):
        grid = []
        for i in range(self.row):
            row = []
            for j in range(self.col):
                seed = random.randint(0, 1)
                btn = Cell(self, text=seed, board=self)
                btn.nis_bomb = False
                btn.grid(row=i, column=j)
                row.append(btn)
            grid.append(row)
        return grid

    def placeBombs(self):
        seed = random.randint(0, 1)
        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                cell = self.cells[row][col]
                if cell.button_value == seed:
                    cell.is_bomb = True

    @property
    def click_count(self):
        return self.clicks

    @click_count.setter
    def click_count(self, value):
        self.clicks = value

    @property
    def score_count(self):
        return self.score

    @score_count.setter
    def score_count(self, value):
        self.score = value
