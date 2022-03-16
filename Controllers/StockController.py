from Controllers.Connections import *
from Models.StockDetails import *

import pandas as pd

class StockController:

    def __init__(self):
        self.__dfsList = pd.read_html('https://marketdata.set.or.th/mkt/sectorquotation.do?sector=SET100&language=th&country=TH'
                       , match="เครื่องหมาย" ,encoding='utf8')
        self.__stock = self.__dfsList[0]
    
    def Intiallize(self):
        c = Connection()
        c.connect()
        return c.message
        
    def StockHeader(self):
        return tuple(self.__stock.columns)
        
    def StockData(self):
        return self.__stock.values.tolist()

    def __isVaildStock(self, StockDetail):
        if StockDetail.getStockName() != "":
            return True
        return False

    def StockStatement(self, StockDetail):
        if self.__isVaildStock(StockDetail):
            StockDetail.setMessage(f"{StockDetail.getStockName()} : {StockDetail.getCurrentPrice()}")
        else:
            StockDetail.setMessage("Not Valid StockName")

