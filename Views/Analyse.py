from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo

from Models.AnalyseDetails import *
from Controllers.AnalyseController import AnalysisData

class StockAnalyse(tk.Toplevel):

    __stateOfFilter = []

    def __init__(self,parent,allData):
        self.allData = allData
        super().__init__(parent)

        self.f = Financial()
        # print(type(self.f))

        self.a = AnalysisData(self.allData)
        self.analyseTable(self.a.InitialTable(self.f))
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
        text=f'อัตราการเติบโตของสินทรัพย์สูงกว่าค่าเฉลี่ย (Asset Growth) >> {self.a.calculateMean_Growth(self.f,"asset")}',
        command = lambda:checkbox_assetSelected(self.checkbox_asset_var.get()),
        variable=self.checkbox_asset_var,
        onvalue='asset',
        offvalue='rm_asset')
        self.checkbox_asset.grid(row=1, column=0, padx=3, sticky=tk.W)

        self.checkbox_revenue_var = tk.StringVar()
        self.checkbox_revenue = ttk.Checkbutton(self,
        text=f'อัตราการเติบโตของรายได้สูงกว่าค่าเฉลี่ย (Revenue Growth) >> {self.a.calculateMean_Growth(self.f,"revenue")}',
        command=lambda:checkbox_revenueSelected(self.checkbox_revenue_var.get()),
        variable=self.checkbox_revenue_var,
        onvalue='revenue',
        offvalue='rm_revenue')
        self.checkbox_revenue.grid(row=2, column=0, padx=3, sticky=tk.W)

        self.checkbox_netprofit_var = tk.StringVar()
        self.checkbox_netprofit = ttk.Checkbutton(self,
        text=f'อัตราการเติบโตของกำไรสูงกว่าค่าเฉลี่ย (NetProfit Growth) >> {self.a.calculateMean_Growth(self.f,"netprofit")}',
        command=lambda:checkbox_netprofitSelected(self.checkbox_netprofit_var.get()),
        variable=self.checkbox_netprofit_var,
        onvalue='netprofit',
        offvalue='rm_netprofit')
        self.checkbox_netprofit.grid(row=3, column=0, padx=3, sticky=tk.W)

        self.checkbox_ROE_var = tk.StringVar()
        self.checkbox_ROE = ttk.Checkbutton(self,
        text=f'อัตราการเติบโตของ ROE สูงกว่าค่าเฉลี่ย (ROE Growth) >> {self.a.calculateMean_Growth(self.f,"roe")}',
        command=lambda:checkbox_roeSelected(self.checkbox_ROE_var.get()),
        variable=self.checkbox_ROE_var,
        onvalue='roe',
        offvalue='rm_roe')
        self.checkbox_ROE.grid(row=4, column=0, padx=3, sticky=tk.W)

        self.checkbox_PE_var = tk.StringVar()
        self.checkbox_PE = ttk.Checkbutton(self,
        text=f'ค่า PE ต่ำกว่าตลาด >> {None}',
        command=lambda:checkbox_peSelected(self.checkbox_PE_var.get()),
        variable=self.checkbox_PE_var,
        onvalue='pe',
        offvalue='rm_pe')
        self.checkbox_PE.grid(row=5, column=0, padx=3, sticky=tk.W)

        self.checkbox_PBV_var = tk.StringVar()
        self.checkbox_PBV = ttk.Checkbutton(self,
        text=f'ค่า P/BV ต่ำกว่าตลาด >> {None}',
        command=lambda:checkbox_pbvSelected(self.checkbox_PBV_var.get()),
        variable=self.checkbox_PBV_var,
        onvalue='pbv',
        offvalue='rm_pbv')
        self.checkbox_PBV.grid(row=6, column=0, padx=3, sticky=tk.W)

        def checkbox_assetSelected(x):
            if x == 'asset':
                self.__stateOfFilter.append(x)
            else:
                self.__stateOfFilter.remove('asset')

            y = self.a.clickEvents(self.f,self.__stateOfFilter)
            self.analyseTable(y)

        def checkbox_revenueSelected(x):
            if x == 'revenue':
                self.__stateOfFilter.append(x)
            else:
                self.__stateOfFilter.remove('revenue')

            y = self.a.clickEvents(self.f,self.__stateOfFilter)
            self.analyseTable(y)

        def checkbox_netprofitSelected(x):
            if x == 'netprofit':
                self.__stateOfFilter.append(x)
            else:
                self.__stateOfFilter.remove('netprofit')

            self.analyseTable(list())
            y = self.a.clickEvents(self.f,self.__stateOfFilter)
            self.analyseTable(y)

        def checkbox_roeSelected(x):
            if x == 'roe':
                self.__stateOfFilter.append(x)
            else:
                self.__stateOfFilter.remove('roe')

            self.analyseTable(list())
            y = self.a.clickEvents(self.f,self.__stateOfFilter)
            self.analyseTable(y)

        def checkbox_peSelected(x):
            if x == 'pe':
                self.__stateOfFilter.append(x)
            else:
                self.__stateOfFilter.remove('pe')

            y = self.a.clickEvents(self.f,self.__stateOfFilter)
            # self.analyseTable(y)

        def checkbox_pbvSelected(x):
            if x == 'pbv':
                self.__stateOfFilter.append(x)
            else:
                self.__stateOfFilter.remove('pbv')

            y = self.a.clickEvents(self.f,self.__stateOfFilter)
            # self.analyseTable(y)

    def analyseTable(self,stk):
        columns = ('หลักทรัพย์', 'งบ(ปี)ที่คำนวณ', '(สินทรัพย์)เฉลี่ย','(รายได้)เฉลี่ย','(กำไร)เฉลี่ย','(%ROE)เฉลี่ย','(P/E)ล่าสุด','(P/BV)ล่าสุด')
        self.tree = ttk.Treeview(self, columns=columns, show='headings', name='analyse')

        # define headings
        for col in columns:
            self.tree.heading(col, text = col)
            self.tree.column(col, minwidth=0, width=100, stretch=True, anchor=tk.CENTER)

        for s in stk:
            self.tree.insert('', tk.END, values=s)

        self.tree.grid(row=0, column=1, rowspan=20, pady=3, sticky=tk.NS)
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=2, rowspan=20, pady=3, sticky=tk.NS)

        self.labelfooter = ttk.Label(self, text = f'**ในตารางไม่นำ "หุ้น" ที่มีการขาดทุนในงบฯย้อนหลัง 3-5 ปี มาพิจารณา {len(stk)} ตัว', foreground='red')
        self.labelfooter.grid(row=40, column=0, columnspan=3, pady=3, sticky=tk.SE)





