import math
from os import abort
import numpy as np
from DSAHashEntry import *
import csv
from LocationInfo import *

class DSAHashTable():
    #hash Array (DSAHASHEntry array)
    # count (int)

    def __init__(self,tableSize):
        self.count = 0
        actualSize = self.nextPrime(tableSize)
        self.hashArray = np.zeros(actualSize, dtype=object)
        for i in range(actualSize):
            self.hashArray[i] = DSAHashEntry()

    def put(self,inKey, inValue):
        if isinstance(inValue,np.ndarray):
            temp =inValue[0]
            humid = inValue[1]
            wind = inValue[2]
            inValue = self.createLocationInfo(temp,humid,wind)
        if self.getLoadFactor() >= 0.75:
            self.resize(len(self.hashArray)*2)
        hashInd = self.hash(inKey)
        if self.hashArray[hashInd].getState() == 0:
            self.hashArray[hashInd].setKey(inKey)
            self.hashArray[hashInd].setValue(inValue)
            self.hashArray[hashInd].setState(1)     
        elif self.hashArray[hashInd].getState() == 1 and self.hashArray[hashInd].getKey() == inKey:
            self.hashArray[hashInd].setValue(inValue)
        else:
            step = self.stepHash(inKey)
            while self.hashArray[hashInd].getState() == 1 and self.hashArray[hashInd].getKey() != inKey:
                hashInd=(hashInd + step)%len(self.hashArray)
            if self.hashArray[hashInd].getState() == 0:
                self.hashArray[hashInd].setKey(inKey)
                self.hashArray[hashInd].setValue(inValue)
                self.hashArray[hashInd].setState(1)
        self.count += 1
    
    def createLocationInfo(self,temp,humidity,wind):
        locationDets = locationInfo(temp,humidity,wind)
        return locationDets
    
    def findEmpty(self,inKey):
        hash1 = self.hash(inKey)
        hash2 = self.doubleHash(inKey)
        i = 0
        while True:
            next_slot = (hash1 + i * hash2) % len(self.hashArray)
            if self.hashArray[next_slot].getState() == 0:
                return next_slot
            i += 1
        if i * hash2 > len(self.hashArray):
            raise Exception("Table is full")
          

    def find(self, inKey):
        hashInd = self.hash(inKey)
        if self.hashArray[hashInd].getState()==0:
            return None
        elif self.hashArray[hashInd].getState()==1 and self.hashArray[hashInd].getKey()==inKey:
            return hashInd
        else:
            hash1 = self.hash(inKey)
            hash2 = self.doubleHash(inKey)
            i = 0
            while True:
                next_slot = (hash1 + i * hash2) % len(self.hashArray)
                if self.hashArray[next_slot].getState() == 0:
                    return None
                elif self.hashArray[next_slot].getKey() == inKey:
                    return next_slot
                i += 1
                if i * hash2 > len(self.hashArray):
                    raise Exception("Table is full")
                
    def get(self,inkey):
        hashInd = self.find(inkey)
        if hashInd is not None:
            return self.hashArray[hashInd].getValue()
        else: 
            return None
        
    def remove(self,inKey):
        hashInd = self.find(inKey)
        if hashInd is not None:
            self.hashArray[hashInd].setKey(None)
            self.hashArray[hashInd].setValue(None)
            self.hashArray[hashInd].setState(2)
            self.count -= 1
        if self.getLoadFactor() <= 0.25:
            self.resize(len(self.hashArray)//2)
    
    def display2(self):
        for hash in self.hashArray:
            print(hash)

    def display(self):
        for hash in self.hashArray:
            if hash.getState() == 1:
                print("Key: "+str(hash.getKey()))
                print("Value: "+str(hash.getValue()))
    
    def getLoadFactor(self):
        lf = self.count / len(self.hashArray)
        return lf
    
    def exportCsv(self,fileName):
        try:
            with open(fileName,"w",newline='') as csvfile :
                writer = csv.writer(csvfile,delimiter=',')
                for item in self.hashArray:
                    if isinstance(item,DSAHashEntry) and item.getState()==1:
                        writer.writerow([item.getKey(),item.getValue()])
            print("Data Saved to "+str(fileName))
        except IOError as e:
            print("Error in file processing"+str(e))
    
    def importFile(self):
        try:
            with open("UAVdata.txt","r") as file:
                for line in file:
                    line = line.strip()
                    
                    key = line[0]
                    values = np.array([int(v) for v in line[2:].split()])
                    #value = np.empty(2,dtype=int)
                    #value[0]=line[1]
                    #value[1]=line[2]
                    #value[2]=line[3]
                   # print("Reading in:")
                   # print(key)
                   # print(row)
                    self.put(key,values)
        except IOError as e:
            print("Error in fileprocessing"+str(e))
    
    def resize(self,size):
        oldTable = self.hashArray
        actualSize = self.nextPrime(size)
        newTable = np.zeros(int(actualSize), dtype=object)
        self.hashArray = newTable
        self.count = 0
        
        for i in range(int(actualSize)):
            self.hashArray[i] = DSAHashEntry()
        for entry in oldTable:
            if isinstance(entry, DSAHashEntry):
                if entry.getKey() is not None:
                    self.put(entry.getKey(),entry.getValue())
        
    def hash(self,inKey):
        a = 63689
        b = 378551
        hashInd = 0
        i = 0
        inKey = str(inKey)
        if not inKey.isdigit():
            sum = 0
            for char in inKey:
                sum += ord(char)
            inKey = sum
        inKey = str(inKey)
        for i in range(len(inKey)):
            hashInd = (hashInd * a) + int(inKey[i])
            a*=b
        hash = hashInd % len(self.hashArray)
        return hash

    def doubleHash(self,inKey):
        tableSize = len(self.hashArray)
        prime= self.nextPrime(tableSize)
        hash_value =0
        inKey = str(inKey)
        for char in inKey:
            hash_value = (hash_value * 33 +ord(char)) % prime
        return hash_value
    
    def stepHash(self,inKey):
        tableSize = len(self.hashArray)
        hash1 = self.hash(inKey)
        hash2 = self.doubleHash(inKey)
        i = 1
        while True:
            next_slot = (hash1 + i * (hash2+1)) % tableSize
            if self.hashArray[next_slot].getState() == 0:
                # empty slot found return index
                return next_slot
            elif self.hashArray[next_slot].getState() == 1 and self.hashArray[next_slot].getKey() == inKey:
                return next_slot
            i +=1

    def nextPrime(self,startVal):
        if (startVal % 2 == 0):
            primeVal = startVal -1
        else:
            primeVal = startVal
    
        isPrime = False
        
        while(not isPrime):
            primeVal += 2
            i = 3
            isPrime = True
            rootVal = math.sqrt(primeVal)
            while(i <= rootVal) and (isPrime):
                if primeVal % i == 0:
                    isPrime = False
                else:
                    i += 2
        return primeVal
    
    #Option methods
    def findKey(inKey):
        pass

    


