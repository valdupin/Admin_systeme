#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import time
import sqlite3
import fileinput
import Parseur
import module_crise

#--------------------------------------------------------------------------------------------
#Commande pour la base de données
#   - connext : se connecte à une base de données, la crée si elle existe pas,
#   - execute : permet d'effecguer des actions,
#   - commit : modifie la table, obligatoire après chaque action,
#   - fetchone : permet de récuperer les résultat de la dernière ligne
#--------------------------------------------------------------------------------------------

def bdd():

    #--------------------------------------------------------------------------------------------
    #Nous allons construire la Base de Données, pour cela nous allons récupérerer les fichier 
    #dans le fichier texte remplie avec les sonde et les envoyés dans une liste
    #--------------------------------------------------------------------------------------------
    liste = [None] * 9
    i=0
    with open("ressonde1.txt","r") as f:
        for line in f:
            for word in line.split():
                liste[i]=word
                i += 1
        f.close()


    #--------------------------------------------------------------------------------------------
    #Création Base de données
    #On va créer une base de données avec la librairie "sqlite3", on va indiquer que l'on se
    #trouve à la fin du fichier avec le cursor.
    #Puis nous allons créer les tables seulement si elle n'existe pas
    #--------------------------------------------------------------------------------------------
    connection = sqlite3.connect('sonde.db')
    x = connection.cursor()
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


    #--------------------------------------------------------------------------------------------
    #Supprime les données de plus d'une heure
    #--------------------------------------------------------------------------------------------
    x.execute("DELETE FROM sonde WHERE heure != strftime('%H','now')+2")


    #--------------------------------------------------------------------------------------------
    #Insert les valeurs de la précédente liste dans la bdd et l'affiche après
    #--------------------------------------------------------------------------------------------
    x.execute("INSERT INTO sonde VALUES(?,?,?,?,?,?,?,?,?+2)",liste)
    for row in x.execute('SELECT * FROM sonde'):
        print (row)
	

    #--------------------------------------------------------------------------------------------
    #Va récupérer les données du CPU, RAM, Disque et le temps et l'envoie dans le module de
    #crise. Pour voir l'état des machines
    #--------------------------------------------------------------------------------------------
    x.execute("""SELECT cpu, ram, disque, time FROM sonde""")
    data = x.fetchone()
        
    module_crise.al_crise(data[0], data[1], data[2])

    connection.commit()
    connection.close()


def bdd_pars():

    #--------------------------------------------------------------------------------------------
    #On va récupérer les info grace à la fonction parseur_web qui va se connecter à une page HTML
    #et qui va renvoyer la dernière alert.
    #Cette dernière alerte va être envoyé à la Bdd créer précédement, si la table est déjà crée
    #on supprime l'ancienne alert et on affiche la BDD
    #--------------------------------------------------------------------------------------------
    liste = Parseur.parseur()
    connection = sqlite3.connect('Alerte.db')
    c = connection.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS Alerte (
     Alerte TEXT,
     time DATE
    )''')
    c.execute("DELETE FROM Alerte")

    #c.execute("INSERT INTO Alerte VALUES(?,?)",liste)

    for row in c.execute('SELECT * FROM Alerte'):
    	print (row)

    connection.commit()
    connection.close()
