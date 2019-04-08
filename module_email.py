#!/usr/bin/env python
import smtplib
import sys
import os
from getpass import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#parametre mail
def param_mail():
    
    print("Enregistrer les nouveaux parametres emails:")
     
    print("Votre adresse:")
    From = sys.stdin.readline()
    print("Destinataire")
    To = sys.stdin.readline()
    print("Votre mot de passe:")
    Mdp = sys.stdin.readline()
    fichier = open("paramail.txt", "w")
    fichier.write(From)
    fichier.write(To)
    fichier.write(Mdp)
    print("Parametre sauvegarde")
    fichier.close()
    

#Creation serveur mail
def send_mail(typ,mes):
    fichier = open("paramail.txt", "r")
    user = fichier.read().split('\n')
    
    if os.path.getsize("paramail.txt") == 0:
        print("Vos parametre sont vides")
        param_mail()
        
    msg = MIMEMultipart()
    msg['From'] = user[0]
    msg['To'] = user[1]
    msg['Subject'] = 'Alerte:' + typ
    

    mailserver = smtplib.SMTP_SSL('smtpz.univ-avignon.fr:465')
    message = mes
    msg.attach(MIMEText(message))

    mailserver.ehlo()
    mailserver.login(user[0], user[2])

    #envoie mail
    mailserver.sendmail(user[0], user[1], msg.as_string())   
    mailserver.close()
    print "Un mail a ete envoye %s" %(msg['To'])
    fichier.close()
