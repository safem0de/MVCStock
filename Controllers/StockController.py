from Controllers.Connections import *
from Models.StockDetails import *

import pandas as pd
import asyncio

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

    def StockStatement(self, StockDetail) -> pd.DataFrame:
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

    def StockStatementDataFrame(self, x) -> pd.DataFrame:
        if len(x) > 0:
            dfstock = pd.read_html('https://www.set.or.th/set/companyhighlight.do?symbol=' + x + '&language=th&country=TH'
                       , match="งวดงบการเงิน")
            df = dfstock[0]
            df.fillna('-', inplace = True)
            return df
        return pd.DataFrame()

    ## Substring Technic
    ## https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/
    def StockStatementHeader(self, df) -> list:
        # stockstatement = self.StockStatement(StockDetail)
        stockstatement = df
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

    def StockStatementData(self, df) -> list:
        # stockstatement = self.StockStatement(StockDetail)
        stockstatement = df
        if not stockstatement.empty:
            return stockstatement.values.tolist()
        return list()

    def getSET100Name(self) -> list:
        if not self.__stock.empty:
            StkList = self.__stock['หลักทรัพย์'].to_list()
            return StkList

    # https://towardsdatascience.com/a-gentle-introduction-to-flow-control-loops-and-list-comprehensions-for-beginners-3dbaabd7cd8a
    # [output if condition else output for l in list]
    def PrepareDataToAnalyse(self,df):
        # data = self.StockStatementData(StockDetail)8
        # col = self.StockStatementHeader(StockDetail)
        data = self.StockStatementData(df)
        col = self.StockStatementHeader(df)
        result  = [col[i] if i==0 else col[i][-2:] for i in range(len(col))]
        dfx = pd.DataFrame(data,columns = result)
        if not dfx.empty:
            modDfObj = dfx.drop([dfx.index[0] , dfx.index[9]])
            return modDfObj
        return pd.DataFrame()

    def growthStock(self,df):
        pass