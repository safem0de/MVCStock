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

    def __isValid_SET100_dict(self,__dictOfSET100):
        return bool(__dictOfSET100)

    async def DataframeToModel(self,df):
        cleanDatas = {}
        for row_index,row in df.iterrows():
            m = pd.to_numeric(row[1:], errors='ignore')
            cleanDatas[row[0]] = m.to_dict()
        return cleanDatas

    async def setAllData(self,i,data):
        __dictOfSET100 = {}
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
        __dictOfSET100[i] = analyseModel
        return __dictOfSET100

    def calculateGrowth(self, financials):
        financials = self.__dictOfSET100.get("ACE")
        print(financials.getAssets())


        

    

    