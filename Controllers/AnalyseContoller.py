from tkinter import Toplevel
from Views.Analyse import *
from Models.AnalyseDetails import *

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
        cleanDatas = {}
        for row_index,row in df.iterrows():
            m = pd.to_numeric(row[1:], errors='ignore')
            cleanDatas[row[0]] = m.to_dict()
        return cleanDatas

    