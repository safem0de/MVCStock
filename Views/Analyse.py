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
        
        # https://www.pythontutorial.net/tkinter/tkinter-checkbox/
        self.checkbox_asset_var = tk.StringVar()
        self.checkbox_asset = ttk.Checkbutton(self,
                text='อัตราการเติบโตของสินทรัพย์ (Asset Growth)',
                command=lambda:print(self.checkbox_asset_var.get()),
                variable=self.checkbox_asset_var,
                onvalue='asset',
                offvalue='')
        self.checkbox_asset.grid(row=1, column=0, sticky=tk.W)

        self.checkbox_revenue_var = tk.StringVar()
        self.checkbox = ttk.Checkbutton(self,
                text='อัตราการเติบโตของรายได้ (Revenue Growth)',
                command=lambda:print(self.checkbox_revenue_var.get()),
                variable=self.checkbox_revenue_var,
                onvalue='revenue',
                offvalue='')
        self.checkbox.grid(row=2, column=0, sticky=tk.W)

        self.checkbox_netprofit_var = tk.StringVar()
        self.checkbox = ttk.Checkbutton(self,
                text='อัตราการเติบโตของกำไร (NetProfit Growth)',
                command=lambda:print(self.checkbox_netprofit_var.get()),
                variable=self.checkbox_netprofit_var,
                onvalue='netprofit',
                offvalue='')
        self.checkbox.grid(row=3, column=0, sticky=tk.W)
