from Graphy import *
from GraphFileReader import *
from testyboi import *

myGraph = readData()

myGraph.displayWeightAsMatrix()

#path = findShortestPath(myGraph,"A","J")
path =myGraph.dijkstra('A','H')
#J = myGraph.getVertex('J')
#print("Previous: "+str(J.getPrevious()))
path.display()