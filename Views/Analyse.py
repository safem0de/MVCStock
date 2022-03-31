from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo

from Models.AnalyseDetails import *
from Controllers.AnalyseController import *

class StockAnalyse(tk.Toplevel):

    def __init__(self,parent,allData):
        self.allData = allData
        super().__init__(parent)

        self.f = Financial()
        # print(type(self.f))

        self.a = AnalysisData(self.allData)
        # self.a.deleteMinusProfit(self.f)
        
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
        command = lambda:checkbox_assetSelected(self.checkbox_asset_var.get()),
        variable=self.checkbox_asset_var,
        onvalue='asset',
        offvalue='')
        self.checkbox_asset.grid(row=1, column=0, padx=3, sticky=tk.W)

        self.checkbox_revenue_var = tk.StringVar()
        self.checkbox_revenue = ttk.Checkbutton(self,
        text='อัตราการเติบโตของรายได้สูงกว่าค่าเฉลี่ย (Revenue Growth)',
        command=lambda:print(self.checkbox_revenue_var.get()),
        variable=self.checkbox_revenue_var,
        onvalue='revenue',
        offvalue='')
        self.checkbox_revenue.grid(row=2, column=0, padx=3, sticky=tk.W)

        self.checkbox_netprofit_var = tk.StringVar()
        self.checkbox_netprofit = ttk.Checkbutton(self,
        text='อัตราการเติบโตของกำไรสูงกว่าค่าเฉลี่ย (NetProfit Growth)',
        command=lambda:print(self.checkbox_netprofit_var.get()),
        variable=self.checkbox_netprofit_var,
        onvalue='netprofit',
        offvalue='')
        self.checkbox_netprofit.grid(row=3, column=0, padx=3, sticky=tk.W)

        self.checkbox_ROE_var = tk.StringVar()
        self.checkbox_ROE = ttk.Checkbutton(self,
        text='อัตราการเติบโตของ ROE สูงกว่าค่าเฉลี่ย (ROE Growth)',
        command=lambda:print(self.checkbox_ROE_var.get()),
        variable=self.checkbox_ROE_var,
        onvalue='roe',
        offvalue='')
        self.checkbox_ROE.grid(row=4, column=0, padx=3, sticky=tk.W)

        self.checkbox_PE_var = tk.StringVar()
        self.checkbox_PE = ttk.Checkbutton(self,
        text='ค่า PE ต่ำกว่าตลาด',
        command=lambda:print(self.checkbox_PE_var.get()),
        variable=self.checkbox_PE_var,
        onvalue='pe',
        offvalue='')
        self.checkbox_PE.grid(row=5, column=0, padx=3, sticky=tk.W)

        self.checkbox_PE_var = tk.StringVar()
        self.checkbox_PE = ttk.Checkbutton(self,
        text='ค่า PE ต่ำกว่าตลาด',
        command=lambda:print(self.checkbox_PE_var.get()),
        variable=self.checkbox_PE_var,
        onvalue='pe',
        offvalue='')
        self.checkbox_PE.grid(row=5, column=0, padx=3, sticky=tk.W)

        columns = ('หลักทรัพย์', 'งบ(ปี)', 'อัตราการเติบโต(สินทรัพย์)เฉลี่ย','อัตราการเติบโต(รายได้)เฉลี่ย','อัตราการเติบโต(กำไร)เฉลี่ย')
        self.tree = ttk.Treeview(self, columns=columns, show='headings', name='analyse')

        # define headings
        for col in columns:
            self.tree.heading(col, text = col)
            self.tree.column(col, minwidth=0, width=150, stretch=True, anchor=tk.CENTER)

        contacts = self.a.deleteMinusProfit(self.f)

        for contact in contacts:
            self.tree.insert('', tk.END, values=contact)

        self.tree.grid(row=0, column=1, rowspan=20, pady=3, sticky=tk.NS)
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=2, rowspan=20, pady=3, sticky=tk.NS)

        self.labelfooter = ttk.Label(self, text = '**ในตารางไม่นำ "หุ้น" ที่มีการขาดทุนในงบฯย้อนหลัง 3-5 ปี มาพิจารณา', foreground='red')
        self.labelfooter.grid(row=40, column=0, columnspan=3, pady=3, sticky=tk.SE)

        def checkbox_assetSelected(x):
            print(x)
            self.a.calculateGrowth(self.f,x)



