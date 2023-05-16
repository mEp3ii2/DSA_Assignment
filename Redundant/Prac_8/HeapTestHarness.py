from DSAHeap import *
import csv
import numpy as np 

numTest = 0
numPass = 0

print("\nTest 1 - Heap Creation ")
print("======================")
try:
    numTest +=1
    heapTest = DSAHeap(100)
    numPass +=1
    print("Passed")
except:
    print("Failed")

print("\nTest 2 - HeapAdd")
print("======================")
try:
    numTest +=1
    heapTest.add(10,"Hello")  
    if heapTest.heap[0].getPriority() != 10:
        raise Exception("Head Add not working") 
    numPass +=1
    print("Passed")
except:
    print("Failed")


print("\nTest 3 - Heap Remove")
print("======================")
try:
    numTest +=1
    removeTest = heapTest.remove()
    if removeTest.getPriority() != 10:
        raise Exception("Remove not working") 
    numPass +=1
    print("Passed")
except:
    print("Failed")

print("\nTest 4 - Heap Display ")
print("======================")
try:
    numTest +=1
    heapTest.add(10,'gdfg')
    heapTest.add(12,'ggdfdf')
    heapTest.add(7,'gdfg')
    heapTest.add(2,'gdfg')
    heapTest.add(99,'gdfg')
    heapTest.add(8,'gdfg')
    heapTest.display()
    numPass +=1
    print("Passed")
except:
    print("Failed")

print("\nTest 5 - Heap Sort")
print("======================")
#try:
numTest +=1
heapSortTest = DSAHeap(5)
data =[(10,'gjj'),(15,'57jb'),(7,'vcnmgj'),(25,'jgndjf'),(2,'qwss')]
for item in data:
    heapSortTest.add(item[0],item[1])
i =0
heapSortTest.display()
max_arr =[]
while i < 5:
    x = heapSortTest.remove()
    max_arr.append(x.getPriority())
    i+=1
same = True
testPri = [25,15,10,7,2]
print(max_arr)
for i in range(len(testPri)):
    if testPri[i] != max_arr[i]:
        same = False
if same == False:
    raise Exception("Heap not sorted properly")
numPass +=1
print("Passed")
#except:
#    print("Failed")

print("\nTest 6 - is full")
print("======================")
try:
    numTest +=1
    fullHeap = DSAHeap(2)
    fullHeap.add(10,'gg')
    fullHeap.add(9,'sgg')
    fullHeap.add(14,'jknjd')
    numPass +=1
    print("Passed")
except:
    print("Failed")
print("\nTest results")
print(str(numPass)+"/"+str(numTest))
print(str(numPass/numTest*100)+"% passed")
