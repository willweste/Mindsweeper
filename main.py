import math
import random
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None, row=10, col=10):
        super().__init__(master)
        self.row = row
        self.col = col
        self.quitButton = None
        self.grid()
        self.createWidgets()
        self.cells = self.createGrid()
        self.tileMap = self.createTileMap()

    def createWidgets(self):
        return

    def createTileMap(self):
        tile_map = []
        for i in range(self.row):
            tile_row = []
            for j in range(self.col):
                tile_row.append(0)
            tile_map.append(tile_row)
        return tile_map

    def createGrid(self):
        grid = []
        for i in range(self.row):
            row = []
            for j in range(self.col):
                random_seed = math.floor(random.random() * 2)
                btn = tk.Button(text=f'{random_seed}', width=2, height=1)
                btn.grid(row=i, column=j)
                row.append(btn)
            grid.append(row)
        return grid

    def placeBombs(self):
        seed = str(math.floor(random.random() * 2))
        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                if self.cells[row][col]['text'] == seed:
                    self.cells[row][col].config(text="BOMB")


if __name__ == '__main__':
    app = Application(None, 4, 4)
    # Set the window size to 400x300 pixels
    # app.master.geometry("400x300")
    # Prevent the window from being resized by the user
    app.master.resizable(True, True)
    app.placeBombs()
    print(app.tileMap)
    app.mainloop()  # Keep this at the bottom
