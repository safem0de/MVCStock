from calendar import c
from statistics import mean

from Views.Analyse import *
from Models.AnalyseDetails import *

class AnalysisData:

    __caculatedSET100 = []
    __current_List = []
    __accumulated_List = []
    __filterDict = {}

    def __init__(self,allData):
        self.__dictOfSET100 = allData

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

        self.__caculatedSET100 = cal

    def InitialTable(self,financials):
        self.deleteMinusProfit(financials)
        TblList = []
        for c in self.__caculatedSET100:
            financials = self.__caculatedSET100.get(c)

            assets = financials.getAssets()
            revenues = financials.getRevenue()
            netprofits = financials.getNetProfit()
            roes = financials.getROE()

            TblList.append([c,
                3 if len(self.makeYear_Growth(assets)) >= 3 else len(self.makeYear_Growth(assets)),
                self.calculateIndiviaual_Growth(assets),
                self.calculateIndiviaual_Growth(revenues),
                self.calculateIndiviaual_Growth(netprofits),
                self.calculateIndiviaual_Growth(roes)
            ])

        return TblList


    # https://realpython.com/iterate-through-dictionary-python/
    # https://www.w3schools.com/python/python_dictionaries_access.asp
    # def calculateGrowth(self, financials, datatype):
    #     all_average_growth = []
    #     removal_list = []
    #     average_growth = 0
    #     more_is_good = True
    #     cal = self.__caculatedSET100
    #     for c in cal:
    #         financials = cal.get(c)
    #         if datatype == "asset":
    #             growthtype = financials.getAssets()
    #         elif datatype == "revenue":
    #             growthtype = financials.getRevenue()
    #         elif datatype == "netprofit":
    #             growthtype = financials.getNetProfit()
    #         elif datatype == "roe":
    #             growthtype = financials.getROE()

    #         year = []
    #         asset = []
    #         for key in sorted(growthtype, reverse=True):
    #             if not growthtype[key] == "-":
    #                 year.append(int(key))
    #                 asset.append(float(growthtype[key]))

    #         year_asset = list(zip(year,asset))
    #         res_growth = []
    #         for i in range(len(year_asset)):
                
    #             if i+1 < len(year_asset):
    #                 # print(f"((สินทรัพย์ปี {year_asset[i][0]} - สินทรัพย์ปี {year_asset[i+1][0]})/ สินทรัพย์ปี {year_asset[i+1][0]})*100")
    #                 # print("อัตราการเติบโตของทรัพย์สิน (ต่อปี)")
    #                 x = ((year_asset[i][1]-year_asset[i+1][1])/year_asset[i+1][1])*100
    #                 if len(res_growth) < 3:
    #                     res_growth.append(round(x,3))

    #         # print(c)
    #         # print(res_growth)
    #         all_average_growth.append(round(sum(res_growth)/len(res_growth),3))
    #         removal_list.append([c,round(sum(res_growth)/len(res_growth),3)])
            
    #     average_growth = round(sum(all_average_growth)/len(all_average_growth),3)
    #     print(datatype, average_growth)

    #     if more_is_good:
    #         for l in removal_list:
    #             if l[1] < average_growth:
    #                 # print(l[0],l[1])
    #                 cal.pop(l[0])
    #     else:
    #         for l in removal_list:
    #             if l[1] > average_growth:
    #                 # print(l[0],l[1])
    #                 cal.pop(l[0])

    #     self.__caculatedSET100 = cal

    #     print(self.__caculatedSET100)
    #     print(len(self.__caculatedSET100))

    def makeYear_Growth(self,growthtype) -> list[tuple]:
        year = []
        valueOfGrowth = []
        for key in sorted(growthtype, reverse=True):
            if not growthtype[key] == "-":
                year.append(int(key))
                valueOfGrowth.append(float(growthtype[key]))

        year_growth = list(zip(year,valueOfGrowth))
        return year_growth

    def calculateGrowth(self,growthtype) -> list:
        year_growth = self.makeYear_Growth(growthtype)
        res_growth = []
        for i in range(len(year_growth)):
            if i+1 < len(year_growth):
            # print(f"((สินทรัพย์ปี {year_asset[i][0]} - สินทรัพย์ปี {year_asset[i+1][0]})/ สินทรัพย์ปี {year_asset[i+1][0]})*100")
            # print("อัตราการเติบโตของทรัพย์สิน (ต่อปี)")
                x = ((year_growth[i][1]-year_growth[i+1][1])/year_growth[i+1][1])*100
                if len(res_growth) < 3:
                    res_growth.append(round(x,3))

        return res_growth

    def calculateIndiviaual_Growth(self,growthtype):
        return round(mean(self.calculateGrowth(growthtype)),3)

    def calculateMean_Growth(self,financials,datatype):
        self.deleteMinusProfit(financials)
        all_average_growth = []
        average_growth = -1
        x = None
        for c in self.__caculatedSET100:
            financials = self.__caculatedSET100.get(c)

            if datatype == "asset":
                x = financials.getAssets()
            elif datatype == "revenue":
                x = financials.getRevenue()
            elif datatype == "netprofit":
                x = financials.getNetProfit()
            elif datatype == "roe":
                x = financials.getROE()
            else:
                return
            
            all_average_growth.append(self.calculateGrowth(x))
        
        average_growth = mean([mean(l) for l in all_average_growth])
        return round(average_growth,3)
        

    def clickEvents(self,financials,filterList):
        self.__filterDict = {filterList[i]: [0,0] for i in range(len(filterList))}
        for k in self.__filterDict:
            if k == 'asset':
                self.__filterDict[k][0] = 2
                self.__filterDict[k][1] = self.calculateMean_Growth(financials,k)
            if k == 'revenue':
                self.__filterDict[k][0] = 3
                self.__filterDict[k][1] = self.calculateMean_Growth(financials,k)
        print(self.__filterDict)
        self.__current_List = self.InitialTable(financials)

    def filter_recursive(self):
        self.__filterList
        self.__current_List
        self.__accumulated_List
        # Base case
        if len(self.__filterList) == 0:
            return self.__current_List
        # Recursive case
        else:
            for j in self.__filterList:
                for k in self.__current_List:
                    # if k[j] < calculateMean_Growth(financials)
                    pass
                
            # accumulated_sum = accumulated_sum + current_number
            # current_number = current_number + 1
            return self.filter_recursive()
        