#!/usr/bin/env python
# -*- coding: Latin-1 -*-
import email
import time
import datetime


#--------------------------------------------------------------------------------------------
#Fonction qui va permettre de vérifier que 
#--------------------------------------------------------------------------------------------


def alert(process,ram,disque):

    #--------------------------------------------------------------------------------------------
    #Dans cette fonction, on va vérifier si les arguments passer dans la fonction
    #   - process
    #   - ram
    #   - disque
    #   - absence
    #ne sont pas supérieur à 100, si ils sont supérieur on envoi un mail
    #avec le fonction send_mail()
    #--------------------------------------------------------------------------------------------
    
    if process > 99 :
        email.send_mail("Processeur","Error : capacitee maximale du processeur atteinte.")

    if ram > 99 :
        email.send_mail("Ram","Error : capacitee maximale de la memoire vive atteinte.")

    if disque > 99 :
        email.send_mail("Disque","Error : capacitee maximale du disque dur atteint.")


