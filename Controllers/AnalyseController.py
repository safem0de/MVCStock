from Views.Analyse import *
from Models.AnalyseDetails import *

class AnalysisData:

    __caculatedSET100 = {}

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
        return self.__caculatedSET100
        # print(self.__caculatedSET100)


    # https://realpython.com/iterate-through-dictionary-python/
    # https://www.w3schools.com/python/python_dictionaries_access.asp
    def calculateGrowth(self, financials, datatype):
        all_average_growth = []
        removal_list = []
        average_growth = 0
        more_is_good = True
        cal = self.__caculatedSET100
        for c in cal:
            financials = cal.get(c)
            if datatype == "asset":
                growthtype = financials.getAssets()
            elif datatype == "revenue":
                growthtype = financials.getRevenue()
            elif datatype == "netprofit":
                growthtype = financials.getNetProfit()
            elif datatype == "roe":
                growthtype = financials.getROE()
            else:
                pass

            year = []
            asset = []
            for key in sorted(growthtype, reverse=True):
                if not growthtype[key] == "-":
                    year.append(int(key))
                    asset.append(float(growthtype[key]))

            year_asset = list(zip(year,asset))
            res_growth = []
            for i in range(len(year_asset)):
                
                if i+1 < len(year_asset):
                    # print(f"((สินทรัพย์ปี {year_asset[i][0]} - สินทรัพย์ปี {year_asset[i+1][0]})/ สินทรัพย์ปี {year_asset[i+1][0]})*100")
                    # print("อัตราการเติบโตของทรัพย์สิน (ต่อปี)")
                    x = ((year_asset[i][1]-year_asset[i+1][1])/year_asset[i+1][1])*100
                    if len(res_growth) < 3:
                        res_growth.append(round(x,3))

            # print(c)
            # print(res_growth)
            all_average_growth.append(round(sum(res_growth)/len(res_growth),3))
            removal_list.append([c,round(sum(res_growth)/len(res_growth),3)])
            
        average_growth = round(sum(all_average_growth)/len(all_average_growth),3)
        print(datatype, average_growth)

        if more_is_good:
            for l in removal_list:
                if l[1] < average_growth:
                    # print(l[0],l[1])
                    cal.pop(l[0])
        else:
            for l in removal_list:
                if l[1] > average_growth:
                    # print(l[0],l[1])
                    cal.pop(l[0])

        self.__caculatedSET100 = cal

        print(self.__caculatedSET100)
        print(len(self.__caculatedSET100))