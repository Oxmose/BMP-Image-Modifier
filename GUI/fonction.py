#!/usr/bin/python
# -*- coding: utf-8 -*-

#Module 1

"""
Fonction du programme BMP Image Modifier, peut fonctionner en standalone
a condition d'etre repris dans un programme skelette
"""
import random#Pour cryptagesmp()
from tkinter import *
import tkinter.messagebox
from dimension import *

#
#
#   Fonctions de BMP Image Modifier
#
#

global verifoka
verifoka=0


#Pour passer les var de la diag aux fonction
def passagevar(verifok, headerfile, imagefile, finalname):
    """
    La fonction récupère les variable envoyé par erreur, utilisation
    due a la mise en place de Tkinter, c'est très moche, paramèrtre :
    verifok, headerfile, imagefile, finalname
    """
    global verifoka
    verifoka=verifok

    if verifoka:
        global header, image , final
        header=headerfile
        image=imagefile
        final=finalname
    else:
        tkinter.messagebox.showerror('Erreur !', "Vous n'avez pas spécifié de fichier (Code 4)")



#
#   Remize a zero
#
def end():
    """
    Fin, remise a zero, aucun parametres
    """
    global header, image , final, verifoka
    header=''
    image=''
    verifoka=0



#
#   Fonction Eclaicir ou Assombrir
#
def choix1():
    """
    Si on clique sur éclaircir
    """
    global choixwin
    choixwin.destroy()

    global choix
    choix=1

    asaic()

def choix2():
    """
    Si on clique sur assombrir
    """

    global choixwin
    choixwin.destroy()

    global choix
    choix=2

    asaic()

def choixassaic():
    """
    La fonction assombrir ou eclaircir fais son travail en fonction de
    choix, cette variable globale est donnée par cette fonction pour
    appliquer la transphormation voulue.
    """
    global choixwin

    #Generation de la fenetre
    choixwin=Toplevel(bg='white')
    choixwin.grab_set()
    choixwin.focus_set()
    choixwin.title('Ouverture du fichier')
    choixwin.geometry("150x25")
    choixwin.resizable(False,False)


    bt_ass=Button(choixwin, text='Assombrir', command=choix2)
    bt_ass.pack(side=LEFT)
    bt_ec=Button(choixwin, text='Eclaircir', command=choix1)
    bt_ec.pack(side=RIGHT)

    choixwin.mainloop()

def asaic():
    """Fonction de saturation, parametres : header de l'image, corps de l'image
        et nom du fichier final
    """
    global verifoka
    global choix

    if verifoka:

        #Initialisation
        global header, image , final, choix

        k=0#Compteur pour boucle
        couleurmodif=''#Nouvelle couleur apres modfication

        #recuperation de la taille de la partie a modifier
        longueurimage=len(image)


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

                #FIN


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

                #FIN

        else:
            tkinter.messagebox.showerror('Erreur !', "Erreur dans durant l'execution du logiciels")




        #Ecriture dans le fichier
        final.write(header+bytes.fromhex(couleurmodif))#ecriture dans le fichier
        final.close()
        tkinter.messagebox.showinfo("Fait !", "Success !")

        #FIN
        end()
    else:
        tkinter.messagebox.showerror('Erreur !', "Vous n'avez pas spécifié de fichier (Code 4)")


#
#   Fonction de cryptage avance
#
def cryptav():

    """Fonction de cryptage avance, parametres : header de l'image, corps de l'image
        et nom du fichier final
        """

    global verifoka

    if verifoka:


        global header, image , final

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

        final.close()
        tkinter.messagebox.showinfo("Fait !", "Success !")

        #FIN
        end()
    else:
        tkinter.messagebox.showerror('Erreur !', "Vous n'avez pas spécifié de fichier (Code 4)")


#
#   Fonction de decryptage avance
#
def decryptav():

    """Fonction de decryptage avance, parametres : header de l'image, corps de l'image
        et nom du fichier final
        """

    global verifoka

    if verifoka:



        global header, image , final

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
        final.close()
        tkinter.messagebox.showinfo("Fait !", "Success !")

        #FIN
        end()

    else:
        tkinter.messagebox.showerror('Erreur !', "Vous n'avez pas spécifié de fichier (Code 4)")


#
#   Fonction de negatif image
#
def negatif():

    """Fonction de negatif, parametres : header de l'image, corps de l'image
        et nom du fichier final
        """

    global verifoka

    if verifoka:



        global header, image , final

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
        final.close()

        tkinter.messagebox.showinfo("Fait !", "Success !")

        #FIN
        end()

    else:
        tkinter.messagebox.showerror('Erreur !', "Vous n'avez pas spécifié de fichier (Code 4)")


#
#   Fonction de division de l'image
#
def coupe():

    """Fonction de division, parametres : header de l'image, corps de l'image
        et nom du fichier final
        """

    global verifoka

    if verifoka:



        global header, image , final

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
        final.close()

        tkinter.messagebox.showinfo("Fait !", "Success !")

        #FIN
        end()

    else:
        tkinter.messagebox.showerror('Erreur !', "Vous n'avez pas spécifié de fichier (Code 4)")


#
#   Fonction de cryptage simple (steganographie)
#
def cryptsmp():

    """Fonction de cryptage simple, parametres : header de l'image, corps de l'image
        et nom du fichier final
        """

    global verifoka

    if verifoka:



        global header, image , final

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
        final.close()

        tkinter.messagebox.showinfo("Fait !", "Success !")

        #FIN
        end()

    else:
        tkinter.messagebox.showerror('Erreur !', "Vous n'avez pas spécifié de fichier (Code 4)")


#
#   Fonction de decryptage simple
#
def decryptsmp():

    """Fonction de decryptage simple, parametres : header de l'image, corps de l'image
        et nom du fichier final
        """
    global verifoka

    if verifoka:


        #Initialisation
        global header, image , final



        #longueurimage de la partie a decrypter
        longueurimage=len(image)

        #
        #   Appiclation du decryptage
        #

        #On recupere tout apres les nibbles ajoutés au cryptage
        moitier=int(longueurimage/2)

        if longueurimage%2!=0:
            moitier+=longueurimage%2

        # Fin Decryptage

        #ecriture dans le fichier
        final.write(header+bytes.fromhex(image[moitier:]))
        final.close()

        tkinter.messagebox.showinfo("Fait !", "Success !")

        #FIN
        end()

    else:
        tkinter.messagebox.showerror('Erreur !', "Vous n'avez pas spécifié de fichier (Code 4)")


#
#
#   FIN DU MODULE FONCTIONS
#
#
