from tkinter import Toplevel
from Views.Analyse import *
from Models.AnalyseDetails import *

import pandas as pd

class AnalyseContoller:

    __dictOfSET100 = {}

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
    def calculateGrowth(self, financials):
        cal = self.__dictOfSET100
        for c in cal:
            financials = cal.get(c)
            growthAsset = financials.getAssets()
            print(c)
            # x = [int(key) for key in sorted(growthAsset, reverse=True) if not growthAsset[key] == "-"]
            # y = [float(growthAsset[key]) for key in sorted(growthAsset, reverse=True) if not growthAsset[key] == "-"]
            # print(x,y)
            year = []
            asset = []
            for key in sorted(growthAsset, reverse=True):
                if not growthAsset[key] == "-":
                    # year_asset[int(key)] = float(growthAsset[key])
                    year.append(int(key))
                    asset.append(float(growthAsset[key]))

            year_asset = list(zip(year,asset))
            # print(year_asset)
            res_growth = []
            for i in range(len(year_asset)):
                if i+1 < len(year_asset):
                    print(f"((สินทรัพย์ปี {year_asset[i][0]} - สินทรัพย์ปี {year_asset[i+1][0]})/ สินทรัพย์ปี {year_asset[i+1][0]})*100")
                    print("อัตราการเติบโตของทรัพย์สิน (ต่อปี)")
                    x = ((year_asset[i][1]-year_asset[i+1][1])/year_asset[i+1][1])*100
                    if len(res_growth) < 3:
                        res_growth.append(x)
            
            print(int(sum(res_growth)/len(res_growth)))

