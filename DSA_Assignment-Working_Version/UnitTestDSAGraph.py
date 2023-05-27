from Graphy import *
import numpy as np
import io
from contextlib import redirect_stdout
from GraphFileReader import *

# reference
# code to capture print out put from function
# Author: ForeverWintr (Dec 5, 2016)
# Stackoverflow How to capture stdout output from a Python function call?(May 15, 2013)
# Used in tests 4-7

def graphTest():
    numTest = 0
    numPass = 0


    print("\nTest 1  - Graph Creation ")
    print("======================")
    try:
        numTest +=1
        myGraph = DSAGraph()
        numPass +=1
        print("Passed")
    except:
        print("Failed")

    print("\nTest 2  - Add Vertexs")
    print("======================")
    try:
        numTest +=1
        myGraph.inputHandler('A','B',10.2) # create node  a and b and connecs them
        myGraph.inputHandler('A','C',15.4)
        myGraph.inputHandler('B','C',3.2)
        myGraph.inputHandler('D','C',1.0)
        myGraph.inputHandler('B','E',5.8)
        myGraph.inputHandler('A','E',4.9)
        myGraph.inputHandler('F','E',7.2)
        if myGraph.hasVertex('A') is not True:
            raise Exception("Vertex not added") 
        numPass +=1
        print("Passed")
    except:
        print("Failed")

    print("\nTest 3 - Edges ")
    print("======================")
    try:
        numTest +=1
        if myGraph.isAdjacent('B','C') is not True:
            raise Exception("Edge not present")
        numPass +=1
        print("Passed")
    except:
        print("Failed")


    print("\nTest 4 - Adjaceny List ")
    print("======================")
    try:
        numTest +=1
        f = io.StringIO()
        with redirect_stdout(f):
            myGraph.displayAsList() 
        out = f.getvalue()
        lines =out.split("\n")
        if lines[0].strip() != "A : ['B' 'C' 'E']":
            raise Exception("Adjaceny list failed")
        numPass +=1
        print("Passed")
    except:
        print("Failed")

    print("\nTest 5 - Adjaceny Matrix")
    print("======================")
    try:
        numTest +=1
        f = io.StringIO()
        with redirect_stdout(f):
            myGraph.displayAsMatrix()
        out = f.getvalue()
        lines =out.split("\n")
        
        if lines[0].strip() != '0 1 1 0 1 0':
            raise Exception("Adjaceny Matrix not correct")
        numPass +=1
        print("Passed")
    except:
        print("Failed")

    print("\nTest 6 - BredthFirstSearch")
    print("======================")
    try:
        numTest +=1
        f = io.StringIO()
        with redirect_stdout(f):
            myGraph.breadFirstSearch()
        out = f.getvalue()
        lines = " ".join(out.splitlines())
        lines = lines.split(':')
        print(lines)
        if lines[2].strip() != 'A B C E D F':
            raise Exception("BreadthFirstSearch Failed")
        numPass +=1
        print("Passed")
    except:
        print("Failed")

    print("\nTest 7 - DepthFirstSearch")
    print("======================")
    try:
        numTest +=1
        t = myGraph.deepFirstSearch()
        path =''
        while t.isEmpty() is not True:
            path += t.dequeue().getLabel()
        if  path != 'ABCDEF':
            print(path)
            raise Exception("DepthFirstSearch Failed")
        numPass +=1
        print("Passed")
    except:
        print("Failed")

    print("\nTest 8 - Edge Weight ")
    print("======================")
    try:
        numTest +=1
        edgeWeight = myGraph.getEdge('A','B')
        weight = edgeWeight.getWeight()
    
        print(weight)
        if float(weight) != 10.2:
            raise Exception("Edge weight incorrect")
        numPass +=1
        print("Passed")
    except:
        print("Failed")

    print("\nTest 9 - Edge Removal")
    print("======================")
    try:
        numTest +=1
        myGraph.removeVertex("A")
        if myGraph.hasVertex("A")==True:
            raise Exception("Vertex A not removed, remove function not working")
        numPass +=1
        print("Passed")
    except:
        print("Failed")
        print("\n Test results")

    print("\nTest 10 - FileIO ")
    print("======================")
    try:
        numTest +=1
        newGraph =  readData()

        if newGraph.hasVertex("A") != True:
            raise Exception("file not read in properly")
        numPass +=1
        print("Passed")
    except:
        print("Failed")
    
    print("DSA Graph test results")
    print(str(numPass)+"/"+str(numTest))
    print(str(numPass/numTest*100)+"% passed")