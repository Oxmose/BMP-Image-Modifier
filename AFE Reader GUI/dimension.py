#!/usr/bin/python
# -*- coding: ascii -*-

#Module 2

"""
Module de recuperation des dimmentions de l'image, le parametre est le header en bytes de l'image
"""
import binascii

def dimensioncolone(header):
    """
    Recuperation des dimmentions de l'image, le parametre est le header en bytes de l'image
    """
    #recuperation de la longeure en pixel d'une colone
    colone=''
    colonehex=header[36:42]

    m=0

    for i in range(4):
        colone+=colonehex[8-m-2:8-m]
        m+=2

    colone = int(colone,16)
    return colone

def dimensionligne(header):
    """
    Recuperation des dimmentions de l'image, le parametre est le header en bytes de l'image
    """
    #recuperation de la longeure en pixel d'une colone
    ligne=''
    lignehex=header[44:50]

    m=0

    for i in range(4):
        ligne+=lignehex[8-m-2:8-m]
        m+=2

    ligne = int(ligne,16)
    return ligne

#
# FIN MODULE DIMENSION
#