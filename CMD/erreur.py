#!/usr/bin/python
# -*- coding: ascii -*-

#Module 2

"""Module de gestion d'erreurs"""

import binascii#pour conversion bin->hex

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
        print('Erreur lors de l\'ouverture du fichier. Est-til dans le bon dossier ? (Code2)')
        return 0

    #On recupere les 4 premiers caracteres
    test=str(binascii.hexlify(test))[2:]

    #On regarde si 424d est present

    #Oui
    if test[0:4]==('424d' or '424D'):
        return 1
    #Non -> erreur
    else:
        print('Mauvaise extention')




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


    #Ouverture du fichier
    try:
        test=open(namefile).read()
    except IOError:
        print('Erreur lors de l\'ouverture du fichier. Est-til dans le bon dossier ? (Code2)')
        return 0
    #Verification du BMP (424d -> BM)


    #Oui
    if test[0:4]==('424d' or '424D'):
        return 1

    #Non -> erreur
    else:
        print('Mauvaise extention')




        #
        #
        #   FIN DU MODULE DE GESTION D'ERREURS
        #
        #