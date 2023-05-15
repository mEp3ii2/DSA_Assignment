from LinkedList import *
import numpy as np
import StackAndQ as sq
import inSort

class DSAGraph():
    # fields: vertices, edge(DsaLinkedList)
    
    def __init__(self):
        self.vertices = DSALinkedList()
        self.vertCount = 0
        self.edgeCount = 0

    # process the inout before handing over
    def inputHandler(self,label,link,weight):
        try:
            if label.isalpha() is False or link.isalpha() is False:
                raise AttributeError("Invalid input type")
            elif len(label) != 1 or len(link) != 1:
                raise ValueError("Only chars acepted for vertxes")
            weight = float(weight)
            if weight <= 0:
                raise ValueError("Edge weight must a positive number")
        except AttributeError as e:
                print("Only Char character accepted")
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
                if edges[i].getTo() == lab2:
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
        myIter = iter(self.vertices)
        value = next(myIter)
        for value in self.vertices:
            if value is not None:
                value.setVisited(False)
        v= self.vertices.head.getValue()
        v.setVisited(True)
        print("Start Value:",v.getLabel())
        q.enqueue(v)
        t.enqueue(v)
        while q.isEmpty() is not True:
            v = q.dequeue()
            adList =v.getAdjacent()
            for value in adList:
                w = self.getVertex(value)
                if w.getVisited() == False:
                    w.setVisited(True)
                    q.enqueue(w)
                    t.enqueue(w)
        
        print("bread:")
        while t.isEmpty() is not True:
            print(t.dequeue().getLabel())

    def deepFirstSearch(self):
        t = sq.DSAQueue()
        s = sq.DSAStack()
        myIter = iter(self.vertices)
        value = next(myIter)
        for value in self.vertices:
                value.setVisited(False)
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

    # goes through vertext list and removes 
    # vertex from graph
    def removeVertex(self,lab):
        label = lab
        lab = self.getVertex(lab)
        currNode = self.vertices.head
        nodeFound = False
        while currNode is not None and nodeFound == False:
            if currNode.getValue() == lab:
                if currNode.getPrev() is None:
                    self.vertices.removeFirst()
                elif currNode.getNext() is None:
                    self.vertices.removeLast()
                    self.updateAdjacencies(label)
                else:
                    currNode.getPrev().setNext(currNode.getNext())
                    currNode.getNext().setPrev(currNode.getPrev())
                self.updateAdjacencies(label)
                nodeFound = True
            currNode = currNode.getNext()
    
    #updates adjacency lists of all vertexes
    def updateAdjacencies(self,lab):
        currNode = self.vertices.head
        while currNode is not None:
            vertex =currNode.getValue()
            vertex.updateEdges(lab)
            currNode = currNode.getNext()
        

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
        testVals = inSort.insertionSort(testVals)
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

    def updateEdges(self,lab):
        currNode = self.links.head
        deleted = False
        while currNode is not None and deleted == False:
            if currNode.getValue().getTo() == lab:
                if currNode.getPrev() is None:
                    self.links.removeFirst()
                elif currNode.getNext() is None:
                    self.links.removeLast()
                else:
                    currNode.getPrev().setNext(currNode.getNext())
                    currNode.getNext().setPrev(currNode.getPrev())
                deleted  = True
                self.count -=1
            currNode = currNode.getNext()
        

    def __str__(self):
        return f"Vertex {self.label} Links: {self.links}"

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


