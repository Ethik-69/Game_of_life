#!/usr/bin/env python3
import pixel
import numpy

largeur = 50
hauteur = 50
zoom = 10

pixel.initialiser(largeur, hauteur, zoom)

def read(tab):
    ##############################################
    'lit l\'etat des cellules du tableau''
    ##############################################
    for i in range(0, 50):
        for j in range(0, 50):
            tab[i, j] = int(pixel.lire(i, j))
    return tab


def alive(tab, i, j):
    ##############################################
    'renvoi le nb de voisin vivant'
    ##############################################
    vivante = 0
    if tab[i, j] == 0 :
        vivante -= 1
    i = i - 1
    j = j + 1
    for x in range(i, j):
        for y in range(i, j):
            if tab[x, y] == 0 :
                vivante += 1
    return vivante


def etat_suivant(tab):
    ##############################################
    'calcul l\'etat suivant'
    ##############################################
    nb_vivante = alive(tab, i, j)
    if nb_vivante == 2 :
        tab[i, j] = 0
    elif nb_vivante == 3 :
        tab[i, j] = 0
    elif nb_vivante > 3:
        tab[i, j] = 1
    elif tab[i, j] == 1 and nb_vivante == 3:
        tab[i, j] = 0


def main(tab):
    ##############################################
    'main'
    ##############################################
    plateau = read(tab)
    for i in range(0, 49):
        for j in range(0, 49):
            tab2 = etat_suivant(tab)
    pixel.afficher(0.3)




plateau = numpy.zeros((50, 50), dtype=numpy.uint32)
pixel.marquer(2, 2, 0)
pixel.marquer(2, 3, 0)
pixel.marquer(2, 4, 0)
pixel.afficher(0.3)
l = 0
for l in range(0, 100):
    main(plateau)
input()


#pixel.lire() lire un pixel
#pixel.initialiser(largeur, hauteur, zoom) pose le tableau
#pixel.marquer(i, j, 0) change etat pixel 0 on 1 off
#pixel.afficher() affiche le(s) pixel ?

#mettre l'état des cellules dans un dico {on/off : 0/1}
#faire les passe avec deux for pour le test et l'affichage