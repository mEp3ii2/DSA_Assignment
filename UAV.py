from Graphy import *
from GraphFileReader import *
from DSAHashTable import *
from DSAHeap import *

class UAV():
    id = 0
    def __init__(self):
        UAV.id +=1
        self.id = UAV.id

    def riskLvlCalc(self,locationData):
        riskLevel = 0
        
        temp = locationData.getTemp()
        humidity = locationData.getHumidity()
        wind = locationData.getWind()

        if temp <= 32:
            riskLevel += 1
        elif 33<=temp>=40:
            riskLevel += 2
        elif temp >=41:
            riskLevel += 3

        if humidity >= 50:
            riskLevel += 1
        elif 31<=humidity>=49:
            riskLevel += 2
        elif humidity <= 30:
            riskLevel += 3
         
        if wind <= 40:
            riskLevel += 1
        elif 41<=temp>=55:
            riskLevel += 2
        elif temp >=56:
            riskLevel += 3

        return riskLevel