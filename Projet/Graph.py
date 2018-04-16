#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import sqlite3
import pygal
from datetime import datetime, timedelta

def graph():
        connection = sqlite3.connect('sonde.db')

        c = connection.cursor() 

        #declaration des list dont on a besoin
        hostnames = list()
        listeDisque = list()
        listeRam = list()
        listeSwap = list()
        listeCpu = list()
        listeUtilisateur = list()
        n=5

        #--------------------------------------------------------------------------------------------
        #Cette boucle va permettre de séparer l'historique de chaque utilisateur
        #--------------------------------------------------------------------------------------------
        graphDisk = [listeDisque[x:x+n] for x in range(0,len(listeDisque),n)]
        


        #--------------------------------------------------------------------------------------------
        #Les boucles suivantes vont permettre de remplir la liste avec tous les noms
        #de toutes les machines, ainsi que l'affichage de chaque entrée
        #--------------------------------------------------------------------------------------------

        for row in c.execute('SELECT DISTINCT hostname FROM sonde'):
            hostnames.append(row)

        for name in hostnames:
            for row in c.execute('select * from sonde WHERE hostname=? ORDER BY time DESC LIMIT 1',name):
                    print (row)
        

        #--------------------------------------------------------------------------------------------
        #Les boucles qui suivent vont permettre de remplir les liste préalablement définis
        #   - Disque,
        #   - Ram,
        #   - Cpu,
        #   - Swap,
        #   - Utilisateur,
        #Elles vont permettre non seulement de remplir les listes mais aussi d'avoir l'historique
        #de chaque machine
        #--------------------------------------------------------------------------------------------

        for name in hostnames:
            for row in c.execute('SELECT disque from sonde WHERE hostname=? ORDER BY time DESC LIMIT 5',name):
                listeDisque.append(row)

        for name in hostnames:
            for row in c.execute('SELECT ram FROM sonde WHERE hostname=? ORDER BY time DESC LIMIT 5',name):
                listeRam.append(row)       
            graphRam = [listeRam[x:x+n] for x in range(0,len(listeRam),n)]

        for name in hostnames:
            for row in c.execute('SELECT cpu FROM sonde WHERE hostname=? ORDER BY time DESC LIMIT 5',name):
                listeCpu.append(row)     
            graphCpu = [listeCpu[x:x+n] for x in range(0,len(listeCpu),n)]
        

        for name in hostnames:
            for row in c.execute('SELECT swap FROM sonde WHERE hostname=? ORDER BY time DESC LIMIT 5',name):
                listeSwap.append(row)        
            graphSwap = [listeSwap[x:x+n] for x in range(0,len(listeSwap),n)]


        for name in hostnames:
            for row in c.execute('SELECT utilisateur FROM sonde WHERE hostname=? ORDER BY time DESC LIMIT 5',name):
                listeUtilisateur.append(row)
            graphUser = [listeUtilisateur[x:x+n] for x in range(0,len(listeUtilisateur),n)]

        connection.close()



        #--------------------------------------------------------------------------------------------
        #Les fonctions qui vont suivre vont permettre de créer un graphique des données suivantes :
        #   - %Disque utilisé,
        #   - %Ram utilisé,
        #   - %CPU utilisé,
        #   - SWAP total,
        #   - Nombre utilisateur connectés
        #Les graphiques seront crées sous forme de page HTML, elles vont se mettre à jour a chaque
        #fois que les sondes vont être relancés
        #--------------------------------------------------------------------------------------------

        connection = sqlite3.connect('sonde.db')
        c = connection.cursor()
        c.execute("""SELECT cpu, ram, disque,cpu, swap time FROM sonde""")
        data = c.fetchone()

        bar_chart = pygal.Bar()
        bar_chart.title = 'Donnees utilisateur'
        bar_chart.x_labels = map(str, range(1,n))
        bar_chart.add('Utilisateur', data[0])
        bar_chart.add('Swap', data[4])
        bar_chart.add('CPU',  data[3])
        bar_chart.add('Ram', data[1])
        bar_chart.add('Disque', data[2])
        bar_chart.render_in_browser()