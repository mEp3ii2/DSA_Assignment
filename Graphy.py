import sys
from LinkedList import *
import numpy as np
import StackAndQ as sq
import inSort
import testyboi as tb
from DSAMinHeap import *

class DSAGraph():
    # fields: vertices, edge(DsaLinkedList)
    
    def __init__(self):
        self.vertices = DSALinkedList()
        self.edges = DSALinkedList()
        self.vertCount = 0
        self.edgeCount = 0
    
    def getertexCount(self):
        return self.vertCount
    
    def floatChecker(self,temp):
        try:
            float(temp)
            return True
        except ValueError:
            return False

    # process the inout before handing over
    def inputHandler(self,label,link,weight):
        try:
            if label.isalpha() is False or link.isalpha() is False:
                raise AttributeError("Invalid input type")
            elif len(label) != 1 or len(link) != 1:
                raise ValueError("Only chars acepted for vertxes")
            if self.floatChecker(weight) == True:
                weight = float(weight)
            else:
                raise ValueError("Only float values accepted for weight")
            if weight <= 0:
                raise ValueError("Edge weight must a positive number")
        except AttributeError as e:
                print("Only Char character accepted for vertexes")
        except ValueError as e:
            print("Invalid input detected: "+str(e))
        else:
            self._inputHandler(label,link,weight)
        
    def _inputHandler(self,label,link,weight):
        #check if the label and link already exist or not
        if self.vertices.isEmpty() is False:
            if self.hasVertex(label) is False and self.hasVertex(link) is False:
                self.addVertex(label)
                self.addVertex(link)
                self.addEdge(label,link,weight)
            elif self.hasVertex(label) is True and self.hasVertex(link) is False:
                self.addVertex(link)
                self.addEdge(label,link,weight)
            elif self.hasVertex(label) is False and self.hasVertex(link) is True:
                self.addVertex(label)
                self.addEdge(label, link,weight)
            elif self.hasVertex(label) is True and self.hasVertex(link) is True:
                # TODO put a check to make sure there isnt already a edge
                self.addEdge(label,link,weight)
        else:
            self.addVertex(label)
            self.addVertex(link)  
            self.addEdge(label,link,weight)

    def addVertex(self,label):
        node = DSAGraphNode(label)
        self.vertices.insertLast(node)
        self.vertCount +=1

    def addEdge(self,lab1,lab2,weight):
        node1 = self.getVertex(lab1)
        node2 = self.getVertex(lab2)
        edge1 = DSAGraphEdge(lab1,lab2,weight)
        edge2 = DSAGraphEdge(lab2,lab1,weight)
        node1.addEdge(edge1)
        node2.addEdge(edge2)
        self.edges.insertLast(edge1)
        self.edges.insertLast(edge2)
        
        self.edgeCount +=1
    
    def hasVertex(self,lab):
        exists = False
        node = None
        myIter = iter(self.vertices)
        value = next(myIter)
        for value in self.vertices:
            if value is not None:
                if value.getLabel() == lab:
                    node = value
        if node is not None:
            exists = True
        return exists
    
    def getVertexCount(self):
        return self.vertCount

    def getEdgeCount(self):
        return self.edgeCount
    
    def getVertex(self,lab):
        vertex = None
        myIter = iter(self.vertices)
        value = next(myIter)
        for value in self.vertices:
            if value is not None:
                if value.getLabel() == lab:
                    vertex = value
        if vertex is not None:
            return vertex
        else:
            print("Node not found")
    
    def getVertexByCount(self, count):
        vertex = self.vertices.head
        index = 0
        while vertex is not None:
            if index == count:
                return vertex.getLabel()
            index+=1
            vertex = vertex.getNext()
        return None 
    
    def getAdjacent(self,label):
        vertex = self.getVertex(label)
        return vertex.getAdjacent()

    def isAdjacent(self,lab1,lab2):
        adBool = False
        vertex = self.getVertex(lab1)
        adList = vertex.getAdjacent()
        for value in adList:
            if lab2 == value:
                adBool = True
        return adBool
    
    def getEdge(self,lab1,lab2):
        edgeObj = None
        if self.isAdjacent(lab1,lab2) != True:
            print("No edge found")
        else:
            vertex = self.getVertex(lab1)
            edges = vertex.getEdges()
            for i in range(len(edges)):
                if edges[i].getTo() == lab2:
                    edgeObj = edges[i]
        return edgeObj

    def displayAsList(self):
        myIter = iter(self.vertices)
        value = next(myIter)
        for value in self.vertices:
            if value is not None:
                label = value.getLabel()
                adList = value.getAdjacent()
                print(label,":",adList)
    
    def displayVisitStatus(self):
        myIter = iter(self.vertices)
        value = next(myIter)
        for value in self.vertices:
            if value is not None:
                label = value.getLabel()
                visit = value.getVisited()
                print(label,":",visit)

    def displayAsMatrix(self):
        x = self.vertCount
        arr = np.zeros((x,x))
        myIter = iter(self.vertices)
        value = next(myIter)
        count = 0
        for value in self.vertices:
            if value is not None:
                adList = value.getAdjacent()
                for vert in adList:
                    pos = ord(vert) - 65 # get pos in alphabet
                    arr[count][pos] = 1
            count +=1
        for i in range(len(arr)):
            for j in range(len(arr)):
                print(int(arr[i][j]),end= ' ')
            print()
    
    def displayWeightAsMatrix(self):
        x = self.vertCount
        arr = np.zeros((x,x),dtype=float)
        myIter = iter(self.vertices)
        value = next(myIter)
        count = 0
        for value in self.vertices:
            if value is not None:
                edgeList = value.getEdges()
                for edge in edgeList:
                    pos = ord(edge.getTo()) - 65 # get pos in alphabet
                    arr[count][pos] = float(edge.getWeight())
            count +=1
        for i in range(len(arr)):
            for j in range(len(arr)):
                print((arr[i][j]),end= ' ')
            print()

    def UnVisit(self):
        for vertex in self.vertices:
            vertex.setVisited(False)
        #myIter = iter(self.vertices)
        #value = next(myIter)
        #for value in self.vertices:
        #        value.setVisited(False)
    
    def dijkstra(self, source, dest):
            source = self.getVertex(source)
            dest = self.getVertex(dest)
            self.UnVisit()
            path = self.djSearch(source,dest)
            return path

    def djSearch(self,source,dest):
        #queue = sq.DSAQueue()
        path = DSALinkedList()
        for vertex in self.vertices:
                if vertex != source:
                    vertex.setDistance(float('inf'))
                else:
                    vertex.setDistance(0)

        currNode = source
        currNode.setVisited(True)
        path.insertFirst(currNode)

        while True:
            edges = currNode.getEdges()
            minDistance = float('inf')
            nextNode = None

            # Find the unvisited neighbor with the minimum distance
            for edge in edges:
                vert = self.getVertex(edge.getTo())
                if not vert.getVisited():
                    distance = currNode.getDistance() + edge.getWeight()
                    if distance < vert.getDistance():
                        vert.setDistance(distance)
                        vert.setPrevious(currNode)
                        path.insertLast((edge.getTo(), distance))
                    if vert.getDistance() < minDistance:
                        minDistance = vert.getDistance()
                        nextNode = vert

            if nextNode is None:
                break

            currNode = nextNode
            currNode.setVisited(True)

    # Build the shortest path from the destination to the source
        shortestPath = DSALinkedList()
        curr = dest
        while curr is not None:
            shortestPath.insertFirst((curr.getLabel(), curr.getDistance()))
            curr = curr.getPrevious()

        return shortestPath

