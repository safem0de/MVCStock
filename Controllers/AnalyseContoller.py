from tkinter import Toplevel
from Views.Analyse import *

class AnalyseContoller:

    def __init__(self,view):
        self.view = view

    def openAnalyseWindow(self):
        analyse = Toplevel()
        analyse.title("Stock Analyse")
        view = StockAnalyse(analyse)
        view.grid(row=0, column=0, padx=10, pady=10)
        print("5555")