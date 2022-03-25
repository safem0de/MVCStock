from multiprocessing.sharedctypes import Value
from tkinter import ttk
from tkinter import *
import tkinter as tk
from tkinter.messagebox import showinfo

import asyncio, time

from Models.StockDetails import *
from Controllers.StockController import *

from Models.AnalyseDetails import *
from Controllers.AnalyseContoller import *


from Controllers.CandleStickCotroller import *
from Views.Analyse import *

class MainMenu(ttk.Frame):

    stock = StockDetail()
    stockCtrl = StockController()

    status = stockCtrl.Intiallize()
    header = stockCtrl.StockHeader()
    set100 = stockCtrl.StockData()

    def __init__(self, parent):
        super().__init__(parent)

        anlsCtrl = AnalyseContoller()
        cdlsCtrl = CandleStickContoller()

        #create widgets
        self.labelheader = ttk.Label(self, text = 'SET100')
        self.labelheader.grid(row=0, column=0, sticky=tk.W)

        #create button Menu
        self.FinanceDetails_btn = ttk.Button(self, text='Stock NEWS')
        self.FinanceDetails_btn.grid(row=1, column=0, padx=3, sticky=tk.EW)

        self.StockDetails_btn = ttk.Button(self, text='CandleStick', command=lambda:cdlsCtrl.openCandelStick())
        self.StockDetails_btn.grid(row=2, column=0, padx=3, sticky=tk.EW)

        self.StockAnalyse_btn = ttk.Button(self, text='Analyse', command=lambda:asyncio.run(BtnAnalyseClick()))
        self.StockAnalyse_btn.grid(row=3, column=0, padx=3, sticky=tk.EW)

        self.labelfooter = ttk.Label(self, text = self.status)
        self.labelfooter.grid(row=40, column=0, padx=3, sticky=tk.S)

        # define columns
        columns = self.header

        self.tree = ttk.Treeview(self, columns=columns, show='headings', name='stock')

        # define headings
        for col in columns:
            self.tree.heading(col, text = col)
            self.tree.column(col, minwidth=0, width=80, stretch=False)

        # generate sample data
        # contacts = []
        # for n in range(1, 100):
        #     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

        # add data to the treeview
        for data in self.set100:
            self.tree.insert('', tk.END, values=data)

        def item_selected(event):
            for selected_item in self.tree.selection():
                item = self.tree.item(selected_item)
                record = item['values']
                # show a message
                # showinfo(title='Information', message=record[0])
                # print(record)
                self.stock.setStockName(record[0])
                self.stock.setRemark(record[1])
                self.stock.setOpenPrice(record[2])
                self.stock.setHighPrice(record[3])
                self.stock.setLowPrice(record[4])
                self.stock.setCurrentPrice(record[5])
                self.stock.setChange(record[6])
                self.stock.setPercentChange(record[7])
                self.stock.setOfferPrice(record[8])
                self.stock.setSalePrice(record[9])
                self.stock.setVolume(record[10])
                self.stock.setValue(record[11])
                # showinfo(title='Information', message=self.stock.getMessage())
                financialTable()

        self.tree.bind('<<TreeviewSelect>>', item_selected)

        # self.tree.grid(row=0, column=1, sticky=tk.NS)
        self.tree.grid(row=0, column=1, rowspan=20, pady=3, sticky=tk.NS)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=2, rowspan=20, pady=3, sticky=tk.NS)

        ### ------------------table2--------------------###
        def financialTable():
            # test = self.stockCtrl.PrepareDataToAnalyse(self.stock)
            # anlsCtrl.DataframeToModel(test)

            financial = self.stockCtrl.StockStatement(self.stock)
            fin_header = self.stockCtrl.StockStatementHeader(financial)
            fin_data = self.stockCtrl.StockStatementData(financial)

            # columns2 = self.fin_header
            columns2 = fin_header

            self.tree2 = ttk.Treeview(self, columns=columns2, show='headings', name='financial')
            
            for col2 in columns2:
                self.tree2.heading(col2, text = col2)
                self.tree2.column(col2, minwidth=0, width=160, stretch=False)

            # for data in self.fin_data:
            for data in fin_data:
                self.tree2.insert('', tk.END, values=data)

            self.tree2.grid(row=21, column=1, sticky=tk.NS)

            # add a scrollbar
            scrollbar2 = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree2.yview)
            self.tree2.configure(yscroll=scrollbar2.set)
            scrollbar2.grid(row=21, column=2, rowspan=20, sticky=tk.NS)

        # https://stackoverflow.com/questions/42231161/asyncio-gather-vs-asyncio-wait
        # https://stackoverflow.com/questions/14535730/what-does-hashable-mean-in-python
        async def BtnAnalyseClick():
            # self.StockAnalyse_btn.config(state=DISABLED)
            fin = Financial()

            __SETfucking100 = await self.stockCtrl.getSET100Name()
            __df_stock = [await self.stockCtrl.StockStatementDataFrame(l) for l in __SETfucking100]
            __prepared_df = [await self.stockCtrl.PrepareDataToAnalyse(l) for l in __df_stock]
            __dict_cleaned = {l.Name : await anlsCtrl.DataframeToModel(l) for l in __prepared_df}
            if not anlsCtrl.isValid_SET100_dict():
                [await anlsCtrl.setAllData(l,__dict_cleaned[l]) for l in __dict_cleaned]
                print("No Memories")

            anlsCtrl.openAnalyseWindow()
            anlsCtrl.deleteMinusProfit(fin)
            # anlsCtrl.calculateGrowth(fin,'asset')
            # anlsCtrl.calculateGrowth(fin,'revenue')
            # anlsCtrl.calculateGrowth(fin,'netprofit')

        def on_closing():
            if showinfo.askokcancel("Quit", "Do you want to quit?"):
                self.destroy()


