from DSAHeap import *
import csv
import numpy as np

heaps =[]

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

heap = DSAHeap(7000)
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