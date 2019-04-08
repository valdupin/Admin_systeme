#!/usr/bin/env python
import os
import time
import email
import graph
import bdd
import s2
import s3

while 1: 
	os.system('''sh "s1.sh"''')
	s2.s2()	
	s3.s3()
	bdd.bdd()
	bdd.lastAlert()
	graph.graph()

	time.sleep(15)
 