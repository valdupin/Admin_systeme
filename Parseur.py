#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
from lxml import html
import requests

#--------------------------------------------------------------------------------------------
#Fonction qui va récupérer la dernier alerte CERT et qui va l'envoyer au moteur de stockage
#--------------------------------------------------------------------------------------------

def parseur():
    page = requests.get('http://www.cert.ssi.gouv.fr/')
    pageHTML = html.fromstring(page.content)

    alert = pageHTML.xpath('//td[@class="ale"]/text()')
    tmp = ""
    for alerte in alert:
        if alerte != " ":
            tmp = alerte[:-1].split('(')
            break

    return tmp





