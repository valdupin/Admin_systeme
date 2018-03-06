#!/bin/bash

fichier=$1;
cat /etc/group | while read ligne
do
    groupe=$(echo "$ligne" | cut -d':' -f1);
    users=$(echo "$ligne" | cut -d':' -f4);
    if [ -n "$users" ]
    then
        echo "Il y a au moins un utilisateur dans le groupe $groupe : $users";
    fi
done > $fichier
