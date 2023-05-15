from DSAHeap import *
heapSortTest = DSAHeap(5)
data =[(10,'gjj'),(15,'57jb'),(7,'vcnmgj'),(25,'jgndjf'),(2,'qwss')]
for item in data:
    heapSortTest.add(item[0],item[1])
#heapSortTest.display()
print(heapSortTest.remove().getPriority())
print(heapSortTest.remove().getPriority())
print(heapSortTest.remove().getPriority())
print(heapSortTest.remove().getPriority())
print(heapSortTest.remove().getPriority())
