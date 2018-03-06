#!/bin/bash

cd $1
echo "–------------------------------ fichier txt –------------------------------"
find -type f >ordinaire.txt
cat ordinaire.txt
echo "–------------------------------ repertoire –------------------------------"
find -type d >repertoire.txt 
cat repertoire.txt
echo "–----------------------------- autre fichier –----------------------------"
find -type c> autre.txt 
cat autre.txt

nbrordinaire=`cat ordinaire.txt | wc -l`
echo "nombre de fichier ordinaire :  $nbrordinaire"
nbrrepertoire=`cat ordinaire.txt | wc -l`
echo "nombre de repertoire :  $nbrrepertoire"
