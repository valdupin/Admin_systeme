#!/usr/bin/env python
import os
import time
import Sonde2
import Sonde3
import BDD
import Graph


while 1: 
    os.system('''sh "Sonde1.sh"''')
    Sonde2.sonde2()	
    #Sonde3.sonde3()
    BDD.bdd()
    BDD.bdd_pars()
    Graph.graph()
   
    
   
    time.sleep(15)
 