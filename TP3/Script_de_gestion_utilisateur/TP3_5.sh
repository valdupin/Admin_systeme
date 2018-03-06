#!/bin/bash

cat /etc/passwd | cut -d':' -f1 | while read users ;
do
	groupe=$(groups $users);
	echo "$users est du groupe : $groupe" ;
done
