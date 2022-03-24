from os import remove
from tkinter import Toplevel

from numpy import average
from Views.Analyse import *
from Models.AnalyseDetails import *

import pandas as pd

class AnalyseContoller:

    __dictOfSET100 = {}
    __caculatedSET100 = {}

    def __init__(self):
        pass

    def openAnalyseWindow(self):
        analyse = Toplevel()
        analyse.title("Stock Analyse")
        view = StockAnalyse(analyse)
        view.grid(row=0, column=0, padx=10, pady=10)

    def isValid_SET100_dict(self):
        return bool(self.__dictOfSET100)

    async def DataframeToModel(self,df):
        cleanDatas = {}
        for row_index,row in df.iterrows():
            m = pd.to_numeric(row[1:], errors='ignore')
            cleanDatas[row[0]] = m.to_dict()
        return cleanDatas

    async def setAllData(self,i,data):
        analyseModel = Financial()
        analyseModel.setAssets(data['สินทรัพย์รวม'])
        analyseModel.setLiabilities(data['หนี้สินรวม'])
        analyseModel.setEquity(data['ส่วนของผู้ถือหุ้น'])
        analyseModel.setCapital(data['มูลค่าหุ้นที่เรียกชำระแล้ว'])
        analyseModel.setRevenue(data['รายได้รวม'])
        analyseModel.setProfit_Loss(data['กำไร (ขาดทุน) จากกิจกรรมอื่น'])
        analyseModel.setNetProfit(data['กำไรสุทธิ'])
        analyseModel.setEPS(data['กำไรต่อหุ้น (บาท)'])
        analyseModel.setROA(data['ROA(%)'])
        analyseModel.setROE(data['ROE(%)'])
        analyseModel.setMargin(data['อัตรากำไรสุทธิ(%)'])
        analyseModel.setLastPrice(data['ราคาล่าสุด(บาท)'])
        analyseModel.setMarketCap(data['มูลค่าหลักทรัพย์ตามราคาตลาด'])
        analyseModel.setFSPeriod(data['วันที่ของงบการเงินที่ใช้คำนวณค่าสถิติ'])
        analyseModel.setPE(data['P/E (เท่า)'])
        analyseModel.setPBV(data['P/BV (เท่า)'])
        analyseModel.setBookValuepershare(data['มูลค่าหุ้นทางบัญชีต่อหุ้น (บาท)'])
        analyseModel.setDvdYield(data['อัตราส่วนเงินปันผลตอบแทน(%)'])
        self.__dictOfSET100[i] = analyseModel


    def deleteMinusProfit(self, financials):
        cal = self.__dictOfSET100
        removal_list = []
        for c in cal:
            financials = cal.get(c)
            netprofit = financials.getNetProfit()
            for key in list(netprofit):
                if not netprofit[key] == "-":
                    if float(netprofit[key]) < 0:
                        if not c in removal_list:
                            removal_list.append(c)

        for l in removal_list:
            cal.pop(l)

        self.__dictOfSET100 = cal


    # https://realpython.com/iterate-through-dictionary-python/
    # https://www.w3schools.com/python/python_dictionaries_access.asp
    def calculateGrowth(self, financials, datatype):
        all_average_growth = []
        removal_list = []
        average_growth = 0
        more_is_good = True
        cal = self.__dictOfSET100
        for c in cal:
            financials = cal.get(c)
            if datatype == "asset":
                growthtype = financials.getAssets()
            elif datatype == "revenue":
                growthtype = financials.getRevenue()
            elif datatype == "netprofit":
                growthtype = financials.getNetProfit()
            elif datatype == "roe":
                growthtype = financials.getROE()
            else:
                growthtype = financials.getAssets()

            year = []
            asset = []
            for key in sorted(growthtype, reverse=True):
                if not growthtype[key] == "-":
                    year.append(int(key))
                    asset.append(float(growthtype[key]))

            year_asset = list(zip(year,asset))
            res_growth = []
            for i in range(len(year_asset)):
                
                if i+1 < len(year_asset):
                    # print(f"((สินทรัพย์ปี {year_asset[i][0]} - สินทรัพย์ปี {year_asset[i+1][0]})/ สินทรัพย์ปี {year_asset[i+1][0]})*100")
                    # print("อัตราการเติบโตของทรัพย์สิน (ต่อปี)")
                    x = ((year_asset[i][1]-year_asset[i+1][1])/year_asset[i+1][1])*100
                    if len(res_growth) < 3:
                        res_growth.append(round(x,3))

            # print(c)
            # print(res_growth)
            all_average_growth.append(round(sum(res_growth)/len(res_growth),3))
            removal_list.append([c,round(sum(res_growth)/len(res_growth),3)])
            
        average_growth = round(sum(all_average_growth)/len(all_average_growth),3)
        print(datatype, average_growth)

        if more_is_good:
            for l in removal_list:
                if l[1] < average_growth:
                    # print(l[0],l[1])
                    cal.pop(l[0])
        else:
            for l in removal_list:
                if l[1] > average_growth:
                    # print(l[0],l[1])
                    cal.pop(l[0])

        self.__dictOfSET100 = cal

        print(self.__dictOfSET100)
        print(len(self.__dictOfSET100))



