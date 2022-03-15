from tkinter import ttk
import tkinter as tk

from Models.StockDetails import *
from Controllers.StockController import *

class MainMenu(ttk.Frame):

    stock = StockDetails()
    stockCtrl = StockController()
    stockCtrl.Intiallize(stock)

    def __init__(self, parent):
        super().__init__(parent)

        #create widgets
        self.labelheader = ttk.Label(self, text = 'SET100')
        self.labelheader.grid(row=0, column=0, sticky=tk.W)

        #create button Menu
        self.FinanceDetails_btn = ttk.Button(self, text='Financial Statement')
        self.FinanceDetails_btn.grid(row=1, column=0, padx=3, sticky=tk.W)

        self.StockDetails_btn = ttk.Button(self, text='CandleStick')
        self.StockDetails_btn.grid(row=2, column=0, padx=3, sticky=tk.W)

        self.StockAnalyse_btn = ttk.Button(self, text='Analyse')
        self.StockAnalyse_btn.grid(row=3, column=0, padx=3, sticky=tk.W)

        self.labelfooter = ttk.Label(self, text = self.stock.getMessage())
        self.labelfooter.grid(row=4, column=0, sticky=tk.SW)

        # define columns
        columns = ('first_name', 'last_name', 'email')

        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        self.tree.heading('first_name', text='First Name')
        self.tree.heading('last_name', text='Last Name')
        self.tree.heading('email', text='Email')

        # generate sample data
        contacts = []
        for n in range(1, 100):
            contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

        # add data to the treeview
        for contact in contacts:
            self.tree.insert('', tk.END, values=contact)


        # def item_selected(event):
        #     for selected_item in self.tree.selection():
        #         item = self.tree.item(selected_item)
        #         record = item['values']
        #         # show a message
        #         self.showinfo(title='Information', message=','.join(record))


        # self.tree.bind('<<TreeviewSelect>>', item_selected)

        # self.tree.grid(row=0, column=1, sticky=tk.NS)
        self.tree.grid(row=0, column=1, columnspan = 3, rowspan = 20, sticky=tk.NS)

        # add a scrollbar
        # scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
        # tree.configure(yscroll=scrollbar.set)
        # scrollbar.grid(row=0, column=1, sticky='ns')

