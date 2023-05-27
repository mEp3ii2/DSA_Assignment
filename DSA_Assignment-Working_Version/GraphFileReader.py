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
    
def writeData(graph):
    try:
        with open("locations.txt","w") as dataFile:
            myIter = iter(graph.edges)
            value = next(myIter)
            for value in graph.edges:
                if value is not None:
                    fromVert = value.getFrom()
                    toVert = value.getTo()
                    weight = value.getWeight()
                    dataFile.write(fromVert+" "+toVert+" "+str(weight)+"\n")
    except IOError as e:
        print("Error in saving file: "+str(e)+"\n")
    else:
        print("Data has been saved!\n")