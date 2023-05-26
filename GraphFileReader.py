from Graphy import *

def readData():
    graph = DSAGraph()
    try:
        with open("location.txt","r") as dataFile:
            for line in dataFile:
                chars = line.strip().split()
                if len(chars)==3:
                    graph.inputHandler(chars[0],chars[1], float(chars[2]))
    except IOError as e:
        print("Error in file processing: "+str(e))
    else:
        return graph