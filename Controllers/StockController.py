from Controllers.Connections import *
from Models.StockDetails import *

import pandas as pd

class StockController:

    def __init__(self):
        try:
            self.__dfsList = pd.read_html('https://marketdata.set.or.th/mkt/sectorquotation.do?sector=SET100&language=th&country=TH'
                        , match="เครื่องหมาย" ,encoding='utf8')
            self.__stock = self.__dfsList[0]
            self.__stock.fillna('-', inplace = True)
        except:
            pass
    
    def Intiallize(self):
        c = Connection()
        c.connect()
        return c.message
        
    def StockHeader(self):
        try:
            return tuple(self.__stock.columns)
        except:
            return tuple()
        
    def StockData(self):
        try:
            return self.__stock.values.tolist()
        except:
            return list()

    def __isVaildStock(self, StockDetail):
        if StockDetail.getStockName() != "":
            return True
        return False

    def StockStatement(self, StockDetail):
        if self.__isVaildStock(StockDetail):
            dfstock = pd.read_html('https://www.set.or.th/set/companyhighlight.do?symbol=' + StockDetail.getStockName() + '&language=th&country=TH'
                       , match="งวดงบการเงิน")
            df = dfstock[0]
            df.fillna('-', inplace = True)
            StockDetail.setMessage(f"{StockDetail.getStockName()} : {StockDetail.getCurrentPrice()}")
            return df
        else:
            StockDetail.setMessage("Not Valid StockName")
            return pd.DataFrame()

    def StockStatementHeader(self, StockDetail):
        stockstatement = self.StockStatement(StockDetail)
        listOfColumn = []
        if not stockstatement.empty:
            tp = list(stockstatement.columns)
            for i in tp:
                if "Unnamed" in str(i[0]): 
                    listOfColumn.append(str(i[1]))
                elif "Unnamed" in str(i[1]): 
                    listOfColumn.append(str(i[0]))
                else:
                    listOfColumn.append(str(i[0]) +' '+str(i[1]))
        return listOfColumn

    def StockStatementData(self, StockDetail):
        stockstatement = self.StockStatement(StockDetail)
        if not stockstatement.empty:
            return stockstatement.values.tolist()


    def testcreateusableDF(self,StockDetail):
        data = self.StockStatementData(StockDetail)
        col = self.StockStatementHeader(StockDetail) 
        dfx = pd.DataFrame(data,columns = col)
        print(type(dfx))
        if not dfx.empty:
            modDfObj = dfx.drop([dfx.index[0] , dfx.index[9]])
            print(modDfObj)