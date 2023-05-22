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

def UavSel():
    selUAv = None
    uavSel = False
    if not uavList.isEmpty():
        print("Please select your UAV using the UAV ID")
        for uav in uavList:
            print("UAV "+str(uav.getID()))
        sel = int(input("Selection: "))
        for uav in uavList:
            if uav.getID() == sel:
                selUAv = uav
                uavSel = True
            if uavSel == False:
                print("No UAV selected!")
        return selUAv
    else:
        print("No uavs to select!!")
def locationInfoValidater():
    print("Please provide the location data")
    tempValid = False
    while tempValid == False:
        try:
            print("Please enter the temperature value")
            temp = input("Temperature: ")
            temp = int(temp)
            if temp < 25:
                raise ValueError("Temperature value cannot be below 25")
        except ValueError as e:
            print("Invalid temperature "+str(e))
        else:
            tempValid = True

    humidValid = False
    while humidValid == False:
        try:
            print("Please enter the humidty")
            humidity = input("Humidity: ")
            humidity = int(humidity)
            if not 0<=humidity <= 100:
                raise ValueError("Humidity value must be between 0-100")
        except ValueError as e:
            print("Invalid humidity "+str(e))
        else:
            humidValid = True

    windValid = False
    while windValid == False:
        try:
            print("Please enter the wind speed")
            wind = input("Wind speed: ")
            wind = int(wind)
            if wind < 0:
                raise ValueError("Wind speed cannot be negative")
        except ValueError as e:
            print("Invalid wind speed "+str(e))
        else:
            windValid = True
    arr = np.empty(3)
    arr[0]=temp
    arr[1]=humidity
    arr[2]=wind
    return arr

def insertLocation(graph,heap,hashTb):

    nextVertex = chr(65 + graph.getVertexCount())
    print("New vertex "+str(nextVertex)+" has been created")
    connected = False
    while connected == False:
        print("Please provide a connection location")
        graph.displayVertexes()
        connection = input("Selection: ")
        check = graph.getVertex(connection.upper())
        if check == None:
            print("Invalid selection please try again")
        elif isinstance(check,DSAGraphNode):
            connected = True
    weighted = False
    while weighted == False:
        print("Please enter the distance between "+str(nextVertex)+" and "+str(connection))
        weight = input("Distance: ")
        if graph.floatChecker(weight):
            weight = float(weight)
        else:
            print("Not a valid float")
        if weight <= 0:
            print("Weight must be above zero")
        else:
            weighted = True
    locationData = locationInfoValidater()
    _insertLocation(graph,heap,hashTb,nextVertex,connection,weight,locationData)

def _insertLocation(graph,heap,hashTb,nextVertex,connection,weight,locationData):
    graph.inputHandler(nextVertex,connection,weight)
    hashTb.put(nextVertex,locationData)
    vert = hashTb.get(nextVertex)
    risk = riskLvlCalc(vert)
    heap.add(risk,nextVertex)
    print("New location has been added")

    
 
def removeLocation(graph,heap,hashTb,label):
    graph.removeVertex(label)
    hashTb.remove(label)
    # need operation for specific heap remove
    # this shit efficent as fuck
    arr = np.empty(graph.getVertexCount()-1,dtype=object)
    index = 0
    while not heap.isEmpty():
        value=heap.remove()
        if value.getValue() != label:
            arr[index]= value
            index += 1
    for i in range(len(arr)):
        heap.add(arr[i].getPriority(),arr[i].getValue())
    print("Location "+str(label)+" has been removed")

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
        print("3: Select UAV")
        currUAV = UavSel()

    elif usrInp == '4':
        print("4: UAV operations")
        UavOptMsg()
    elif usrInp == '5':
        print("5: View locations")
        pass
    elif usrInp == '6':
        print("6: Location Options")
        print("A: Insert new location")
        print("B: Delete location")
        print("C: Search location")
        selection = input("Selection: ")
        selection = selection.upper()
        if selection == 'A':
            insertLocation(graph,heap,hashTb)
        elif selection == 'B':
            pass
        elif selection == 'C':
            pass
        else:
            print("Invalid operation returning back to the main menu")
    elif usrInp == '7':
        print("7: Traverse the list via high to low risk")
        if currUAV is None:
            print("Please select a UAV before proceeding ")
            currUAV = UavSel()
        
        travelList = np.empty(graph.getVertexCount()-1,dtype=object)
        index = 0
        totDistance = 0
        initLocation = currUAV.getLocation()
        
        print("UAV "+str(currUAV.getID())+" itinerary")
        itinerary = str(currUAV.getLocation())+' -> '
        while not heap.isEmpty():
            dest = heap.remove()
            if dest.getValue() != initLocation:
                path = graph.dijkstra(currUAV.getLocation(),dest.getValue())
                end = path.removeLast()
                currUAV.setLocation(end[0])
                totDistance += end[1]
                travelList[index]= end[0]
                index += 1
        for char in travelList:
            itinerary += str(char)+ ' -> '
        itinerary = itinerary.rstrip(' -> ')
        print(itinerary) 
        print("Total distance: {:.2f}".format(totDistance))
    elif usrInp == '8':
        pass
    elif usrInp == '9':
        pass
    elif usrInp == 'f':
        menuMsg()
    else:
        print(usrInp+"is a invalid command please try again")
