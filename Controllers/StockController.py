from Controllers.Connections import *
from Models.StockDetails import *
import pandas as pd
# from datetime import date
# import numpy as np

class StockController:

    def __init__(self):
        pass
    
    def Intiallize(self,StockDetails):
        c = Connection()
        c.connect()
        StockDetails.setMessage(c.message)
        dfsList = pd.read_html('https://marketdata.set.or.th/mkt/sectorquotation.do?sector=SET100&language=th&country=TH'
                       , match="เครื่องหมาย" ,encoding='utf8')
        for col in dfsList.columns:
            print(col)
        
        
