#!/bin/bash

echo "Ecrire 2 nombres séparer d'un espace ou quit pour quitté"
while read arg1 arg2
do
  	  if [ "$arg1" == "quit" ]
	  then
 	    	  echo "End"
      		  exit 1
    	 fi
	 echo "Somme = `expr $arg1 + $arg2`"
	 echo "Difference  = `expr $arg1 - $arg2`"
	 echo "Produit  = `expr $arg1 \* $arg2`"
done
	
