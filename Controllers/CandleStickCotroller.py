from tkinter import Toplevel
from Views.CandleStick import *

class CandleStickContoller:

    def __init__(self):
        pass

    def openCandelStick(self):
        candle = Toplevel()
        candle.title("Candle Stick")
        candleview = CandleStickChart(candle)
        candleview.grid(row=0, column=0, padx=10, pady=10)
