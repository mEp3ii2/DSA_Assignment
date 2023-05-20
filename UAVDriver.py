from  UAV import *
from Graphy import *
from GraphFileReader import *
from DSAHashTable import *
from DSAHeap import *
import StackAndQ as sq

myUav = UAV()

graph = readData()
count = graph.getVertexCount()

hash = DSAHashTable(count)
hash.importFile()

heap = DSAHeap(count)
vertexes = graph.deepFirstSearch()

while vertexes.isEmpty() is not True:
    lab = vertexes.dequeue().getLabel()
    vert = hash.get(lab)
    risk = myUav.riskLvlCalc(vert)
    heap.add(risk,lab)
heap.display()