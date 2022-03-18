from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo

from Models.AnalyseDetails import *
from Controllers.StockController import *

class StockAnalyse(ttk.Frame):

    fin = Financial()

    def __init__(self,parent):
        super().__init__(parent)

        #create widgets
        self.labelheader = ttk.Label(self, text = 'Analyse')
        self.labelheader.grid(row=0, column=0, sticky=tk.W)
