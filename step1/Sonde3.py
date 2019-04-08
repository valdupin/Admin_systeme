#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import subprocess as sp
import time


def sonde3():
        donnees=list()

        #--------------------------------------------------------------------------------------------
        #Envoi le nom de la machine dans le fichier texte
        #--------------------------------------------------------------------------------------------
        p = sp.Popen(["hostname"],stdout=sp.PIPE, stdin=sp.PIPE)
        donnees.append(p.stdout.readline())
	

        #--------------------------------------------------------------------------------------------
        #On va prendre le CPU libre et on le soustraire au CPU utilisé
        #Ensuite on va tout envoyer dans le fichier texte
        #--------------------------------------------------------------------------------------------
        cmd = "top -b -n1 | grep 'Cpu' | cut -d' ' -f11 | sed 's/,/./g'"
        p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
        cpuDisponible = float(p.stdout.readline())
        cpuUtilise = 100-float(cpuDisponible)
        donnees.append("%.2f" % cpuUtilise)


        #--------------------------------------------------------------------------------------------
        #On va calculer la mémoire total puis on va la soustraire à la mémoire disponible et 
        #l'envoyer dans le fichier texte        
        #--------------------------------------------------------------------------------------------
        cmd="grep MemTotal /proc/meminfo | cut -d: -f2 | sed 's/kB//' | sed 's/ //g'"	
        p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
        MemTot = p.stdout.readline()
        cmd = "grep MemFree /proc/meminfo | cut -d: -f2 | sed 's/kB//' | sed 's/ //g'"
        p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
        MemDispo = p.stdout.readline()
        MemFree = float(MemDispo)/float(MemTot)*100
        MemUse = 100-MemFree
        donnees.append("%.2f" % MemUse)

        #--------------------------------------------------------------------------------------------
        #Permet d'obtenir le swap total et le swap disponible pour l'utlisateur et l'envoi dans 
        #le fichier texte
        #--------------------------------------------------------------------------------------------
        cmd = "grep SwapTotal /proc/meminfo | cut -d: -f2  | sed 's/kB//' | sed 's/ //g'"
        p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
        SwapTot = p.stdout.readline()
        cmd = "grep SwapTotal /proc/meminfo | cut -d: -f2  | sed 's/kB//' | sed 's/ //g'"
        p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
        SwapDispo = p.stdout.readline()

        #--------------------------------------------------------------------------------------------
        #Permet d'obtenir le swap libre et utilisé et envoyer dans le fichier texte le swap
        #utlisé par l'utilisateur
        #--------------------------------------------------------------------------------------------
        SwapFree = float(SwapDispo)/float(SwapTot)*100
        SwapUse = 100-SwapFree
        donnees.append("%.2f" % SwapUse)


        #--------------------------------------------------------------------------------------------
        #On va donc envoyer la memoire du disque dans le fichier texte
        #--------------------------------------------------------------------------------------------
        cmd= "df $PWD | awk '/[0-9]%/{print $(NF-1)}' | sed 's/%//g'"
        p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
        donnees.append(p.stdout.readline())

        #--------------------------------------------------------------------------------------------
        #Permet de connaitre combien d'utilisateur présent, et l'envoi dans le fichier texte
        #--------------------------------------------------------------------------------------------
        cmd="who -q | cut -d: -f2 | tail -1 | sed 's/ //g'"
        p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
        donnees.append(p.stdout.readline())

        #--------------------------------------------------------------------------------------------
        #On envoi tout dans le fichier texte
        #--------------------------------------------------------------------------------------------
        cmd="ps -elf | wc -l"
        p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
        donnees.append(p.stdout.readline())

        #--------------------------------------------------------------------------------------------
        #Permet d'obtenir la date du sondage de la sonde en bash
        #--------------------------------------------------------------------------------------------
        p=sp.Popen(["date", "+%Y-%m-%d:%H:%M:%S"],stdout=sp.PIPE, stdin=sp.PIPE)
        donnees.append(p.stdout.readline())

        #--------------------------------------------------------------------------------------------
        #Permet d'obtenir seulement l'heure de la sonde
        #--------------------------------------------------------------------------------------------
        p=sp.Popen(["date","+%H"],stdout=sp.PIPE, stdin=sp.PIPE)
        donnees.append(p.stdout.readline())


        fichier = open("ressonde1.txt","w")
        for item in donnees:
                fichier.write("%s\n" % item)

        fichier.close

