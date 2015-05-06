#!/usr/bin/python
# -*- coding: utf-8 -*-

#Module 2

"""Module de gestion d'erreurs"""

import binascii#pour conversion bin->hex
import tkinter.messagebox

#
#
#   Gestion d'erreurs de BMP Image Modifier
#
#




#                           #
#   Pour les fichier BMP    #
#                           #

#Test de l'extension physique seule

def extentionajout(nommodifier):
    """Fonction ajout de l'extention, parametre : nom du fichier"""


    #Oui presente
    if nommodifier.endswith('.bmp' or '.BMP'):
        print('\n')
    #Non -> on lui rajoute
    else:
        nommodifier+='.bmp'

    #On retourne le nom avec l'extention
    return nommodifier




#Test avec lecture du code HEX
def testextention(namefile):
    """Fonction  de teste du type de fichier, parametre : nom du fichier avec extention"""

    #Test de l'extention physique
    namefile=extentionajout(namefile)

    #Verification du BMP (424d -> BM)

    #Ouverture du fichier
    try:
        test=open(namefile, 'rb').read()
    except IOError:

        tkinter.messagebox.showerror('Attention !', "Erreur lors de l\'ouverture du fichier. Est-il dans le bon dossier ? (Code 2)")
        return 0

    #On recupere les 4 premiers caracteres
    test=str(binascii.hexlify(test))[2:]

    #On regarde si 424d est present(BM)

    print (int(test[28:30]))
    #Oui
    if test[0:4]==('424d' or '424D'):
        if test[28:30]=='28':
            return 1
        else:
            tkinter.messagebox.showerror('Mauvaise extention, ou le BMP n\'est pas un 24 bits')
    #Non -> erreur
    else:
        tkinter.messagebox.showerror('Mauvaise extention, ou le BMP n\'est pas un 24 bits')




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
        if test[28:30]=='28':
            return 1
        else:
            tkinter.messagebox.showerror('Mauvaise extention, ce fichier compréssé n\'est pas un AFE')
    #Non -> erreur
    else:
        tkinter.messagebox.showerror('Mauvaise extention, ce fichier compréssé n\'est pas un AFE')



        #
        #
        #   FIN DU MODULE DE GESTION D'ERREURS
        #
        #