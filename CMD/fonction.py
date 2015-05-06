#!/usr/bin/python
# -*- coding: ascii -*-

#Module 1

"""
Fonction du programme BMP Image Modifier, peut fonctionner en standalone
a condition d'etre repris dans un programme skelette
"""
import random#Pour cryptagesmp()
import os#Pour clear console
from dimension import *


#
#
#   Fonctions de BMP Image Modifier
#
#



#Efface la console pour plus d'esthetique
def cls():
    """
        Efface la console
    """
    #Recupere le system pour savoir si on utilise cls pour NT -> Windaube ou clear -> Base Unix
    os.system(['clear','cls'][os.name == 'nt'])



#
#   Fonction Eclaicir ou Assombrir
#

def asaic(header, image , final):
    """Fonction de saturation, parametres : header de l'image, corps de l'image
    et nom du fichier final
    """

    #Initialisation

    k=0#Compteur pour boucle
    couleurmodif=''#Nouvelle couleur apres modfication

    #recuperation de la taille de la partie a modifier
    longueurimage=len(image)

    #Appiclation des modifications
    stop=0

    while stop==0:

        #Demande su choix
        print('\n\n| Que voulez vous ? |')
        print('1. Eclaicir l\'image')
        print('2. Assombrir l\'image')

        #Entre utilisateur
        choix=int(input())


        #Fonce l'image
        if choix==2:

            #Tant que longueur de l'image
            while k!=longueurimage:

                #On recupere un nibble de la composant RGB d'un pixel

                #Conversion en decimal de la valeur de ce nibble
                newcoul=int(image[k:k+2], 16)

                #Si nibble un peu plus fonce que la moyenne on le fonce en noir
                if newcoul<128:
                    newcoul='00'
                #Sinon il reste le meme
                else:
                    newcoul=hex(newcoul)[2:]

                #On rajoute a la chaine finale
                couleurmodif += newcoul

                k+=2

                #Fin
            stop=1


        #Eclaircit l'image
        elif choix==1:

            #Tant que longueur de l'image
            while k!=longueurimage:

                #Conversion en decimal de la valeur de ce nibble
                newcoul=int(image[k:k+2], 16)

                #Si nibble un peu plus fonce que la moyenne on l'eclaicit en blanc
                if newcoul>=128:
                    newcoul='FF'


                else:
                    #Lors de la conversion on recup 0x1 si 1 ou 0xa si 10 alors pour repasser en hex voulu on ajoute 0 et on enlece 0x
                    if newcoul<=15:
                        newcoul='0'+(hex(newcoul)[2:])
                    else:
                        newcoul=hex(newcoul)[2:]

                #Sinon il reste le meme

                couleurmodif+=newcoul
                #Sinon il reste le meme
                k+=2

            stop=1

        else :
            print('Mauvaise commande')


    #Ecriture dans le fichier
    final.write(header+bytes.fromhex(couleurmodif))#ecriture dans le fichier



#
#   Fonction de cryptage avance
#

def cryptav(header, image , final):
    """Fonction de cryptage avance, parametres : header de l'image, corps de l'image
    et nom du fichier final
    """

    #Recuperation des dimensions de l'image'
    ligne=dimensionligne(header)
    colone=dimensioncolone(header)

    #Recuperation de la longueur de la chaine corps de l'image
    longueurimage=len(image)


    #
    #   Debut du cryptage
    #


    #Changement de couleur

    k=0
    couleurmodif=''

    while k<longueurimage:

        couldec=int(image[k:k+2], 16)

        if couldec<128:

            couldec+=128
            newcoul=hex(couldec)[2:]

        else:

            couldec-=128
            if couldec<=15:
                newcoul='0'+(hex(couldec)[2:])
            else:
                newcoul=hex(couldec)[2:]

        couleurmodif+=newcoul

        k+=2

    #Second decallage
    k=0
    decal1=''
    for i in range(ligne):
        if len(couleurmodif[(6*colone)*k:(k+1)*(6*colone)])<6*colone:
            decal1+=couleurmodif[(6*colone)*k:(k+1)*(6*colone)]
            break
        else:
            for j in range(colone):
                decal1+='010101'
                decal1+=couleurmodif[(6*colone)*k:(k+1)*(6*colone)]
                k+=1

    #Double du second decallage
    k=0
    decal2=''
    for i in range(ligne):
        if len(decal1[(6*colone)*k:(k+1)*(6*colone)])<6*colone:
            decal2+=decal1[(6*colone)*k:(k+1)*(6*colone)]
            break
        else:
            for j in range(colone):
                decal2+='101010'
                decal2+=decal1[(6*colone)*k:(k+1)*(6*colone)]
                k+=1


    #Ajout de parasites
    k=0

    newimage2decfinal=''
    while k<len(decal2):
        newimage2decfinal+=decal2[k:k+6]+"AFEDBEF"
        k+=6


    #Ecriture dans le fichier
    if len(newimage2decfinal)%2!=0:
        final.write(header+bytes.fromhex(newimage2decfinal+'0'))
    else:
        final.write(header+bytes.fromhex(newimage2decfinal))



