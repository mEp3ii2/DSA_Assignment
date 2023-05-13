class DSAHashEntry():
    #field str
    #value obj
    #state int

    def __init__(self,key = None, value = None):
        self.key = key
        self.value = value
        self.state = 0

        if key is not None and value is not None:
            self.state = 1

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value

    def getState(self):
        return self.state
    
    def setState(self,state):
        self.state = state
    
    def setKey(self,inKey):
        self.key = inKey
    
    def setValue(self,inValue):
        self.value = inValue

    