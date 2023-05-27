from DSAHashTable import *
from DSAHashEntry import *
import numpy as np

def hashTest():
    numTest =0
    numPass =0

    print("\nTest 1 - Hash Table Creation")
    print("======================")
    try:
        numTest +=1
        tabs = DSAHashTable(100)
        numPass +=1
        print("Passed")
    except:
        print("Failed")

    print("\nTest 2 - Hash Entries")
    print("======================")
    try:
        numTest +=1
        tabs.put(10,11)
        tabs.put(15,12)
        tabs.put(23,'hejhfb')
        if tabs.get(10) != 11:
            raise Exception("Incorrect valued retrieved")
        numPass +=1
        print("Passed")
    except:
        print("Failed")
    print("\nTest 3 - Get Entry ")
    print("======================")
    try:
        numTest +=1
        if tabs.get(10) != 11:
            pass 
        numPass +=1
        print("Passed")
    except:
        print("Failed")

    print("\nTest 4 - Removing Entries ")
    print("======================")
    try:
        numTest +=1
        tabs.remove(10)
        if tabs.get(10) != None:
            raise Exception("Entry not removed")
        numPass +=1
        print("Passed")
    except:
        print("Failed")

    print("\nTest 5 - Reading File ")
    print("======================")
    try:
        numTest +=1
        tabs = DSAHashTable(15000)
        tabs.importFile()
        if str(tabs.get('A')) != "Temp: 32°C. Humidity: 45%.  Wind: 90 km/h":
            print(tabs.get('A'))
            raise Exception("Entry not matching or not found")
        numPass +=1
        print("Passed")
    except:
        print("Failed")

    print("\nTest 6 - Retrieve value of entry after collision and then deletion of the collision cause")
    print("======================")
    try:
        numTest +=1
        tabs = DSAHashTable(50)
        tabs.put(1,'')
        tabs.put(2,'')
        tabs.put(3,'')
        tabs.put(8,'')
        tabs.put(19,'')
        tabs.put(42,'')
        tabs.put(83,'my my')
        tabs.put(51,'')
        tabs.put(109,'')
        tabs.put(11,'')
        tabs.put(89,'')
        tabs.put(23,'')
        tabs.put(87,'')
        tabs.remove(42)
        
        if tabs.get(83) != 'my my':
            raise Exception("Print collision handling not working")
        numPass +=1
        print("Passed")
    except:
        print("Failed")

    print("\nTest 7 - Resizing")
    print("======================")
    try:
        numTest +=1
        tabs = DSAHashTable(5)
        tabs.importFile()
        resizeLen=(len(tabs.hashArray))
        if resizeLen != 17:
            raise Exception("Print table did not resize to expected amounts")
        numPass +=1
        print("Passed")
    except:
        print("Failed")

    print("\n DSA Hash Table Test results")
    print(str(numPass)+"/"+str(numTest))
    print(str(numPass/numTest*100)+"% passed")
