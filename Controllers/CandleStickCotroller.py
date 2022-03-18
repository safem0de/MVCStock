from tkinter import Toplevel
from Views.CandleStick import *

class CandleContoller:

    def __init__(self):
        pass

    def openCandelStick(self):
        candle = Toplevel()
        candle.title("Candle Stick")
        view = CandleStick(candle)
        view.grid(row=0, column=0, padx=10, pady=10)
