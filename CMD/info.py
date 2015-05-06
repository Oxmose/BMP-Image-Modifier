#!/usr/bin/python
# -*- coding: ascii -*-

#Module 3

"""Module info et credit"""

#
#
#Informations et Credits du programme
#
#
import time#pour info()
import sys#pour eviter retour ligne info()

def info():
    """Fonction informations, aucun parametre, standalone"""

    #Animation
    titre='BMP Image Modifier'
    for i in range(len (titre)):
        sys.stdout.write(titre[i])
        time.sleep(0.1)

    #Informations MAJ

    print("\n\nFuture mise a jour :\n ")
    print('-Gestion d\'erreur plus poussee\n-Nouvelles fonctionalite\n-La methode pour parser les infos du header n\'est pas la meilleure')
    print('-Meilleurs algorithmes de cryptage\n-Creation d\'une interface graphique')
    print('-Reversibilite de l\'alogrithme diviseur\n-Compretion/Decompretion d\'BMP autre methode')
    print('-Amelioration du code source (plus oprtimise, beaucoup d\'actions se repettent inutilement)\n-ATTENTION ! Ne s\'utilise que pour les BMP codes en 24Bits sans padding\n')

    #Credits
    print('\n\n========\n| V0.2 |\n========\n Copyright Torres/Becco')

    #
    #
    #   FIN DU MODULE INFORMATIONS
    #
    #