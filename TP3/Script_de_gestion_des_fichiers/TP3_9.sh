#!/bin/bash

for fichier in `find -type f`
do
	echo " $fichier"
	cat $fichier
done
