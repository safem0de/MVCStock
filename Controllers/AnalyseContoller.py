from tkinter import Toplevel
from Views.Analyse import *

import pandas as pd

class AnalyseContoller:

    def __init__(self):
        pass

    def openAnalyseWindow(self):
        analyse = Toplevel()
        analyse.title("Stock Analyse")
        view = StockAnalyse(analyse)
        view.grid(row=0, column=0, padx=10, pady=10)

    def DataframeToModel(self,df):

        for row_index,row in df.iterrows():
            print(row[0])
            print(row[1:].to_dict(),sep='\n')
            # print(row_index, row, sep='\n')cls
