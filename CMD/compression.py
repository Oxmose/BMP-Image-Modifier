#!/usr/bin/python
# -*- coding: ascii -*-

#Module 4

"""Module de compression"""

import binascii#pour conversion bin->hex
from erreur import *#gestion d'erreur


#
#
#   Compression de BMP Image Modifier
#
#


def compression() :
    """Fonction de compretion aucun parametre requis, standalone"""

    origin=None
    final=None
    #Demande du choix
    print('\n\nVoulez vous ?')
    print('_______________')
    print('1. Compresser une image.')
    print('2. Decompresser une image.')

    #Entree utilisateur
    choix=int(input())

    if choix==1:

    #                             #
    #                             #
    #   Fonction de compression   #
    #                             #
    #                             #

        # Demande du nom de l'image d'entree
        print('\n\nRentrez le nom de l\'image BMP a compresser : ')
        namefile = input()

        print('Le fichier de sortie sera au format .afe')

        #Teste de l'extention du fichier
        if testextention(namefile):

            try:
                #Ouverture du fichier d'entree
                origin=open(extentionajout(namefile), 'rb')

            except IOError:
                print('Erreur lors de l\'ouverture du fichier. Est-til dans le bon dossier ? (Code2)')


            #Ouverture ou creation du fichier de sortie
            try:
                final=open((extentionajout(namefile))[:-4]+'.afe', 'w')

            except IOError:
                print('Erreur lors de l\'ouverture ou la creation du fichier de sortie. Avez vous les droits requis ? (Code3)')
                origin.close()

        else:

            #Erreur lors de l'ouverture due a l'extention
            print('Ce n\'est pas un BMP.')
            return 0


        #Lecture du fichier d'entree
        fichier=origin.read()


        #
        #Gestion du HEADER
        #

        #Recuperation du header de l'image
        header=fichier[0x0:0x36]

        #On traduit en hex et on enleve le b'
        header=(str(binascii.hexlify(header)))[2:]
        #On enleve le ' a la fin de la chaine
        header=header[0:len(header)-1]


        #
        #Gestion de l'image (couleures)
        #

        #On traduit en hex et on enleve le b'
        image=(str(binascii.hexlify(fichier[0x36:])))[2:]
        #On enleve le ' a la fin de la chaine
        image=image[0:len(image)-1]

        #Recuperation de la longueure de la chaine contenant les couleures
        longueurimage=len(image)

        #Declaration des variables

        newim= ''#Chaine contenant la nouvelle image
        k=0#Compteur pour le calcul de repetition du motif

        charante=image[0:6]#Le premier caractere doit-etre egale au precedent

        #
        #Debut le l'algorithme de compression
        #
        i=0

        while i<longueurimage:

            #Lecture du caratere au ieme tour de boucle
            charlu=image[i:i+6]#Caractere lu dans un tour de boucle

            #on le conpare au nibble precedent
            if charlu==charante:
                k+=1

            #Si il n'est pas egale on stocke le nombre de fois que le nibble se repete dans un variable
            else:
                #||Montre la separation entre deux motifs de nibbles
                newim+=charante+(hex(k))[2:]+'|'

                #Reinitialisation du k fois nombre de nibbles
                k=1

                #On stocke un nouveau caractere
                charante=charlu
            i+=6

        #Un dernier tout de boucle
        newim+=charante+(hex(k))[2:]+'|'

        #Ecriture dans le fichier de sortie
        final.write(header+newim)
        print('\nFait !\n\n')

    else:

    #                             #
    #                             #
    #   Fonction de decompression #
    #                             #
    #                             #


        # Demande du nom de l'image d'entre compresse
        print('\n\nRentrez le nom de l\'image BMP a decompresser : ')
        namefile = input()

        print('Le fichier de sortie sera au format .bmp')

        #Test de l'extension du fichier
        if testextentionafe(namefile):

            #Ouverture du fichier d'entree
            origin=open(extentionajoutafe(namefile))

            #Ouverture ou creation du fichier de sortie
            final=open((extentionajoutafe(namefile))[:-4]+'decomp.bmp', 'wb')

        else:

            #Erreur d'extension
            print('Ce n\'est pas un AFE.')

        #Lecture du fichier d'origine
        fichier=origin.read()

        #Recuperation du header
        header=fichier[0:108]

        #Recuparation de la partie image
        image=fichier[108:]

        #Recuperation de la longueur de la chaine de caractere image
        longueurimage=len(image)


        #Initalisation des variables

        newim= ''#Chaine contenant la nouvelle image
        m=0#Compteur decrypteur
        v=0#la variable i n'est pas assez flexible on doit en creer une autre pour faire un v+=2
        nombrecoul=''#Nombre de repetition du nobble en hex
        coul=''#Nibble

        #Debut de l'algorithme de decompression
        for i in range(longueurimage):

            #On recupere la valeur du nibble
            if m==0:

                #Recuperation de la valeure du vieme nibble
                coul=image[v:v+6]

                #On informe quelle a ete recupere
                m=1

                #Incremente pour passer au caractere suivant
                v+=6
            else:

                #On a le nibble on verrifie combien de fois il apparait

                #Si || -> separation donc on arrete de compter le nombre de fois que le nibble se repete
                if image[v:v+1]=='|':

                    #On convertir en decimal de nombre de fois que le nibble apparait
                    k=int(nombrecoul, 16)

                    #On stocke le motif complet
                    newim+=coul*k

                    #On doit recuperer un nouveau motif
                    m=0

                    #remise a zero des variables
                    nombrecoul=''


                #Sinon on continu a compte k le nombre de fois que le motif se repete
                else:
                    #On compte
                    nombrecoul+=image[v:v+1]

                #++
                v+=1

        #Ecriture dans le fichier de sortie
        final.write(bytes.fromhex(header+newim))
        print('\nFait !\n\n')




    #Fermeture de fichiers
    final.close()
    origin.close()

    #
    #
    #   FIN DU MODULE COMPRESSION
    #
    #