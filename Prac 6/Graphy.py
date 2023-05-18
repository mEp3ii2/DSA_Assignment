import sys
from LinkedList import *
import numpy as np
import StackAndQ as sq
import inSort
import testyboi as tb
class DSAGraph():
    # fields: vertices, edge(DsaLinkedList)
    
    def __init__(self):
        self.vertices = DSALinkedList()
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
        edge = None
        if self.isAdjacent(lab1,lab2) != True:
            print("No edge found")
        else:
            vertex = self.getVertex(lab1)
            edges = vertex.getEdges()
            for i in range(len(edges)):
                if edges[i].getFrom() == lab2:
                    edge = edges[i]
        return edge

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

    def breadFirstSearch(self):
        t = sq.DSAQueue()
        q = sq.DSAQueue()
        self.UnVisit()
        start_Vertex= self.vertices.head.getValue()
        start_Vertex.setVisited(True)
        print("Start Value:",start_Vertex.getLabel())
        q.enqueue(start_Vertex)
        t.enqueue(start_Vertex)
        while q.isEmpty() is not True:
            start_Vertex = q.dequeue()
            adList =start_Vertex.getAdjacent()
            for value in adList:
                neighbor = self.getVertex(value)
                if neighbor.getVisited() == False:
                    neighbor.setVisited(True)
                    q.enqueue(neighbor)
                    t.enqueue(neighbor)
        
        print("bread:")
        while t.isEmpty() is not True:
            print(t.dequeue().getLabel())

    def deepFirstSearch(self):
        t = sq.DSAQueue()
        s = sq.DSAStack()
        self.UnVisit()
        v= self.vertices.head.getValue()
        v.setVisited(True)
        s.push(v)
        t.enqueue(v)
        while s.isEmpty() is not True:
            v = s.peekFirst()
            abList = v.getAdjacent()
            AllVisited = True
            for vertex in abList:
                wTemp = self.getVertex(vertex)
                if wTemp.getVisited() == False:
                    wTemp.setVisited(True)
                    s.push(wTemp)
                    t.enqueue(wTemp)
                    AllVisited = False
                    break
            if AllVisited:
                s.pop()

        print("deep:")
        while t.isEmpty() is not True:
            print(t.dequeue().getLabel())
    
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
        #path = tb.findShortestPath(self,source,dest)
        return path
    def djSearch(self,source,dest):
        queue = sq.DSAQueue()
        path = DSALinkedList()
        self.UnVisit()

        source.setVisited(True)
        queue.enqueue(source)

        while not queue.isEmpty():
            currNode = queue.dequeue()
            path.insertLast(currNode.getLabel())
        
            edges = currNode.getEdges()

            lowWeight = float('inf')
            lowVertex = None

            for edge in edges:
                #if edge.getTo() == dest.getLabel():
                #    path.insertLast(edge.getTo())
                #    return path
                #else:
                if float(edge.getWeight()) < float(lowWeight):
                    lowWeight = edge.getWeight()
                    lowVertex = self.getVertex(edge.getTo())

            if lowVertex.getVisited() == False:
                lowVertex.setVisited(True)
                queue.enqueue(lowVertex)

        self.displayVisitStatus()
        return path

#           Vertex
class DSAGraphNode():
    # fields label,[links], visited
    # edges sole keeper of connections

    def __init__(self,inLabel):
        self.label = inLabel
        self.visited = False
        self.links = DSALinkedList()
        self.count = 0

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

    def __str__(self):
        return f"Vertex {self.label}"
        #Links: {self.links}"

class DSAGraphEdge():

    def __init__(self,fromVertex,toVertex,inWeight):
        self.fVertex = fromVertex
        self.tVertex = toVertex
        self.weight = inWeight

    def getWeight(self):
        return self.weight
    
    def getFrom(self):
        return self.fVertex
    
    def getTo(self):
        return self.tVertex

    def __str__(self):
        return f"From: {self.fVertex} To: {self.tVertex} Distance: {self.weight}"


