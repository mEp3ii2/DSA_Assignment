from Prac_6.Graphy import *
from Prac_7.DSAHashTable import *
from Prac_8.DSAHeap import *
from Prac_6.GraphFileReader import *
from Prac_7.LocationInfo import *
from Prac_8.DSAHeapEntry import *


class DSAUAV():

    def __init__(self,graph,hash,heap):
        self.graph = readData()
        count = self.graph.vertCount
        self.hash = DSAHashTable(count)
        self.hash.importFile()
        self.heap = DSAHeap(count)

    def uploadUAVData(self):
        
    def riskLvlCalc(self,location):
        riskLevel = 0
        
        locationData = self.hash.get(location).getValue()
        temp = locationData.getTemp()
        humidity = locationData.getHumidity()
        wind = locationData.getWind()

        if temp <= 32:
            riskLevel += 1
        elif 33<=temp>=40:
            riskLevel += 2
        elif temp =>41:
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
        elif temp =>56:
            riskLevel += 3

        return riskLevel
