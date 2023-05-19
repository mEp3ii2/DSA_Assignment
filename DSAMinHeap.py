from DSAHeapEntry import *
import numpy as np

class DSAMinHeap():
    
    def __init__(self,size) -> None:
        self.heap = np.zeros(size,dtype=object)
        for i in range(len(self.heap)):
            self.heap[i] = DSAHeapEntry()
        self.count = 0
        self.length = size

    def add(self,priority,value):
        try:
            if self.count == self.length:
                raise IndexError("Heap is full")
            if type(priority) == str:
                if not priority.isdigit():
                    raise AttributeError("Non integer value")
            priority = int(priority)
            if priority < 0:
                raise ValueError("Negative Value detected for priority")
            if not value:
                raise ValueError("Empty Value string detected")
        except AttributeError as e:
            print("Invalid priority: "+str(e))
        except ValueError as e:
            print("Invalid input: "+str(e))
        except IndexError as e:
            print("Exceeded heap boundaries: "+str(e))
        else:
            self._add(priority,value)
        
    def _add(self,priority,value):
        self.heap[self.count].setPriority(priority)
        self.heap[self.count].setValue(value)
        self.trickleUp(self.count,self.heap)
        self.count +=1

    def remove(self):
        try:
            if self.count == 0 or self.heap[0].getPriority() == None:
                raise IndexError("Cannot remove from empty list")
            root = self.heap[0]
            self.heap[0]=self.heap[self.count-1]
            self.count -=1
            self.trickleDown(0)
        except IndexError as e:
            print("List empty: "+str(e))
        else:    
            return root.getPriority(), root.getValue()
        '''
            temp = self.heap[0]
            if self.count == 1:
                self.heap = np.zeros(self.length,dtype=object)
                for i in range(len(self.heap)):
                    self.heap[i] = DSAHeapEntry()
            else:
                self.heap[0]=self.heap[self.count-1] 
                self.trickleDown(0,self.heap)
                self.count -= 1
        except IndexError as e:
            print("List empty: "+str(e))
        else:    
            return temp '''


    def display(self):
        for item in self.heap:
            if item.getPriority() is not None:
                print("Priority: "+str(item.getPriority()))
                print("Value: "+str(item.getValue()))
                print()

    def trickleUp(self,index,heapArr):
        parentIdn = int((index -1)/2)
        if index > 0 and heapArr[index].getPriority() is not None and heapArr[parentIdn].getPriority() is not None:
            if self.heap[index].getPriority() < self.heap[parentIdn].getPriority():
                temp = heapArr[parentIdn]
                heapArr[parentIdn] = heapArr[index]
                heapArr[index] = temp
                self.trickleUp(parentIdn,heapArr)

    def trickleDown(self,index):
        lChild = 2*index+1
        rChild = 2*index+2
        smallest = index

        if lChild < self.count and self.heap[lChild].getPriority() < self.heap[smallest].getPriority():
            smallest = lChild
        if rChild < self.count and self.heap[rChild].getPriority() < self.heap[smallest].getPriority():
            smallest = rChild
        if smallest != index:
            temp =self.heap[index]
            self.heap[index] = self.heap[smallest]
            self.heap[smallest]=temp
            self.trickleDown(smallest)

    def trickleDown2(self,index,heapArr):
        lChild = index * 2 +1
        rChild = lChild + 1
        if lChild < len(heapArr):
            largeInd = lChild
            if rChild < len(heapArr):
                if heapArr[lChild].getPriority() < heapArr[rChild].getPriority():
                    largeInd = rChild
            if heapArr[largeInd].getPriority() > heapArr[index].getPriority():
                temp = heapArr[largeInd]
                heapArr[largeInd] = heapArr[index]
                heapArr[index] = temp
                self.trickleDown(largeInd)
    
    def heapify(self,heapArr):
        for i in range(int(len(heapArr)/2)-1,-1,-1):
            self.trickleDown(i)
        return heapArr
    
    def heapSort(self,heapArr):
        heapArr = self.heapify(heapArr)
        i = len(heapArr)-1
        for i in range(len(heapArr)-1,0,-1):
            temp = heapArr[0]
            heapArr[0] = heapArr[i]
            heapArr[i] = temp
            self.trickleDown(0)
        self.heap = heapArr
    
    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False