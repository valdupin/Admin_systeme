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
        n=1

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

        for row in c.execute('SELECT DISTINCT hostname FROM sonde'):
            hostnames.append(row)
        data = [None] * 6
        for name in hostnames:
            for row in c.execute('''SELECT utilisateur, ram, disque, cpu, swap, time FROM sonde'''):
                bar_chart = pygal.Bar()
                bar_chart.title = 'Donnees utilisateur'
                bar_chart.x_labels = map(str, range(1,n))
                bar_chart.add('Utilisateur', row[0])
                bar_chart.add('Swap', row[4])
                bar_chart.add('CPU',  row[3])
                bar_chart.add('Ram', row[1])
                bar_chart.add('Disque', row[2])
                bar_chart.render_to_file("bar_chart.svg")
                bar_chart.render_in_browser()
