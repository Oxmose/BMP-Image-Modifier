#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from erreur import *
from dimension import *


def pixel(image, pos, color, ligne):
    """Place les pixels a la possition=(x,y) sur l'image, avec color=(r,g,b)."""
    r,g,b = color

    x, y = pos

    image.put("#%02x%02x%02x" % (r,g,b), (x,ligne-y))


def affichage(namefile):
    global root2



    root2=Tk()
    root2.title('AFE Reader')
    root2.resizable(False,False)

    #Test de l'extension du fichier
    if testextentionafe(namefile):

        #Ouverture du fichier d'entree
        origin=open(extentionajoutafe(namefile))
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


    colone=dimensioncolone(header)
    ligne=dimensionligne(header)


    root2.title(('AFE Reader', extentionajoutafe(namefile)))
    taille=str(colone+4)+'x'+str(ligne+30)

    root2.geometry(taille)
    photo = tkinter.PhotoImage(width=colone, height=ligne)

    bt_quitter=Button(root2, text="Quitter la vue", command=root2.quit)
    #Initalisation des variables


    m=0#Compteur decrypteur
    v=0#la variable i n'est pas assez flexible on doit en creer une autre pour faire un v+=2
    nombrecoul=''#Nombre de repetition du nobble en hex
    coul=''#Nibble

    x, y=0,0
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

                #On convertir en decimal de nombre de fois que le nibble apparait
                k=int(nombrecoul, 16)

                b=int((coul[0:2]),16)
                g=int((coul[2:4]),16)
                r=int((coul[4:6]),16)

                #On stocke le motif complet
                for im in range(k):
                    pixel(photo, (x,y), (r,g,b), ligne)
                    if x==colone-1:
                        y+=1
                        x=0
                    else:
                        x+=1



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




    origin.close()
    label = tkinter.Label(root2, image=photo)
    label.grid(row=2, column=1)

    bt_quitter.grid(row=1, column=1)
    root2.mainloop()

    m=1
    main(m)


def stop():

    global t
    t=0
    global root
    root.quit()


def main(m):
    global root
    global root2
    global t
    global v


    if m:
        root2.destroy()
    t=1

    root=Tk()
    root.title('AFE Reader')
    root.geometry("200x45")
    root.resizable(False,False)

    fichierouvrir = StringVar()#Variable globale
    ligne_texte = Entry(root, textvariable=fichierouvrir, width=100)
    ligne_texte.pack()

    bt_ouvrir=Button(root, text="Ouvrir", command=stop)
    bt_ouvrir.pack(side=LEFT)
    bt_quitter=Button(root, text="Quitter", command=root.quit)
    bt_quitter.pack(side=RIGHT)


    root.mainloop()

    if t==0:
        root.destroy()

        namefile=fichierouvrir.get()
        affichage(namefile)


main(0)