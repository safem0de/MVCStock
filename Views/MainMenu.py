from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo

from Models.StockDetails import *
from Controllers.StockController import *
from Controllers.AnalyseContoller import *
from Controllers.CandleStickCotroller import *
from Views.Analyse import *

class MainMenu(ttk.Frame):

    stock = StockDetail()
    stockCtrl = StockController()

    status = stockCtrl.Intiallize()
    header = stockCtrl.StockHeader()
    set100 = stockCtrl.StockData()

    test = stockCtrl.testcreateusableDF(stock)

    financial = stockCtrl.StockStatement(stock)
    fin_header = stockCtrl.StockStatementHeader(stock)
    fin_data = stockCtrl.StockStatementData(stock)

    def __init__(self, parent):
        super().__init__(parent)

        anlsCtrl = AnalyseContoller(self)
        cdlsCtrl = CandleContoller(self)

        #create widgets
        self.labelheader = ttk.Label(self, text = 'SET100')
        self.labelheader.grid(row=0, column=0, sticky=tk.W)

        #create button Menu
        self.FinanceDetails_btn = ttk.Button(self, text='Stock NEWS')
        self.FinanceDetails_btn.grid(row=1, column=0, padx=3, sticky=tk.EW)

        self.StockDetails_btn = ttk.Button(self, text='CandleStick', command=lambda:cdlsCtrl.openCandelStick())
        self.StockDetails_btn.grid(row=2, column=0, padx=3, sticky=tk.EW)

        self.StockAnalyse_btn = ttk.Button(self, text='Analyse', command=lambda:anlsCtrl.openAnalyseWindow())
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
                print(self.stock.getStockName())
                self.financial = self.stockCtrl.StockStatement(self.stock)
                self.fin_header = self.stockCtrl.StockStatementHeader(self.stock)
                self.fin_data = self.stockCtrl.StockStatementData(self.stock)
                showinfo(title='Information', message=self.stock.getMessage())
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
            self.test = self.stockCtrl.testcreateusableDF(self.stock)
            columns2 = self.fin_header

            self.tree2 = ttk.Treeview(self, columns=columns2, show='headings', name='financial')
            
            for col2 in columns2:
                self.tree2.heading(col2, text = col2)
                self.tree2.column(col2, minwidth=0, width=160, stretch=False)

            for data in self.fin_data:
                self.tree2.insert('', tk.END, values=data)

            self.tree2.grid(row=21, column=1, sticky=tk.NS)

            # add a scrollbar
            scrollbar2 = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree2.yview)
            self.tree2.configure(yscroll=scrollbar2.set)
            scrollbar2.grid(row=21, column=2, rowspan=20, sticky=tk.NS)

