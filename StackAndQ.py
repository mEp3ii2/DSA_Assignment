#StacksAndQ.py
#test file for implementing stacks and queues
#Mitchell Pontague 
#19126924

import numpy as np
from LinkedList import *

class DSAStack():
    
    def __init__(self):
        self.stack = DSALinkedList()

    def __iter__(self):
        return iter(self.stack)

    def isEmpty(self):
        if self.stack.isEmpty():
            return True

    def push(self,value):
        self.stack.insertFirst(value)
    
    def pop(self):
        return self.stack.removeFirst()
    
    def peekFirst(self):
        return self.stack.peekFirst()

    def display(self):
        self.stack.display()      

class DSAQueue():

    def __init__(self):
        self.queue = DSALinkedList()
    
    def __iter__(self):
        return iter(self.queue)
    
    def isEmpty(self):
        if self.queue.isEmpty():
            return True
    
    # adds item to the queue
    def enqueue(self,value):
        self.queue.insertLast(value)

    # takes the first item from queue
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        else:
            x = self.queue.peekFirst()
            self.queue.removeFirst()
            return x

    # gives the first item
    def front(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        else:
            return self.queue.peekFirst()

    def last(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        else:
            return self.queue.peekLast()

