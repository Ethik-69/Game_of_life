#!/usr/bin/env python3
import random
import pygame
import pygame.gfxdraw
from pygame.locals import *
import numpy

largeur = 200
hauteur = 200
taille_pixel = 4
plateau=[]
plateau0=[]
for i in range(200):
    plateau.append([0]*200)
    plateau0.append([0]*200)

pygame.init()
fenetre = pygame.display.set_mode((taille_pixel*hauteur, taille_pixel*largeur))
pygame.display.flip()

def etat_suivant(tab):
    def alive(tab, i, j):
        ##############################################
        'renvoi le nb de voisin vivant'
        ##############################################
        vivante = 0
        if tab[i][j] == 1 :
            vivante -= 1
        for x in range(i-1, i+1):
            for y in range(j-1, j+1):
                if tab[x][y] == 1 :vivante += 1
        return vivante
    ##############################################
    'calcul l\'etat suivant'
    ##############################################
    tab2=[]
    for i in range(200):
        tab2.append([0]*200)
    for i in range(200):
        for j in range(200):
            nb_vivante = alive(tab, i, j)
            if nb_vivante%2==0 : tab2[i][j]=0
            else: tab2[i][j]=1

    return tab2

def afficher(tab):
    ##############################################
    'change les pixels'
    ##############################################
    for i in range(200):
        for j in range(200):
            if tab[i][j] == 0: couleur = [0, 0, 0]
            elif tab[i][j] == 1: couleur = [255, 255, 255]
            pygame.gfxdraw.box(fenetre, (taille_pixel*i, taille_pixel*j, taille_pixel, taille_pixel), couleur)
    pygame.display.flip()

def main(tab):
    ##############################################
    'main'
    ##############################################
    tab2 = etat_suivant(tab)
    afficher(tab2)
    return tab2




plateau[25][25]=1
plateau[25][26]=1
plateau[25][26]=1

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
#zombie = 200 20 20
#fond = 0 0 0


