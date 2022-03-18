class Financial:

    def __init__(self) -> dict:
        pass

    __Assets = {}
    __Liabilities = {}
    __Equity = {}
    __Capital = {}
    __Revenue = {}
    __Profit_Loss = {}
    __NetProfit = {}
    __EPS = {}
    __ROA = {}
    __ROE = {}
    __Margin = {}
    __LastPrice = {}
    __MarketCap = {}
    __FSPeriod = {}
    __PE = {}
    __PBV = {}
    __BookValuepershare = {}
    __DvdYield = {}

    #Getters
    def getAssets(self):
        return self.__Assets

    def getLiabilities(self):
        return self.__Liabilities

    def getEquity(self):
        return self.__Equity

    def getCapital(self):
        return self.__Capital

    def getRevenue(self):
        return self.__Revenue

    def getProfit_Loss(self):
        return self.__Profit_Loss

    def getNetProfit(self):
        return self.__NetProfit

    def getEPS(self):
        return self.__EPS

    def getROA(self):
        return self.__ROA

    def getROE(self):
        return self.__ROE

    def getMargin(self):
        return self.__Margin

    def getLastPrice(self):
        return self.__LastPrice

    def getMarketCap(self):
        return self.__MarketCap

    def getFSPeriod(self):
        return self.__FSPeriod

    def getEPS(self):
        return self.__PE

    def getPE(self):
        return self.__PBV

    def getBookValuepershare(self):
        return self.__BookValuepershare

    def getDvdYield(self):
        return self.__DvdYield

    #Setters
    def setAssets(self, param):
        self.__Assets = param

    def setLiabilities(self, param):
        self.__Liabilities = param

    def setEquity(self, param):
        self.__Equity = param

    def setCapital(self, param):
        self.__Capital = param

    def setRevenue(self, param):
        self.__Revenue = param

    def getProfit_Loss(self, param):
        self.__Profit_Loss = param

    def setNetProfit(self, param):
        self.__NetProfit = param

    def getEPS(self, param):
        self.__EPS = param

    def getROA(self, param):
        self.__ROA = param

    def getROE(self, param):
        self.__ROE = param

    def getMargin(self, param):
        self.__Margin = param

    def getLastPrice(self, param):
        self.__LastPrice = param

    def getMarketCap(self, param):
        self.__MarketCap = param

    def getFSPeriod(self, param):
        self.__FSPeriod = param

    def getEPS(self, param):
        self.__PE = param

    def getPE(self, param):
        self.__PBV = param

    def getBookValuepershare(self, param):
        self.__BookValuepershare = param

    def getDvdYield(self, param):
        self.__DvdYield = param