#!/usr/bin/python
# -*- coding: utf-8 -*-

#Module 1

"""Module de gestion d'erreurs"""

import tkinter.messagebox

#
#
#   Gestion d'erreurs de AFE Reader
#
#



#                           #
#   Pour les fichier AFE    #
#                           #

#Test de l'extension physique seule

def extentionajoutafe(nommodifier):
    """Fonction ajout de l'extention, parametre : nom du fichier"""


    #Oui
    if nommodifier.endswith('.afe' or '.AFE'):
        print('\n')

    #Non -> on lui rajoute
    else:
        nommodifier+='.afe'

    #On retourne le nom avec l'extention
    return nommodifier

#Test de l'extention physique en HEX



def testextentionafe(namefile):
    """Fonction  de teste du type de fichier, parametre : nom du fichier avec extention"""


    #Test de l'extention physique
    namefile=extentionajoutafe(namefile)

    try:
        test=open(namefile).read()
    except IOError:

        tkinter.messagebox.showerror('Attention !', "Erreur lors de l\'ouverture du fichier. Est-il dans le bon dossier ? (Code 2)")
        return 0


    #Verification du BMP (424d -> BM)

    #On recupere les 4 premier caracteres

    #Oui
    if test[0:4]==('424d' or '424D'):
        return 1

    #Non -> erreur
    else:
        tkinter.messagebox.showerror('Mauvaise extention')



        #
        #
        #   FIN DU MODULE DE GESTION D'ERREURS
        #
        #