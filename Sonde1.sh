#!/bin/bash
# -*- coding: utf-42 -*-
rm ressonde1.txt

#--------------------------------------------------------------------------------------------
#Envoi le nom de la machine dans le fichier texte
#--------------------------------------------------------------------------------------------
hostname >> ressonde1.txt

#Nombre cpu 
#cat /proc/cpuinfo | grep "physical id" | sort -u | wc -l >> ressonde1.txt
#Nombre cores cpu
#cat /proc/cpuinfo | grep "siblings" | sort -u | cut -d: -f2 | sed 's/ //g' >> ressonde1.txt

#--------------------------------------------------------------------------------------------
#On va prendre le CPU libre et on le soustraire au CPU utilisé
#Ensuite on va tout envoyer dans le fichier texte
#--------------------------------------------------------------------------------------------
cpuLibre=$(top -b -n1 | grep 'Cpu'| cut -d' ' -f11 | sed 's/,/./g')
cpuUtilise=$(echo "scale=2; 100.00 - $cpuLibre" | bc -l) 
echo $cpuUtilise >> ressonde1.txt

#--------------------------------------------------------------------------------------------
#On va calculer la RAM total
#--------------------------------------------------------------------------------------------
ramTotal=$(grep MemTotal /proc/meminfo | cut -d: -f2 | sed 's/kB//' | sed 's/ //g')	


#--------------------------------------------------------------------------------------------
#Permet d'obtenir la ram disponible
#--------------------------------------------------------------------------------------------
ramDisponible=$(grep MemFree /proc/meminfo | cut -d: -f2 | sed 's/kB//' | sed 's/ //g')

#--------------------------------------------------------------------------------------------
#Permet d'obtenir la RAM libre et d'envoyer uniquement la RAM utilise dans le fichier 
#texte
#--------------------------------------------------------------------------------------------
ramLibre=$(echo "scale=2;$ramDisponible/$ramTotal*100" | bc -l)
ramUtilise=$(echo "scale=2; 100.00 - $ramLibre" | bc -l) 
echo $ramUtilise >> ressonde1.txt

#--------------------------------------------------------------------------------------------
#Permet d'obtenir le swap total et le swap disponible pour l'utlisateur et l'envoi dans 
#le fichier texte
#--------------------------------------------------------------------------------------------
swapTotal=$(grep swapTotalal /proc/meminfo | cut -d: -f2  | sed 's/kB//' | sed 's/ //g') 
swapDisponible=$(grep swapTotalal /proc/meminfo | cut -d: -f2  | sed 's/kB//' | sed 's/ //g') 

#--------------------------------------------------------------------------------------------
#Permet d'obtenir le swap libre et utilisé et envoyer dans le fichier texte le swap
#utlisé par l'utilisateur
#--------------------------------------------------------------------------------------------
swapLibre=$(echo "scale=2;$swapDisponible/$swapTotal*100" | bc -l)
swapUtilise=$(echo "scale=2; 100.00 - $swapLibre" | bc -l)
echo $swapUtilise >> ressonde1.txt

#--------------------------------------------------------------------------------------------
#DF permet de connaitre la taille total du répertoire
#On va donc envoyer la memoire du disque dans le fichier texte
#--------------------------------------------------------------------------------------------
df $PWD | awk '/[0-9]%/{print $(NF-1)}' | sed 's/%//g' >> ressonde1.txt

#--------------------------------------------------------------------------------------------
#Permet de connaitre combien d'utilisateur présent, et l'envoi dans le fichier texte
#--------------------------------------------------------------------------------------------
who -q	| cut -d: -f2 | tail -1 | sed 's/ //g' >> ressonde1.txt

#--------------------------------------------------------------------------------------------
#PS permet de connaître tous les processus qui sont en activités
#On envoi tout dans le fichier texte
#--------------------------------------------------------------------------------------------
ps -elf | wc -l >> ressonde1.txt

#--------------------------------------------------------------------------------------------
#Permet d'obtenir la date du sondage de la sonde en bash
#--------------------------------------------------------------------------------------------
date +%Y-%m-%d:%H:%M:%S>> ressonde1.txt

#--------------------------------------------------------------------------------------------
#Permet d'obtenir seulement l'heure de la sonde
#--------------------------------------------------------------------------------------------
date +%H  >> ressonde1.txt