#           Vertex
class DSAGraphNode():
    # fields label,[links], visited
    # edges sole keeper of connections

    def __init__(self,inLabel):
        self.label = inLabel
        self.visited = False
        self.links = DSALinkedList()
        self.count = 0
        self.distance = float('inf')
        self.previous = None
        self.next = None
    
    def getLabel(self):
        return self.label

    def getAdjacent(self):
        testVals = np.empty(self.count,dtype=object)
        myIter = iter(self.links)
        value = next(myIter)
        count = 0
        for value in self.links:
            testVals[count] = value.getTo()
            count +=1
        #testVals = inSort.insertionSort(testVals)
        return testVals
    
    def getEdges(self):
        testVals = np.empty(self.count,dtype=object)
        myIter = iter(self.links)
        value = next(myIter)
        count = 0
        for value in self.links:
            testVals[count] = value
            count +=1
        #testVals = inSort.insertionSort(testVals)    
        return testVals
    
    def addEdge(self,vertex):
        self.links.insertLast(vertex)
        self.count +=1

    def setVisited(self,visit):
        self.visited = visit

    def getVisited(self):
        return self.visited
    
    def setDistance(self,distance):
        self.distance = distance

    def getDistance(self):
        return self.distance
    
    def setPrevious(self,previous):
        self.previous = previous
    
    def getPrevious(self):
        return self.previous
    
    def getNext(self):
        return self.next
    
    def setNext(self,next):
        self.next = next

    def __str__(self):
        return f"Vertex {self.label}"
        #Links: {self.links}"

class DSAGraphEdge():

    def __init__(self,fromVertex,toVertex,inWeight):
        self.fVertex = fromVertex
        self.tVertex = toVertex
        self.weight = float(inWeight)

    def getWeight(self):
        return self.weight
    
    def getFrom(self):
        return self.fVertex
    
    def getTo(self):
        return self.tVertex

    def __str__(self):
        return f"From: {self.fVertex} To: {self.tVertex} Distance: {self.weight}"


