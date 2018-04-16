#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import psutil
import socket
from time import gmtime,strftime

def sonde2():
        donnees=list()

        #--------------------------------------------------------------------------------------------
        #Envoi le nom de la machine dans le fichier texte
        #--------------------------------------------------------------------------------------------
        donnees.append(socket.gethostname())


        #--------------------------------------------------------------------------------------------
        #On va prendre le CPU utilisé
        #Ensuite on va tout envoyer dans le fichier texte
        #--------------------------------------------------------------------------------------------
        donnees.append(psutil.cpu_percent(interval=1))


        #--------------------------------------------------------------------------------------------
        #On va calculer la RAM total            
        #--------------------------------------------------------------------------------------------
        donnees.append(psutil.virtual_memory().percent)

       
        #--------------------------------------------------------------------------------------------
        #Permet d'obtenir le swap total et le swap disponible pour l'utlisateur et l'envoi dans 
        #le fichier texte
        #--------------------------------------------------------------------------------------------
        donnees.append(psutil.swap_memory().percent)

        
        #--------------------------------------------------------------------------------------------
        #Permet d'obtenir le % du disk utilise de l'utlisateur et l'envoi dans le fichier
        #texte
        #--------------------------------------------------------------------------------------------
        donnees.append(psutil.disk_usage('/').percent)
        

        #--------------------------------------------------------------------------------------------
        #Permet de connaitre combien d'utilisateur présent, et l'envoi dans le fichier texte
        #--------------------------------------------------------------------------------------------
        donnees.append(len(psutil.users()))


        #--------------------------------------------------------------------------------------------
        #PS permet de connaître tous les processus qui sont en activités
        #On envoi tout dans le fichier texte
        #--------------------------------------------------------------------------------------------
        donnees.append(len(psutil.pids()))


        #--------------------------------------------------------------------------------------------
        #Permet d'obtenir la date du sondage de la sonde en bash
        #--------------------------------------------------------------------------------------------
        donnees.append(strftime("%Y-%m-%d:%H:%M:%S",gmtime()))


        #--------------------------------------------------------------------------------------------
        #Permet d'obtenir seulement l'heure de la sonde
        #--------------------------------------------------------------------------------------------
        donnees.append(strftime("%H",gmtime()))

        fichier = open("ressonde1.txt","w")
        for item in donnees:
                fichier.write("%s\n" %item)
        fichier.close

