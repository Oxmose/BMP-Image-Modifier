#!/usr/bin/python
# -*- coding: utf-8 -*-

#Module 3

"""Module info et credit GUI"""

#
#
#Informations et Credits du programme GUI
#
#
from tkinter import *


def info():

    """
    Affiche les credit et informations dans des labels, pas d'arguments
    """


    #Generation de la fenetre
    infowin=Toplevel(bg='white')
    infowin.grab_set()
    infowin.focus_set()
    infowin.title('Informations...')
    infowin.geometry("600x280")
    infowin.resizable(False,False)

    imageinfo=PhotoImage(file="res/menu.gif")
    titre_label=Label(infowin, image=imageinfo, borderwidth=0)
    titre_label.pack()

    imageinfobg=PhotoImage(file="res/bg2.gif")
    bglabel=Label(infowin, image=imageinfobg)


    bglabel.pack()

    #Informations MAJ

    infowin.mainloop()


    #
    #
    #   FIN DU MODULE INFORMATIONS
    #
    #