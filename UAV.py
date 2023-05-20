from Graphy import *
from GraphFileReader import *
from DSAHashTable import *
from DSAHeap import *

class UAV():
    id = int(0)
    def __init__(self,location = None):
        self.id = UAV.id
        UAV.id +=1
        self.location = location
    
    def getID(self):
        return self.id
    
    def getLocation(self):
        return self.location
    
    def setLocation(self,location):
        self.location = location