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

    ## Substring Technic
    ## https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/
    def StockStatementHeader(self, StockDetail):
        stockstatement = self.StockStatement(StockDetail)
        listOfColumn = []
        if not stockstatement.empty:
            ls = list(stockstatement.columns)
            # print(ls)
            for i in range(len(ls)):
                if i == 0:
                    listOfColumn.append(str(ls[i][1]))
                else:
                    if "Unnamed" in str(ls[i][0]): 
                        listOfColumn.append(str(ls[i][1])[-10:])
                    elif "Unnamed" in str(ls[1]): 
                        listOfColumn.append(str(ls[i][0])[-10:])
                    else:
                        listOfColumn.append(str(ls[i][1])[-10:])
            # print(listOfColumn)
        return listOfColumn

    def StockStatementData(self, StockDetail):
        stockstatement = self.StockStatement(StockDetail)
        if not stockstatement.empty:
            return stockstatement.values.tolist()

    def PrepareDataToAnalyse(self,StockDetail):
        data = self.StockStatementData(StockDetail)
        col = self.StockStatementHeader(StockDetail) 
        dfx = pd.DataFrame(data,columns = col)
        if not dfx.empty:
            modDfObj = dfx.drop([dfx.index[0] , dfx.index[9]])
            return modDfObj