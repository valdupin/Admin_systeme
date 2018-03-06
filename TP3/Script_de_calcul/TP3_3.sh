#!/bin/bash

somme=0
for i in $*
do
	somme=`expr $i + $somme`
done
echo "Somme : $somme"
