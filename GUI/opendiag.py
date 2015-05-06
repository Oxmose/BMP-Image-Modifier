#!/usr/bin/python
# -*- coding: utf-8 -*-

#Module 5

"""Module Boite de dialogue d'ouverturede fichier GUI"""

#
#
#Boite de dialogue d'ouverturede fichier
#
#
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import binascii
from erreur import *
from fonction import *

def click():
    """
    Sur click de souris sur bouton ok, aucun paramatres
    """
    global namefilein, origin
    global namefilesortie
    global opendiagwin

    namefile=namefilein.get()
    namefileout=namefilesortie.get()

    global header
    global image
    global final

    global verifok
    verifok=-1


    opendiagwin.destroy()

    if testextention(namefile):


        #Ouverture du fichier d'entree, avec gestion d'erreur
        try:
            origin=open(extentionajout(namefile), 'rb')

            #Lecture du fichier d'origine
            fichier=origin.read()

            #Recuperation du header de l'image
            header=fichier[0x0:0x36]

            #on traduit en hex et on enleve le b'
            image=(str(binascii.hexlify(fichier[0x36:])))[2:]
            #on enleve le ' a la fin de la chaine
            image=image[0:len(image)-1]

            verifok+=1

        except IOError:
            tkinter.messagebox.showerror('Attention !', 'Erreur lors de l\'ouverture du fichier. Est-til dans le bon dossier ? (Code2)')



        #Ouverture ou creation du fichier de sortie, avec gestion d'erreur
        try:
            final=open(extentionajout(namefileout), 'wb')
            verifok+=1

        except IOError:
            tkinter.messagebox.showerror('Attention !', "Erreur lors de l\'ouverture du fichier. Avez vous les droits requis ? (Code 3)")
            origin.close()

    else :
        #Le fichier n'est pas un BMP 42 : choix arbitraire
        tkinter.messagebox.showerror('Attention !', "Vous devez utiliser un fichier BMP. (Code 1)")


    passagevar(verifok, header, image, final)


    origin.close()


def opendiag():

    """
    Boite de dialogue d'ouverture de fichier, aucun parametres
    """
    global namefilein



    global namefilesortie
    global opendiagwin

     #Generation de la fenetre
    opendiagwin=Toplevel(bg='white')
    opendiagwin.grab_set()
    opendiagwin.focus_set()
    opendiagwin.title('Ouverture du fichier')
    opendiagwin.geometry("260x130")
    opendiagwin.resizable(False,False)

    titre_label=Label(opendiagwin, text="Entrez un nom pour le fichier d'entrée", borderwidth=0, justify=LEFT,bg='white')
    titre_label.pack(side=TOP)

    namefilein = StringVar()#Variable globale
    ligne_texte = Entry(opendiagwin, textvariable=namefilein, width=50)
    ligne_texte.pack()


    info_lbl=Label(opendiagwin, text="Entrez un nom pour le fichier de sortie", justify=LEFT,bg='white')
    info_lbl.pack(side=TOP)

    namefilesortie = StringVar()#Variable globale
    ligne_texte2 = Entry(opendiagwin, textvariable=namefilesortie, width=50)
    ligne_texte2.pack()

    bt_ok=Button(opendiagwin, text='Ouvrir...', command=click)
    bt_ok.pack(side=BOTTOM)

    opendiagwin.mainloop()


    #
    #
    #   FIN DU MODULE OUVERTURE
    #
    #