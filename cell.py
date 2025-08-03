import tkinter as tk


class Cell(tk.Frame):

    def __init__(self, text, master=None):
        super().__init__(master)
        self.isBomb = False
        self.text = text

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
        self.button = tk.Button(self, text='EMPTY', width=2, height=1)
        self.button.grid()

    @property
    def button_value(self):
        return self.text

    @button_value.setter
    def button_value(self, value):
        self.text = value
