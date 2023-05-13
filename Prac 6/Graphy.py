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

    def inputHandler(self,label,link):
        try:
            if label.isalpha() is False or link.isalpha() is False:
                raise AttributeError("Invalid input type")
            elif len(label) != 1 or len(link) != 1:
                raise ValueError("Only chars acepted")
        except AttributeError as e:
                print("Only Char character accepted")
        except ValueError as e:
            print("Input should be two chars, check your spacing")
        else:
            self._inputHandler(label,link)
        
    def _inputHandler(self,label,link):
        #check if the label and link already exist or not
        if self.vertices.isEmpty() is False:
            if self.hasVertex(label) is False and self.hasVertex(link) is False:
                self.addVertex(label)
                self.addVertex(link)
                self.addEdge(label,link)
            elif self.hasVertex(label) is True and self.hasVertex(link) is False:
                self.addVertex(link)
                self.addEdge(label,link)
            elif self.hasVertex(label) is False and self.hasVertex(link) is True:
                self.addVertex(label)
                self.addEdge(label, link)
            elif self.hasVertex(label) is True and self.hasVertex(link) is True:
                # TODO put a check to make sure there isnt already a edge
                self.addEdge(label,link)
        else:
            self.addVertex(label)
            self.addVertex(link)  
            self.addEdge(label,link)

    def addVertex(self,label):
        node = DSAGraphNode(label)
        self.vertices.insertLast(node)
        self.vertCount +=1

    def addEdge(self,lab1,lab2):
        node1 = self.getVertex(lab1)
        node2 = self.getVertex(lab2)
        node1.addEdge(node2)
        node2.addEdge(node1)
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
    
    #redo
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
        
        #vertice = self.vertices.findNode(lab)
        #return vertice

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
            testVals[count] = value.getLabel()
            count +=1
        testVals = inSort.insertionSort(testVals)
        return testVals
    
    def addEdge(self,vertex):
        self.links.insertLast(vertex)
        self.count +=1

    def setVisited(self,visit):
        self.visited = visit

    def getVisited(self):
        return self.visited

    def __str__(self):
        print("Vertex",self.label,"Links:",self.links)




