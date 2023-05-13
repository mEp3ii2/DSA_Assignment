from DSAHashTable import *
from DSAHashEntry import *
import numpy as np

tabs = DSAHashTable(100)
tabs.put(10,11)
tabs.put(15,12)
tabs.put(23,'hejhfb')
tabs.remove(10)
tabs.display()