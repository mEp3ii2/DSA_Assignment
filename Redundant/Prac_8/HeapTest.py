from DSAHeap import *
import csv
import numpy as np

heap = DSAHeap(10)
heap.add(2,'bjf')
heap.add(6,'jbhb')
heap.add(0,'jbhb')
heap.add(9,'jbhb')
heap.add(3,'jbhb')
heap.add(8,'jbhb')
heap.add(5,'nshcvgyu')

heap.display()

heaps=[]
try:
    with open("RandomNames7000.csv","r") as csvfile:
        data = csv.reader(csvfile,delimiter=',')
        for row in data:
            priority = int(row[0])
            value = row[1]
            entry = DSAHeapEntry(priority,value)
            # print("Reading in:")
            # print(key)
            # print(row)
            heaps.append(entry)
except IOError as e:
    print("Error in fileprocessing"+str(e))

heap.heapSort(heaps)
heap.display()


try:
    with open('heapslist.csv',"w",newline='') as csvfile :
        writer = csv.writer(csvfile,delimiter=',')
        for item in heap.heap:
            if isinstance(item,DSAHeapEntry):
                writer.writerow([item.getPriority(),item.getValue()])
    print("Data Saved to csv")
except IOError as e:
    print("Error in file processing"+str(e))