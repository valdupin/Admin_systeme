#!/bin/bash
# -*- coding: utf-42 -*-

#rm s1RES.txt						#supprime le résultat existant
hostname >> s1RES.txt				#insère le nom de la machine dans le resultat

#---------------------------------------------------------------------------------
#	affiche utilisation ram
#---------------------------------------------------------------------------------
totalRAM=$(grep MemTotal /proc/meminfo | cut -d: -f2 | sed 's/kB//' | sed 's/ //g')
freeRAM=$(grep MemFree /proc/meminfo | cut -d: -f2 | sed 's/kB//' | sed 's/ //g')

unusedRAM=$(echo "scale=2;$freeRAM/$totalRAM*100" | bc -l)
usedRAM=$(echo "scale=2; 100.00 - $unusedRAM" | bc -l) 
echo $usedRAM >> s1RES.txt

#---------------------------------------------------------------------------------
#	mémoire restante : cpu libre - cpu utilisé
#---------------------------------------------------------------------------------
freeCPU=$(top -b -n1 | grep 'Cpu'| cut -d' ' -f11 | sed 's/,/./g')
usedCPU=$(echo "scale=2; 100.00 - $freeCPU" | bc -l) 
echo $usedCPU >> s1RES.txt

#---------------------------------------------------------------------------------
#	affiche utilisation swap memory
#---------------------------------------------------------------------------------
totalSwap=$(grep swapTotalal /proc/meminfo | cut -d: -f2  | sed 's/kB//' | sed 's/ //g')
freeSwap=$(grep swapTotalal /proc/meminfo | cut -d: -f2  | sed 's/kB//' | sed 's/ //g')

unusedSwap=$(echo "scale=2;$freeSwap/$totalSwap*100" | bc -l)
usedSwap=$(echo "scale=2; 100.00 - $unusedSwap" | bc -l)
echo $usedSwap >> s1RES.txt

#---------------------------------------------------------------------------------
#	affiche utilisation disque
#---------------------------------------------------------------------------------
df $PWD | awk '/[0-9]%/{print $(NF-1)}' | sed 's/%//g' >> s1RES.txt

#---------------------------------------------------------------------------------
#	affiche utilisateurs
#---------------------------------------------------------------------------------
who -q	| cut -d: -f2 | tail -1 | sed 's/ //g' >> s1RES.txt

#---------------------------------------------------------------------------------
#	affiche processus actifs
#---------------------------------------------------------------------------------
ps -elf | wc -l >> s1RES.txt

#---------------------------------------------------------------------------------
#	affiche date
#---------------------------------------------------------------------------------
date +%Y-%m-%d:%H:%M:%S>> s1RES.txt