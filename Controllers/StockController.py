from turtle import st
from unicodedata import name
from Controllers.Connections import *
from Models.StockDetails import *

import pandas as pd

class StockController:
    # https://marketdata.set.or.th/mkt/sectorquotation.do?market=SET&sector=ICT&language=th&country=TH
    # https://www.set.or.th/set/commonslookup.do?language=th&country=TH&prefix=NUMBER
    def __init__(self):
        try:
            self.__dfsList = pd.read_html('https://marketdata.set.or.th/mkt/sectorquotation.do?sector=SET100&language=th&country=TH'
                        , match="เครื่องหมาย" ,encoding='utf8')
            self.__stock = self.__dfsList[0]
            # self.__stock.fillna('-', inplace = True)
            # https://datatofish.com/convert-string-to-float-dataframe/
            # df['DataFrame Column'] = pd.to_numeric(df['DataFrame Column'],errors='coerce')
            self.__stock['เครื่องหมาย'].fillna('-', inplace = True)

            self.__stock['ปริมาณ(หุ้น)'] = pd.to_numeric(self.__stock['ปริมาณ(หุ้น)'],errors='ignore')
            self.__stock['ปริมาณ(หุ้น)'] = self.__stock['ปริมาณ(หุ้น)'].map('{:,.2f}'.format)

            self.__stock["มูลค่า('000 บาท)"] = pd.to_numeric(self.__stock["มูลค่า('000 บาท)"],errors='ignore')
            self.__stock["มูลค่า('000 บาท)"] = self.__stock["มูลค่า('000 บาท)"].map('{:,.2f}'.format)
            # print(self.__stock.head())
        except:
            pass
            
        # df = pd.read_html('https://www.set.or.th/set/commonslookup.do?language=th&country=TH&prefix=NUMBER'
        #                 , match="ชื่อย่อหลักทรัพย์" ,encoding='utf8')
        # print(df[0])

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

    def isVaildStock(self, StockDetail):
        if StockDetail.getStockName() != "":
            return True
        return False

    def StockStatement(self, StockDetail) -> pd.DataFrame:
        if self.isVaildStock(StockDetail):
            dfstock = pd.read_html('https://www.set.or.th/set/companyhighlight.do?symbol=' + StockDetail.getStockName() + '&language=th&country=TH'
                       , match="งวดงบการเงิน")
            df = dfstock[0]
            df.fillna('-', inplace = True)
            df.Name = StockDetail.getStockName()
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
            df.Name = x
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
                    listOfColumn.append(df.Name)
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
            stockstatement
            return stockstatement.values.tolist()
        return list()

    async def getSET100Name(self) -> list:
        if not self.__stock.empty:
            StkList = self.__stock['หลักทรัพย์'].to_list()
            return StkList


    async def StockStatementDataFrame(self, x) -> pd.DataFrame:
        if len(x) > 0:
            dfstock = pd.read_html('https://www.set.or.th/set/companyhighlight.do?symbol=' + x + '&language=th&country=TH'
                       , match="งวดงบการเงิน")
            df = dfstock[0]
            df.fillna('-', inplace = True)
            df.Name = x
            return df
        return pd.DataFrame()

    # https://towardsdatascience.com/a-gentle-introduction-to-flow-control-loops-and-list-comprehensions-for-beginners-3dbaabd7cd8a
    # [output if condition else output for l in list]
    async def PrepareDataToAnalyse(self,df):
        data = self.StockStatementData(df)
        col = self.StockStatementHeader(df)
        col_result  = [col[0] if i==0 else col[i][-2:] for i in range(len(col))]
        dfx = pd.DataFrame(data,columns = col_result)
        if not dfx.empty:
            modDfObj = dfx.drop([dfx.index[0] , dfx.index[9]])
            modDfObj.Name = col_result[0]
            return modDfObj
        return pd.DataFrame()

    def growthStock(self,df):
        pass