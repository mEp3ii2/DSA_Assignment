from  UAV import *
from Graphy import *
from GraphFileReader import *
from DSAHashTable import *
from DSAHeap import *
import StackAndQ as sq
import numpy as np
from LocationInfo import *
from LinkedList import *

def riskLvlCalc(locationData):
    riskLevel = 0
    
    temp = locationData.getTemp()
    humidity = locationData.getHumidity()
    wind = locationData.getWind()

    if temp <= 32:
        riskLevel += 1
    elif 33 <= temp <= 40:
        riskLevel += 2
    elif temp >= 41:
        riskLevel += 3

    if humidity >= 50:
        riskLevel += 1
    elif 31 <= humidity <= 49:
        riskLevel += 2
    elif humidity <= 30:
        riskLevel += 3
        
    if wind <= 40:
        riskLevel += 1
    elif 41 <= wind <= 55:
        riskLevel += 2
    elif wind >=56:
        riskLevel += 3

    return riskLevel

def loadFiles():
    graph = readData()
    count = graph.getVertexCount()

    hash = DSAHashTable(count)
    hash.importFile()

    heap = DSAHeap(count)
    vertexes = graph.deepFirstSearch()

    while vertexes.isEmpty() is not True:
        lab = vertexes.dequeue().getLabel()
        vert = hash.get(lab)
        risk = riskLvlCalc(vert)
        heap.add(risk,lab)
    arr = np.empty(3,dtype=object)
    arr[0]= graph
    arr[1] = hash
    arr[2] = heap
    return arr

def menuMsg():
    print("BushFire Monitoring Station")
    print("Options")
    print("1: Load Files")
    print("2: Launch UAV")
    print("3: Select UAV")
    print("4: UAV operations")
    print("5: View locations")
    print("6: Location Options('Insert', 'Delete','Search')")
    print("7: Traverse the list via high to low risk")
    print("8: Save Information to files")

def UavOptMsg():
    print("UAV options")
    print("1: View Current Location")
    print("2: Travel to new location")

menuMsg()
uavList = DSALinkedList()
filesLoaded = False
currUAV = None
run = True

while run:
    print("Please enter a number to select your operation enter 'f' to view the options again")
    usrInp = input("Selection: ")

    if usrInp == '1':
        arr = loadFiles()
        graph = arr[0]
        hashTb = arr[1]
        heap = arr[2]
        filesLoaded = True
    
    elif usrInp == '2':
        print("2: Launch UAV")
        if filesLoaded == True:
            try:
                location = input("Please enter a starting location: ")
                if len(location) !=1  or not location.isalpha():
                    raise AttributeError("Location should be a char")
                start = graph.getVertex(location)
                if start is None:
                    raise ValueError("Location "+str(location)+" not in the graph")
            except AttributeError as e:
                print("Input was invalid: "+str(e))
            except ValueError as e:
                print("Location not found please try again")
            else:

                uavList.insertLast(UAV(location))
        else:
            uavList.insertLast(UAV)

    elif usrInp == '3':
        uavSel = False
        print("3: Select UAV")
        print("Please select your UAV using the UAV ID")
        for uav in uavList:
            print("UAV "+str(uav.getID()))
        sel = int(input("Selection: "))
        for uav in uavList:
            if uav.getID() == sel:
                currUAV = uav
                uavSel = True
        if uavSel == False:
            print("No UAV selected!")

    elif usrInp == '4':
        print("4: UAV operations")
        UavOptMsg()
    elif usrInp == '5':
        print("5: View locations")
        pass
    elif usrInp == '6':
        print("6: Location Options('Insert', 'Delete','Search')")
        pass
    elif usrInp == '7':
        print("7: Traverse the list via high to low risk")
        travelList = np.empty(graph.getVertexCount(),dtype=object)
        index = 0
        totDistance = 0
        print("UAV "+str(currUAV.getID())+" itinerary")
        itinerary = str(currUAV.getLocation())+' -> '
        while not heap.isEmpty():
            dest = heap.remove()
            path = graph.dijkstra(currUAV.getLocation(),dest.getValue())
            end = path.removeLast()
            currUAV.setLocation(end[0])
            totDistance += end[1]
            travelList[index]= end[0]
            print(index)
        for char in travelList:
            itinerary += str(char)+ ' -> '
        itinerary = itinerary.rstrip(' -> ')
        print(itinerary) 
        print("Total distance: "+str(totDistance))
    elif usrInp == '8':
        pass
    elif usrInp == '9':
        pass
    elif usrInp == 'f':
        menuMsg()
    else:
        print(usrInp+"is a invalid command please try again")
