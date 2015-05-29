#!/usr/bin/env python3
import random
import pygame
import pygame.gfxdraw
from pygame.locals import *
import numpy

largeur = 150
hauteur = 150
taille_pixel = 4
plateau=[]
plateau0=[]
for i in range(largeur):
    plateau.append([0]*largeur)
    plateau0.append([0]*largeur)

pygame.init()
fenetre = pygame.display.set_mode((taille_pixel*hauteur, taille_pixel*largeur))
pygame.display.flip()


def afficher(tab):
    ##############################################
    'change les pixels'
    ##############################################
    for i in range(largeur):
        for j in range(largeur):
            if tab[i][j] == 0: couleur = [0, 0, 0]
            elif tab[i][j] == 1: couleur = [255, 255, 255]
            else : couleur = [100, 10, 10]
            pygame.gfxdraw.box(fenetre, (taille_pixel*i, taille_pixel*j, taille_pixel, taille_pixel), couleur)
    pygame.display.flip()


def etat_suivant(tab):
    def alive(i, j):
        ##############################################
        'renvoi le nb de voisin vivant'
        ##############################################
        vivante = 0

        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if tab[x][y] == 1 : vivante += 1
        if tab[i][j] == 1 : vivante -= 1
        return vivante
    ##############################################
    'calcul l\'etat suivant'
    ##############################################
    tab2=[]
    for i in range(largeur):
        tab2.append([0]*largeur)
    for i in range(largeur-1):
        for j in range(largeur-1):
            nb_vivante = alive(i, j)
            if nb_vivante == 3 : tab2[i][j] = 1
            elif nb_vivante == 2 : tab2[i][j] = tab[i][j]
            elif nb_vivante > 3 : tab2[i][j] = 0
            elif nb_vivante < 2 : tab2[i][j] = 0

    return tab2


def main(tab):
    ##############################################
    'main'
    ##############################################
    tab2 = etat_suivant(tab)
    afficher(tab2)
    return tab2



for i in range(largeur):
    for j in range(largeur):
        if random.random()>0.5:
            plateau[i][j] = 0
        else:
            plateau[i][j] = 1


l = True

while l:
    plateau = main(plateau)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            l = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                l = False












#couleur :
#citoyen = 255 255 255
#cadavre = 50 50 50
#zombie = largeur 20 20
#fond = 0 0 0