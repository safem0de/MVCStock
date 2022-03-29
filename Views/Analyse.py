from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo

from Models.AnalyseDetails import *
from Controllers.AnalyseController import *

class StockAnalyse(tk.Toplevel):

    a = AnalysisData()

    def __init__(self,parent):
        super().__init__(parent)

        # https://www.pythontutorial.net/tkinter/tkinter-toplevel/
        # self.geometry('300x100')
        self.title('Analysis Mode')

        #create widgets
        self.labelheader = ttk.Label(self, text = 'Analyse')
        self.labelheader.grid(row=0, column=0, sticky=tk.W)
        
        # https://www.pythontutorial.net/tkinter/tkinter-checkbox/
        self.checkbox_asset_var = tk.StringVar()
        self.checkbox_asset = ttk.Checkbutton(
        self,
        text='อัตราการเติบโตของสินทรัพย์สูงกว่าค่าเฉลี่ย (Asset Growth)',
        command = lambda:self.test(self.checkbox_asset_var.get()),
        variable=self.checkbox_asset_var,
        onvalue='asset',
        offvalue='')
        self.checkbox_asset.grid(row=1, column=0, sticky=tk.W)

        self.checkbox_revenue_var = tk.StringVar()
        self.checkbox_revenue = ttk.Checkbutton(self,
        text='อัตราการเติบโตของรายได้สูงกว่าค่าเฉลี่ย (Revenue Growth)',
        command=lambda:print(self.checkbox_revenue_var.get()),
        variable=self.checkbox_revenue_var,
        onvalue='revenue',
        offvalue='')
        self.checkbox_revenue.grid(row=2, column=0, sticky=tk.W)

        self.checkbox_netprofit_var = tk.StringVar()
        self.checkbox_netprofit = ttk.Checkbutton(self,
        text='อัตราการเติบโตของกำไรสูงกว่าค่าเฉลี่ย (NetProfit Growth)',
        command=lambda:print(self.checkbox_netprofit_var.get()),
        variable=self.checkbox_netprofit_var,
        onvalue='netprofit',
        offvalue='')
        self.checkbox_netprofit.grid(row=3, column=0, sticky=tk.W)

        self.checkbox_ROE_var = tk.StringVar()
        self.checkbox_ROE = ttk.Checkbutton(self,
        text='อัตราการเติบโตของ ROE สูงกว่าค่าเฉลี่ย (ROE Growth)',
        command=lambda:print(self.checkbox_ROE_var.get()),
        variable=self.checkbox_ROE_var,
        onvalue='roe',
        offvalue='')
        self.checkbox_ROE.grid(row=4, column=0, sticky=tk.W)

        self.checkbox_PE_var = tk.StringVar()
        self.checkbox_PE = ttk.Checkbutton(self,
        text='ค่า PE ต่ำกว่าตลาด',
        command=lambda:print(self.checkbox_PE_var.get()),
        variable=self.checkbox_PE_var,
        onvalue='pe',
        offvalue='')
        self.checkbox_PE.grid(row=5, column=0, sticky=tk.W)

        self.checkbox_PE_var = tk.StringVar()
        self.checkbox_PE = ttk.Checkbutton(self,
        text='ค่า PE ต่ำกว่าตลาด',
        command=lambda:print(self.checkbox_PE_var.get()),
        variable=self.checkbox_PE_var,
        onvalue='pe',
        offvalue='')
        self.checkbox_PE.grid(row=5, column=0, sticky=tk.W)

        columns = ('first_name', 'last_name', 'email')

        self.tree = ttk.Treeview(self, columns=columns, show='headings', name='analyse')

        # define headings
        for col in columns:
            self.tree.heading(col, text = col)
            self.tree.column(col, minwidth=0, width=80, stretch=False)

        # generate sample data
        contacts = []
        for n in range(1, 100):
            contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

        for contact in contacts:
            self.tree.insert('', tk.END, values=contact)

        self.tree.grid(row=0, column=1, rowspan=20, pady=3, sticky=tk.NS)

    def test(self,x):
        print(x)

        f = Financial()
        print(type(f))

        print(type(self.a))


