#!/bin/bash

heure=`date | awk '{print $5}' | awk -F:  '{print $1}'` 
if [ $heure -lt 12 ] 
then 
	echo "Bonjour !"
elif [ $heure -lt 17 ] 
then
	 echo "Bon après-midi !"
else 
	echo "Bonsoir !" 
fi 
