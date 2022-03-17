from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo

class CandleStick(ttk.Frame):

    def __init__(self,parent):
        super().__init__(parent)

        #create widgets
        self.labelheader = ttk.Label(self, text = 'CandleStick')
        self.labelheader.grid(row=0, column=0, sticky=tk.W)