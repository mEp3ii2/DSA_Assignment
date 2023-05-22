#LinkedList.py
#Linked list class file
#Mitchell Pontague
#19126924
#DSA SEM 1 2023

from Graphy import *

class DSALinkedList():
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        self._cur = self.head
        return self
    
    def __next__(self):
        curVal = None
        if self._cur == None:
            raise StopIteration
        else:
            curVal = self._cur.getValue()
            self._cur = self._cur.getNext()
        return curVal
        
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def insertFirst(self,value):
        newNd = DSAListNode(value)
        if self.isEmpty():
            self.head = newNd
            self.tail = newNd
        else:
            self.head.setPrev(newNd)
            newNd.setNext(self.head)
            self.head = newNd
            

    def insertLast(self,value):
        newNd = DSAListNode(value)
        if self.isEmpty():
            self.head = newNd
            self.tail = newNd
        elif self.tail != None:
            newNd.setPrev(self.tail)
            self.tail.setNext(newNd)
            self.tail = newNd
        """else:
            currNd = self.head
            while currNd.getNext() != None:
                currNd = currNd.getNext()
            currNd.setNext(newNd)
            newNd.setPrev(currNd)
            self.tail = newNd"""
            
    def peekFirst(self):
        try:
            if self.isEmpty():
                raise IndexError("List is empty")
        except IndexError as e:
            print("Cannont view first element: "+str(e))
        else:
            return self.head.getValue()
    
    def peekLast(self):
        try:
            if self.isEmpty():
                raise IndexError("No tail set")
        except IndexError as e:
            print("Cannot view last element: "+str(e))
        else:
            return self.tail.getValue()
    
    def removeFirst(self):
        try:
            if self.isEmpty():
                raise IndexError("List is empty")
            elif (self.head is None):
                raise AttributeError("Unexpected Error")
        except IndexError as e:
            print("Cannot remove item from list:",e)
        except AttributeError as e:
            print("IDK Fam")
        else:
            if self.head.getNext() is None:
                value = self.head.getValue()
                self.head = None
                self.tail = None
                #print("The list is now empty")
            else:     
                value = self.head.getValue()
                self.head = self.head.getNext()
                self.head.setPrev(None)
            return value

    def removeLast(self):
        try:
            if self.isEmpty():
                raise IndexError("List is empty")
            elif self.tail is None:
                raise AttributeError("Unexpected Error")
        except IndexError as e:
            print("Cannot remove from item from list:",e)
        except AttributeError as e:
            print("IDK Fam")
        else:
            if self.tail.getPrev() is None:
                value = self.head.getValue()
                self.head = None
                self.tail = None
                #print("The list is now empty")
            else: 
                value = self.tail.getValue()
                self.tail = self.tail.getPrev()
                self.tail.setNext(None)
            return value
    
    def display(self):
        if self.isEmpty() == False:
            print("List Contents:\n")        
            currNd = self.head
            while currNd.getNext() is not None:
                print(currNd.getValue())
                print("\u2191\u2193")
                currNd = currNd.getNext()
            print(currNd.getValue())
        else:
            print("List is Empty")
    
    #def findNode(self,value):
    #    fnode = None


class DSAListNode():

    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    
    def getValue(self):
        return self.value
    
    def setValue(self,value):
        self.value = value
    
    def setNext(self,Nnode):
        self.next = Nnode
    
    def getNext(self):
        return self.next
    
    def getPrev(self):
        return self.prev
    
    def setPrev(self,Pnode):
        self.prev = Pnode
    


        
    