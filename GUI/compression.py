#!/usr/bin/python
# -*- coding: utf-8 -*-

#Module 4

"""Module de compression GUI"""

import binascii#pour conversion bin->hex
from erreur import *#gestion d'erreur
from tkinter import *
import tkinter.messagebox

#
#
#   Compression de BMP Image Modifier
#
#


def compression() :
    """Fonction de compretion aucun parametre requis, standalone"""

    #Generation de la fenetre
    global compwin
    compwin=Toplevel(bg='white')
    compwin.grab_set()
    compwin.focus_set()
    compwin.title('Que faire ?')
    compwin.geometry("300x50")
    compwin.resizable(False,False)

    #Label de demande
    quest_lbl=Label(compwin, text="Que voulez-vous faire ?", bg='white')
    quest_lbl.pack(side=TOP)

    #Bouttons de demande
    infocomp_bt=Button(compwin, text="Compresser une image", command=diagopencomp)
    infocomp_bt.pack(side=LEFT)
    infodecomp_bt=Button(compwin, text="Décompresser une image", command=diagopendecomp)
    infodecomp_bt.pack(side=RIGHT)




#
#   Fin fenetre principale
#



#
# Si decompression
#
def diagopendecomp():
    """
    Boite de dialogue pour le fichier à décompresser
    """

    global namefile
    global compfilenamewin
    global compwin

    #On detruit la fenetre précédente
    compwin.destroy()

    #Generation de la fenetre
    compfilenamewin=Toplevel(bg='white')
    compfilenamewin.grab_set()
    compfilenamewin.focus_set()
    compfilenamewin.title('Nom du fichier')
    compfilenamewin.geometry("300x65")
    compfilenamewin.resizable(False,False)

    # Demande du nom de l'image d'entre compresse
    quest_lbl=Label(compfilenamewin, text="Quel fichier modifier ?", bg='white')
    quest_lbl.pack(side=TOP)

    namefile = StringVar()#Variable globale
    ligne_texte = Entry(compfilenamewin, textvariable=namefile, width=30)
    ligne_texte.pack()

    comp_bt=Button(compfilenamewin, text="OK", command=decompressalgo)
    comp_bt.pack(side=LEFT)



#
# Si compression
#
def diagopencomp():
    """
    Boite de dialogue pour le fichier à compresser
    """

    global namefile
    global compfilenamewin2

    global compwin
    compwin.destroy()
    #Generation de la fenetre
    compfilenamewin2=Toplevel(bg='white')
    compfilenamewin2.grab_set()
    compfilenamewin2.focus_set()
    compfilenamewin2.title('Nom du fichier')
    compfilenamewin2.geometry("300x65")
    compfilenamewin2.resizable(False,False)

    # Demande du nom de l'image d'entre compresse
    quest_lbl=Label(compfilenamewin2, text="Quel fichier modifier ?", bg='white')
    quest_lbl.pack(side=TOP)

    namefile = StringVar()#Variable globale
    ligne_texte = Entry(compfilenamewin2, textvariable=namefile, width=30)
    ligne_texte.pack()

    comp_bt=Button(compfilenamewin2, text="OK", command=compressalgo)
    comp_bt.pack(side=LEFT)





#                             #
#                             #
#   Fonction de decompression #
#                             #
#                             #
def decompressalgo():
    """
    Fonction de décompression, aucun paramètres
    """

    global compfilenamewin
    compfilenamewin.destroy()

    tkinter.messagebox.showinfo("Attention !", "Le fichier de sortie sera au format .bmp")

    global namefile
    namefile=namefile.get()


    origin=None
    final=None

    #Test de l'extension du fichier
    if testextentionafe(namefile):

        #Ouverture du fichier d'entree
        origin=open(extentionajoutafe(namefile))

        #Ouverture ou creation du fichier de sortie
        final=open((extentionajoutafe(namefile))[:-4]+'decomp.bmp', 'wb')

    else:

        #Erreur d'extension
        tkinter.messagebox.showinfo("Attention !", "Ce n'est pas un AFE !")

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

        #On recupere la valeur du pixel
        if m==0:

            #Recuperation de la valeure du vieme pixel
            coul=image[v:v+6]

            #On informe quelle a ete recupere
            m=1

            #Incremente pour passer aux caracteres suivants
            v+=6
        else:

            #On a le nibble on verrifie combien de fois il apparait

            #Si || -> separation donc on arrete de compter le nombre de fois que le pixel se repete
            if image[v:v+1]=='|':
                if image [v+6:v+7]=="|" or image[v+12:v+13]=="|":
                    newim+=coul
                    m=0
                    
                else:

                    #On convertir en decimal de nombre de fois que le nibble apparait
                    k=int(nombrecoul, 16)

                    #On stocke le motif complet
                    newim+=coul*k

                    #On doit recuperer un nouveau nibble
                    m=0

                    #remise a zero des variables
                    nombrecoul=''

            #Sinon on continu a compte k le nombre de fois que le nibble se repete
            else:
                #On compte
                nombrecoul+=image[v:v+1]

            #++
            v+=1

    #Ecriture dans le fichier de sortie

    final.write(bytes.fromhex(header+newim))
    #Fermeture de fichiers
    final.close()
    origin.close()

    tkinter.messagebox.showinfo("Fait !", "Success !")



#                             #
#                             #
#   Fonction de compression   #
#                             #
#                             #
def compressalgo():
    """
    Fonction de compression, aucun paramètres
    """

    global compfilenamewin2
    compfilenamewin2.destroy()

    tkinter.messagebox.showinfo("Attention !", "Le fichier de sortie sera au format .afe")

    origin=None
    final=None

    #On recupère le nom de fichier
    global namefile
    namefile=namefile.get()

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
            #Si ne pixel ne se répète que 3 fois
            if k<1:

                for vk in range(k):
                    newim+=charante+(hex(k))

                newim+='|'
                k=1
                charante=charlu
                
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

    #Fermeture de fichiers
    final.close()
    origin.close()

    tkinter.messagebox.showinfo("Fait !", "Success !")




    #
    #
    #   FIN DU MODULE COMPRESSION
    #
    #
