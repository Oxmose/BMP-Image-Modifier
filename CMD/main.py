#!/usr/bin/python
# -*- coding: ascii -*-

#Main

"""
Module main, base du programme, les importations :

from fonction import *
from compression import *
from info import *
erreur.py est importe dans fonction

Attention pas de protection contre double inclusion !


doivent etre presentent pour son bon fonctionnement

"""

#
#       BMP Image Modifier V0.2
#
#       MAIN avec Menu
#       Pour acceder aux fonctions veuillez vous referer aux fichiers modules
#       fonction.py, erreur.py et compression.py
#
#

from fonction import *#fonction du programme
from compression import *#compression des bmp
from info import *#fonction informations

#Le programme se lance dans un boucle infinie, seul choix=0 peut l'arreter
while 1:
    #Menu
    cls()
    print('                         =======================\n                         |  BMP Image Modifier |\n                         =======================\n=================================================================================')
    print('| 1. Crypter une image BMP (Methode Simple)                                     |')
    print('| 2. Decrypter une image BMP (Methode Simple)                                   |')
    print('| 3. Crypter une image BMP (Methode Avancee)                                    |')
    print('| 4. Decrypter une image BMP (Methode Avancee)                                  |')
    print('| 5. Negatif / Contre negatif                                                   |')
    print('| 6. Diviser une image BMP (Irreversible pour le moment)                        |')
    print('| 7. Saturation des couleurs (+/-)                                              |')
    print('| 8. Compresser/Decompresser une image BMP                                      |')
    print('| 9. Informations                                                               |\n=================================================================================\n')
    print('==============\n| 0. Quitter |\n==============\n\n')

    #Choix du mode
    print('Entrez le mode de fonctionnement voulu : \n----------------------------------------')

    #Entree de l'utilisateur
    choix=int(input())

    #fichier ouvert ou non initialisation
    fichierouvert=0

    #Debut du choix
    if choix!=(0 or 8):
        if 8 > choix > 0:

            # demande du nom de l'image en entree
            print('\n\nRentrez le nom de l\'image BMP a modifier : ')
            namefile = input()

            # demande du nom de l'image
            print('\n\nEntrez le nom du fichier de sortie : ')
            namefileout = input()

            if testextention(namefile):


                #Ouverture du fichier d'entree, avec gestion d'erreur
                try:
                    origin=open(extentionajout(namefile), 'rb')

                    #Pour fermeture on dit que les fichiers sont ouverts
                    fichierouvert=1
                    #Lecture du fichier d'origine
                    fichier=origin.read()

                    #Recuperation du header de l'image
                    header=fichier[0x0:0x36]

                    #on traduit en hex et on enleve le b'
                    image=(str(binascii.hexlify(fichier[0x36:])))[2:]
                    #on enleve le ' a la fin de la chaine
                    image=image[0:len(image)-1]


                except IOError:
                    print('Erreur lors de l\'ouverture du fichier. Est-til dans le bon dossier ? (Code2)')
                    fichierouvert=0
                    choix=42


                #Ouverture ou creation du fichier de sortie, avec gestion d'erreur
                try:
                    final=open(extentionajout(namefileout), 'wb')

                except IOError:
                    print('Erreur lors de l\'ouverture ou la creation du fichier de sortie. Avez vous les droits requis ? (Code3)')
                    origin.close()
                    fichierouvert=0
                    choix=42



            else :
                #Le fichier n'est pas un BMP 42 : choix arbitraire
                choix=42
                fichierouvert=0
        else:
            #Erreur de commander ou choix 9 et la fonction compression gere l'ouverture et la fermeture
            fichierouvert=0

    #Gestion du choix
    if choix==1:
        cryptsmp(header, image , final)

    elif choix==2:
        decryptsmp(header, image , final)

    elif choix==3:
        cryptav(header, image , final)

    elif choix==4:
        decryptav(header, image , final)

    elif choix==5:
        negatif(header, image , final)

    elif choix==6:
        coupe(header, image , final)

    elif choix==7:
        asaic(header, image , final)

    elif choix==8:
        compression()
        
    elif choix==9:
        info()
        
    elif choix==0:
        print('Aurevoir ...')
        break

    elif choix==42:
        print('Erreur, retour au menu')

    else:
        print('Mauvaise commande veuillez reesayer') #en cas d'erreur de saisie

    if fichierouvert==1:
        #on libere les fichiers
        origin.close()
        final.close()

        #message d'arret
        print('Fait.\n')

    #Attente d'une entree pour revenir au menu os.system("pause") n'est pas compatible mac et linux
    input('\n\nAppuyez sur entrer pour revenir au menu...')

#
#
#   FIN DU MAIN
#
#
