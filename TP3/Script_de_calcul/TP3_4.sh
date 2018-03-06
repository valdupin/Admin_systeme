#!/bin/bash

echo "Entrer la deuxieme valeurs: "
read val2
echo "Quel operation vouelz vous faire ? (+,-,/)"
read operator 
	case "$operator" in
	"+") echo "Somme = `expr $1 + $val2`"
 	;;
	"-") echo "Difference  = `expr $1 - $val2`"
	;;
	"/") echo "Quotient  = `expr $1 / $val2`"
	esac
