#!/usr/bin/python
# -*- coding: latin-1 -*-
import socket
import os, sys
from time import gmtime,strftime
import psutil


def s2():
	data=list()
#---------------------------------------------------------------------------------
#	affiche nom machine
#---------------------------------------------------------------------------------
	data.append(socket.gethostname())
#---------------------------------------------------------------------------------
#	affiche ram
#---------------------------------------------------------------------------------
    data.append(psutil.virtual_memory().percent)
#---------------------------------------------------------------------------------
#	affiche cpu
#---------------------------------------------------------------------------------
    data.append(psutil.cpu_percent(interval=1))
#---------------------------------------------------------------------------------
#	affiche swap memory
#---------------------------------------------------------------------------------
    data.append(psutil.swap_memory().percent)
#---------------------------------------------------------------------------------
#	affiche utilisation disque
#---------------------------------------------------------------------------------
    data.append(psutil.disk_usage('/').percent)
#---------------------------------------------------------------------------------
#	affiche utilisateurs connectés
#---------------------------------------------------------------------------------
    data.append(len(psutil.users()))
#---------------------------------------------------------------------------------
#	affiche processus actifs
#---------------------------------------------------------------------------------
    data.append(len(psutil.pids()))
#---------------------------------------------------------------------------------
#	affiche date
#---------------------------------------------------------------------------------
    data.append(strftime("%Y-%m-%d:%H:%M:%S",gmtime()))
