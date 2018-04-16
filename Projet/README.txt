/* Projet réaliser par MATHIEU Thomas et MOITIE--MATHON Victor *\


/*---------------------------------------------------------------------------------------------*\
/*--------------------------------------  Main :  -------------------------------------------- *\
/*---------------------------------------------------------------------------------------------*\


Main : main.py	
	Librairie  utilisée : 
		- psutil,
		- os, 
		- time,

/*--------------------------------------------------------------------------------------------*\
/*------------------------------------- Etape 1 : ------------------------------------------- *\
/*--------------------------------------------------------------------------------------------*\


1ere sonde : sonde1.sh
	- Tout en commande bash, pas de librairie utulisé.

2eme sonde : sonde2.py
	Librairies utilisées : 
		- psutil, 
		- socket (Pour avoir le nom de la machine), 
		- time.

3eme sonde : sonde3.py
	Librairies utilisées :
		- subprocess, 
		- time.


Ces trois sondes récoltes les mêmes informations : 
	- Nom de la machine, 
	- %CPU utilisé, 
	- %RAM utilisé, 
	- %Swap utilisé, 
	- %DISK utitlisé,
	- nombre d'utilisateur connecté, 
	- nombre de processus, 
	- la date et l'heure.
	
Ces données sont envoyées dans un fichier txt.



/*--------------------------------------------------------------------------------------------*\
/*------------------------------------- Etape 2 : ------------------------------------------- *\
/*--------------------------------------------------------------------------------------------*\

Stockage de données : bdd.py
	Librairies utilisées : sqlite3 , fileinput , time

Le module ouvre le fichier txt et prend les données de la sonde pour les inserer dans la base de donner crée à l'aide sqlite3.
Le fichiers .db est stocker sur disque dur.
Une requete permet de suprimer les données datant de plus d'une heure.
L'ajout d'une nouvelle machine nécessite aucune modification.



Parseur web : parseur.py
	Librairies utilsées : lxml , requests
Recupere et envoie a la bdd la derniere alerte du site http://www.cert.ssi.gouv.fr/

