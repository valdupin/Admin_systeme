#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import time
import sqlite3
import fileinput
#perso
import lastAlert
import alert


def bdd():
	#---------------------------------------------------------------------------------
	#	création de la bdd à partir du fichier s1RES
	#---------------------------------------------------------------------------------
	list = [None] * 9
	i = 0
	with open("s1RES.txt","r") as f:
		for line in f:
			for word in line.split():
				liste[i]=word
				i+=1
		f.close()

	#---------------------------------------------------------------------------------
	#	création de la table
	#---------------------------------------------------------------------------------
	connect = sqlite3.connect('sonde.db')
	x = connect.cursor()
	x.execute('''CREATE TABLE IF NOT EXISTS sonde (
		hostname TEXT,
		cpu INTEGER,
		ram INTEGER,
		swap INTEGER,
		disque INTEGER,
		utilisateur INTEGER,
		processus INTEGER,
		time DATE,
		heure INTEGER
		)''')

	#---------------------------------------------------------------------------------
	#	suppression des anciennes données
	#---------------------------------------------------------------------------------
	x.execute("DELETE FROM sonde WHERE heure != strftime('%H','now')+2")

	#---------------------------------------------------------------------------------
	#	insert valeurs
	#---------------------------------------------------------------------------------
	x.execute("INSERT INTO sonde VALUES(?,?,?,?,?,?,?,?,?+2)",liste)
	for row in x.execute('SELECT * FROM sonde'):
		print (row)

	#---------------------------------------------------------------------------------
	#	récupère les données et les envoie dans le module alert
	#---------------------------------------------------------------------------------
	x.execute("""SELECT cpu, ram, disque, time FROM sonde""")
	data = x.fetchone()
	alert.alert(data[0], data[1], data[2])
	connection.commit()
	connection.close()



def bdd_pars():
	liste = lastAlert.lastAlert()
	connect = sqlite3.connect('Alerte.db')
	c = connect.cursor()
	c.execute('''CREATE TABLE IF NOT EXISTS Alerte (
		Alerte TEXT,
		time DATE
	)''')
	c.execute("DELETE FROM Alerte")

	for row in c.execute('SELECT * FROM Alerte'):
		print(row)
	connect.commit()
	connect.close()