#!/bin/bash

resultat=1
if [[ $1 == +([0-9]) ]]
then 
	for ((i=1;i<=$1;i++))
	do
		resultat=`expr $resultat \* $i`
	done
	echo "fact : $resultat"
fi
if [[ $1 != +([0-9]) ]]
then 
	echo "Non entier"
fi
