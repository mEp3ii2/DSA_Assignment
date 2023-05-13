from Graphy import *

def readData():
    graph = DSAGraph()
    try:
        with open("prac6_1.al","r") as dataFile:
            for line in dataFile:
                chars = line.strip().split()
                graph.inputHandler(chars[0],chars[1])
    except IOError as e:
        print("Error in file processing: "+str(e))
    else:
        return graph

myGraph = readData()
myGraph.displayAsList()
myGraph.displayAsMatrix()
myGraph.breadFirstSearch()
myGraph.deepFirstSearch()