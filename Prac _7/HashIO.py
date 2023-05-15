from DSAHashTable import *
from DSAHashEntry import *

tabs = DSAHashTable(100)
#tabs.display2()
tabs.importCsv()
tabs.exportCsv('hashes.csv')