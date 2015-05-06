#!/usr/bin/python
# -*- coding: ascii -*-

#Module 5

"""
Module de recuperation des dimmentions de l'image, le parametre est le header en bytes de l'image
"""
import binascii

def dimensionligne(header):
    """
    Recuperation des dimmentions de l'image, le parametre est le header en bytes de l'image
    """


    #recuperation de la longeure en pixel d'une ligne
    ligne=''
    lignehex=(str(binascii.hexlify(header[0x16:0x1a])))[2:len(ligne)-1]

    m=0

    for i in range(4):
        if lignehex[8-m-2:8-m]=='00':
            print('')
        else:
            ligne+=lignehex[8-m-2:8-m]


        m+=2

    ligne = int(ligne,16)

    return ligne



def dimensioncolone(header):
    """
    Recuperation des dimmentions de l'image, le parametre est le header en bytes de l'image
    """
    #recuperation de la longeure en pixel d'une colone
    colone=''
    colonehex=(str(binascii.hexlify(header[0x12:0x16])))[2:len(colone)-1]

    m=0

    for i in range(4):
        if colonehex[8-m-2:8-m]=='00':
            print('')
        else:
            colone+=colonehex[8-m-2:8-m]


        m+=2

    colone = int(colone,16)

    return colone

#
# FIN MODULE DIMENSION
#