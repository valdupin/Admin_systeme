#!/usr/bin/python
# -*- coding: latin-1 -*-
import pygal
import sqlite3
import os, sys
from datetime import datetime, timedelta

def graph():
        connect = sqlite3.connect('sonde.db')
        c = connect.cursor() 
        hostnames = list()
        n=5

        #--------------------------------------------------------------------------------------------
        #   création d'un graph contenant les données du pc
        #--------------------------------------------------------------------------------------------

        for row in c.execute('SELECT DISTINCT hostname FROM sonde'):
            hostnames.append(row)

        for name in hostnames:
            for row in c.execute("""SELECT utilisateur, ram, disque, cpu, swap time FROM sonde"""):
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
