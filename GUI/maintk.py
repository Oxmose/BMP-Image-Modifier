#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Main

"""
Module main avec GUI, base du programme, les importations :

from fonction import *
from compression import *
from info import *
from opendiag import *

doivent etre presentent pour son bon fonctionnement

Attention pas de protection contre double inclusion !
"""

#
#       BMP Image Modifier V1 GUI Version
#
#       MAIN avec Menu
#       Pour acceder aux fonctions veuillez vous referer aux fichiers modules
#       fonction.py, erreur.py et compression.py
#       Certaines variable globales sont utilisés pour pallier au problème de l'utilisation de Tkinter sans POO
#

from fonction import *#fonction du programme
from compression import *#compression des bmp
from info import *#fonction informations
from opendiag import *#Boite de diablogue ouverture fichier



#Generation de la fenetre
windowbim= Tk()
windowbim.title('BMP Image Modifier')
windowbim.geometry("600x445")
windowbim.resizable(False,False)

#
#   Generation des Widgets
#

#Generation des frames
background_image=PhotoImage(file="res/bg.gif")
tsr_image=PhotoImage(file="res/tsr.gif")
tsr2_image=PhotoImage(file="res/tsr2.gif")

fr_general=Label(windowbim, width=600, height=300, borderwidth=0, image=background_image)
fr_optn=Label(fr_general, width=500, height=300, borderwidth=0, image=tsr_image)
lbl_cmd=Label(fr_optn, width=200, height=75,image=tsr2_image)


#Creation des labels
immenu=PhotoImage(file="res/menu.gif")
titre_label=Label(fr_general, image=immenu, borderwidth=0)

iminfo=PhotoImage(file="res/droite.gif")
choix_label=Label(fr_optn, image=iminfo, borderwidth=0)

fichierin_bt=Button(fr_optn, text='Ouvrir un fichier', command=opendiag)

#Creation des boutons
imquit=PhotoImage(file="res/bt_quitter.gif")
bt_quitter=Button(lbl_cmd, image=imquit , command=windowbim.quit, width=53, height=53)
bt_quitter.config(relief=FLAT)

bt_cryptsmp=Button(fr_optn, text="Crypter une image BMP (Methode Simple) ", width=40, command=cryptsmp)
bt_decryptsmp=Button(fr_optn, text="Décrypter une image BMP (Methode Simple)", width=40, command=decryptsmp)
bt_cryptav=Button(fr_optn, text="Crypter une image BMP (Methode Avancée)", width=40, command=cryptav)
bt_decryptav=Button(fr_optn, text="Décrypter une image BMP (Methode Avancée)", width=40, command=decryptav)
bt_negatif=Button(fr_optn, text="Négatif / Contre négatif", width=40, command=negatif)
bt_div=Button(fr_optn, text="Diviser une image BMP (Irréversible)", width=40, command=coupe)
bt_sombai=Button(fr_optn, text="Saturation des couleurs (+/-)", width=40, command=choixassaic)
bt_comp=Button(fr_optn, text="Compresser/Décompresser une image BMP", width=40, command=compression)

imginfo=PhotoImage(file="res/bt_info.gif")
bt_info=Button(lbl_cmd, image=imginfo,width=53, height=53, command=info)
bt_info.config(relief=FLAT)

#
#   Affichage des Widgets
#

#Affichage des frame avec widget
fr_general.pack()
titre_label.pack(side=TOP, fill=X)

fr_optn.pack(side=RIGHT)
lbl_cmd.pack(side=BOTTOM)

#Affichage des label de mise en page

fichierin_bt.pack(side=TOP, pady=5)


#Affichage des bouttons d'actions


bt_cryptsmp.pack(side=BOTTOM, pady=5)
bt_decryptsmp.pack(side=BOTTOM, pady=5)
bt_cryptav.pack(side=BOTTOM, pady=5)
bt_decryptav.pack(side=BOTTOM, pady=5)
bt_negatif.pack(side=BOTTOM, pady=5)
bt_div.pack(side=BOTTOM, pady=5)
bt_sombai.pack(side=BOTTOM, pady=5)
bt_comp.pack(side=BOTTOM, pady=5)
bt_info.pack(side=LEFT, pady=5)
bt_quitter.pack(side=LEFT, pady=5)

#Bouton quitter




windowbim.mainloop()


#
#
#
#   FIN MAIN GUI
#
#
#