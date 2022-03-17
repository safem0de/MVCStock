from tkinter import Toplevel
from Views.Analyse import *

class CandleContoller:

    def __init__(self,view):
        self.view = view

    def openCandelStick(self):
        analyse = Toplevel()
        analyse.title("Candle Stick")
        view = StockAnalyse(analyse)
        view.grid(row=0, column=0, padx=10, pady=10)
