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
            dfstock = pd.read_html('https://www.set.or.th/set/companyhighlight.do?symbol=' + StockDetail.getStockName() + '&language=th&country=TH'
                       , match="งวดงบการเงิน")
            df = dfstock[0]
            StockDetail.setMessage(f"{StockDetail.getStockName()} : {StockDetail.getCurrentPrice()}")
            # print(type(df))
            return df
        else:
            StockDetail.setMessage("Not Valid StockName")
            return pd.DataFrame()

    def StockStatementHeader(self, StockDetail):
        stockstatement = self.StockStatement(StockDetail)
        listOfColumn = []
        # print(tuple(stockstatement.columns))
        # print(type(stockstatement))
        if not stockstatement.empty:
            tp = list(stockstatement)
            for i in tp:
                if "Unnamed" in str(i[0]): 
                    listOfColumn.append(str(i[1]))
                elif "Unnamed" in str(i[1]): 
                    listOfColumn.append(str(i[0]))
                else:
                    listOfColumn.append(str(i[0]) +' '+str(i[1]))
            # print(listOfColumn)
        return listOfColumn

    def StockStatementData(self, StockDetail):
        stockstatement = self.StockStatement(StockDetail)
        if not stockstatement.empty:
            print(stockstatement.values.tolist())
            return stockstatement.values.tolist()


