import tkinter as tk


class Cell(tk.Button):

    def __init__(self, master=None, text='', board=None):
        super().__init__(master)
        self.isBomb = False
        self.text = text
        self.isVisible = False
        self.board = board

        """Construct a button widget with the parent MASTER.

            STANDARD OPTIONS
        
                activebackground, activeforeground, anchor,
                background, bitmap, borderwidth, cursor,
                disabledforeground, font, foreground
                highlightbackground, highlightcolor,
                highlightthickness, image, justify,
                padx, pady, relief, repeatdelay,
                repeatinterval, takefocus, text,
                textvariable, underline, wraplength
        
            WIDGET-SPECIFIC OPTIONS
        
                command, compound, default, height,
                overrelief, state, width
        """
        self.button = tk.Button(self, text='', width=2, height=1, command=self.press_button)
        self.button.grid()

    def press_button(self):
        if not self.is_visible:
            self.button['text'] = self.button_value
            self.is_visible = True
            if self.board:
                self.board.click_count += 1
                print(self.board.clicks)

    @property
    def button_value(self):
        return self.text

    @button_value.setter
    def button_value(self, value):
        self.text = value

    @property
    def is_bomb(self):
        return self.isBomb

    @is_bomb.setter
    def is_bomb(self, value):
        self.isBomb = value

    @property
    def is_visible(self):
        return self.isVisible

    @is_visible.setter
    def is_visible(self, value):
        self.isVisible = value