#
#   Fonction de decryptage avance
#
def decryptav(header, image , final):
    """Fonction de decryptage avance, parametres : header de l'image, corps de l'image
    et nom du fichier final
    """

    #Recuperation des dimensions de l'image
    ligne=dimensionligne(header)
    colone=dimensioncolone(header)

    #longueurimage de la partie a crypter
    longueurimage=len(image)


    #on enleve le afedbef dans les intervals donnee par la compretion
    imagededec1=''
    i=0
    while i<=longueurimage:
        if image[i:i+7]=="afedbef":
            i+=7
        else:
            imagededec1+=image[i:i+6]
            i+=6

    #Second decallage-inverse (Deux foix)
    k=0
    newimagedec2=''

    for i in range(ligne+1):
        newimagedec2+=imagededec1[((6*colone)+6)*k:(k+1)*((6*colone)+6)][6:]
        k+=1

    k=0
    imagededec=''

    for i in range(ligne):
        imagededec+=newimagedec2[((6*colone)+6)*k:(k+1)*((6*colone)+6)][6:]
        k+=1


    #changement de couleur
    k=0
    couleurmodif=''

    while k<len(imagededec):

        couldec=int(imagededec[k:k+2], 16)

        if couldec<128:

            couldec+=128
            newcoul=hex(couldec)[2:]

        else:
            couldec-=128
            if couldec<=15:
                newcoul='0'+(hex(couldec)[2:])
            else:
                newcoul=hex(couldec)[2:]

        couleurmodif+=newcoul

        k+=2


    #fin de cryptage
    final.write(header+bytes.fromhex(couleurmodif))#ecriture dans le fichier



#
#   Fonction de negatif image
#

def negatif(header, image, final):
    """Fonction de negatif, parametres : header de l'image, corps de l'image
    et nom du fichier final
    """

    #longueurimage de la partie modifier
    longueurimage=len(image)

    #Debut application negatif
    newim= ''
    i=0
    while i<longueurimage:

        #On convertit la veleur d'une composante R,G ou B en decimal
        val=int(image[i:i+2], 16)

        #On prend sa couleur complementaire (negatif)
        coulpart=255-val

        if coulpart<= 15:
            #La convertion en decimal enleve le 0 aux dizaines on doit le rajouter, on enleve le 0x de la convertion
            newim+="0"+(hex(coulpart)[2:])
        else :
            #on enleve le 0x de la convertion
            newim+=(hex(coulpart)[2:])

        i+=2

    # Fin de negatif

    #Ecriture dans le fichier
    final.write(header+bytes.fromhex(newim))



#
#   Fonction de division de l'image
#

def coupe(header, image , final):
    """Fonction de division, parametres : header de l'image, corps de l'image
    et nom du fichier final
    """

    #longueurimage de la partie a diviser
    longueurimage=len(image)

    #
    #   Application de la division
    #

    i=0
    m=6

    diviser=''
    while i<longueurimage:
        diviser+=image[i:i+6]
        i+=12

    while m<longueurimage:
        diviser+=image[m:m+6]
        m+=12

    i=0
    m=6
    newim=''
    while i<longueurimage:
        newim+=diviser[i:i+6]
        i+=12

    while m<longueurimage:
        newim+=diviser[m:m+6]
        m+=12

    # Fin de la division

    #Ecriture dans le fichier
    final.write(header+bytes.fromhex(newim))



#
#   Fonction de cryptage simple (steganographie)
#

def cryptsmp(header, image , final):
    """Fonction de cryptage simple, parametres : header de l'image, corps de l'image
    et nom du fichier final
    """

    #Initialisation
    newimage=''

    #longueur de la chaine de la partie a crypter
    longueurimage=len(image)

    #
    #   Debut du cryptage
    #
    for i in range(longueurimage):

        #Generation d'une couleure aleatoire
        r=int(random.randint(0,9))
        r=hex(r)[2:]
        newimage+=r

    # Fin de cryptage

    #ecriture dans le fichier
    final.write(header+bytes.fromhex(newimage+image))



#
#   Fonction de decryptage simple
#

def decryptsmp(header, image , final):
    """Fonction de decryptage simple, parametres : header de l'image, corps de l'image
    et nom du fichier final
    """


    #longueurimage de la partie a decrypter
    longueurimage=len(image)

    #
    #   Appiclation du decryptage
    #
    #On recupere tout apres les nibbles ajout?s au cryptage
    moitier=int(longueurimage/2)

    if longueurimage%2!=0:
        moitier+=longueurimage%2

    # Fin Decryptage

    #ecriture dans le fichier
    final.write(header+bytes.fromhex(image[moitier:]))

#
#
#   FIN DU MODULE FONCTIONS
#
#
