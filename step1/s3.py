#!/usr/bin/python
# -*- coding: latin-1 -*-
import time
import os, sys
import subprocess as sp

def s3():
	data=list()

	#---------------------------------------------------------------------------------
	#	affiche nom machine
	#---------------------------------------------------------------------------------
	p = sp.Popen(["hostname"],stdout=sp.PIPE, stdin=sp.PIPE)
	data.append(p.stdout.readline())

	#---------------------------------------------------------------------------------
	#	affiche ram
	#---------------------------------------------------------------------------------
	cmd="grep MemTotal /proc/meminfo | cut -d: -f2 | sed 's/kB//' | sed 's/ //g'"	
    p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
    totalRAM = p.stdout.readline()
    cmd = "grep MemFree /proc/meminfo | cut -d: -f2 | sed 's/kB//' | sed 's/ //g'"
    p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
    freeRAM = p.stdout.readline()
    unusedRAM = float(freeRAM)/float(totalRAM)*100
    usedRAM = 100-unusedRAM
    data.append("%.2f" % usedRAM)

	#---------------------------------------------------------------------------------
	#	affiche cpu
	#---------------------------------------------------------------------------------
	cmd = "top -b -n1 | grep 'Cpu' | cut -d' ' -f11 | sed 's/,/./g'"
    p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
    freeCPU = float(p.stdout.readline())
    usedCPU = 100-float(freeCPU)
    data.append("%.2f" % usedCPU)

	#---------------------------------------------------------------------------------
	#	affiche swap memory
	#---------------------------------------------------------------------------------
	cmd = "grep SwapTotal /proc/meminfo | cut -d: -f2  | sed 's/kB//' | sed 's/ //g'"
    p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
    totalSwap = p.stdout.readline()
    cmd = "grep SwapTotal /proc/meminfo | cut -d: -f2  | sed 's/kB//' | sed 's/ //g'"
    p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
    freeSwap = p.stdout.readline()

    unusedSwap = float(freeSwap)/float(totalSwap)*100
    usedSwap = 100-unusedSwap
    data.append("%.2f" % usedSwap)

	#---------------------------------------------------------------------------------
	#	affiche utilisation disque
	#---------------------------------------------------------------------------------
	cmd= "df $PWD | awk '/[0-9]%/{print $(NF-1)}' | sed 's/%//g'"
    p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
    data.append(p.stdout.readline())

	#---------------------------------------------------------------------------------
	#	affiche utilisateurs connectés
	#---------------------------------------------------------------------------------
	cmd="who -q | cut -d: -f2 | tail -1 | sed 's/ //g'"
    p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
    data.append(p.stdout.readline())

    #---------------------------------------------------------------------------------
	#	affiche date
	#---------------------------------------------------------------------------------
	p=sp.Popen(["date", "+%Y-%m-%d:%H:%M:%S"],stdout=sp.PIPE, stdin=sp.PIPE)
    data.append(p.stdout.readline())

	#---------------------------------------------------------------------------------
	#	exporte toutes les données
	#---------------------------------------------------------------------------------
	cmd="ps -elf | wc -l"
    p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
    data.append(p.stdout.readline())

	