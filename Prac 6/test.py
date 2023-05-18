from Graphy import *
from GraphFileReader import *
from testyboi import *

myGraph = readData()
path = findShortestPath(myGraph,"A","J")
#myGraph.dijkstra('A','J')
path.display()