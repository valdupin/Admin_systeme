#!/bin/bash

if [ ! -e "ProgC" ]
then
    mkdir -p "ProgC"
fi

for fichier in `ls *.c`
do 
    mv $fichier `echo ProgC/$fichier | sed 's/\(.*\.\)c/\1cpp/'`
done
