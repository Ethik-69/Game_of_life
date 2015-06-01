#!/usr/bin/env python3
import random
import pygame
import pygame.gfxdraw
from pygame.locals import *


largeur = 180
hauteur = 150
taille_pixel = 4
plateau=[]
plateau0=[]
for i in range(hauteur):
    plateau.append([0]*largeur)
    plateau0.append([0]*largeur)

pygame.init()

fenetre = pygame.display.set_mode((taille_pixel*largeur, taille_pixel*hauteur), RESIZABLE)

background = pygame.Surface(fenetre.get_size())
background = background.convert()
background.fill((255, 255, 255))

pygame.display.set_caption('Game Of Life')

def afficher(plateau):
    ##############################################
    'change les pixels'
    ##############################################
    for i in range(hauteur):
        for j in range(largeur):
            if plateau[i][j] == 0: couleur = [0, 0, 0]
            elif plateau[i][j] == 1: couleur = [255, 255, 255]
            elif plateau[i][j] == 2: couleur = [150, 20, 20]
            else : couleur = [0, 100, 0]
            pygame.gfxdraw.box(fenetre, (taille_pixel*i+120, taille_pixel*j, taille_pixel, taille_pixel), couleur)
    pygame.display.flip()

def etat_suivant(plateau):
    def alive(i, j):
        ##############################################
        'renvoi le nb de voisin vivant'
        ##############################################
        vivante = 0

        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if plateau[x][y] == 1 : vivante += 1
        if plateau[i][j] == 1 : vivante -= 1
        return vivante
    ##############################################
    'calcul l\'etat suivant'
    ##############################################
    plateau2=[]
    for i in range(hauteur):
        plateau2.append([0]*largeur)
    for i in range(hauteur-1):
        for j in range(largeur-1):
            nb_vivante = alive(i, j)
            if nb_vivante == 3 : plateau2[i][j] = 1
            elif nb_vivante == 2 : plateau2[i][j] = plateau[i][j]
            elif nb_vivante > 3 : plateau2[i][j] = 0
            elif nb_vivante < 2 : plateau2[i][j] = 0
    return plateau2

def main(plateau):
    ##############################################
    'main'
    ##############################################
    plateau2 = etat_suivant(plateau)
    afficher(plateau2)
    return plateau2

def init():
    for i in range(hauteur):
        for j in range(largeur):
            rd = random.random()
            if rd > 0.5:
                plateau[i][j] = 1
            elif rd < 0.5:
                plateau[i][j] = 2
            else:
                plateau[i][j] = 1

def pause(plateau):
    pause = True
    while pause:
        mouse_xy = pygame.mouse.get_pos()
        init_on = init_bouton.collidepoint(mouse_xy)
        start_on = start_bouton.collidepoint(mouse_xy)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause = False
            elif event.type == MOUSEBUTTONDOWN and start_on:
                pause = False
            elif event.type == MOUSEBUTTONDOWN and init_on: #ou UP
                afficher(plateau)
                init()

def accueil_font():
    font_1 = pygame.font.Font('fonts/visitor1.ttf', 40)
    font_2 = pygame.font.Font('fonts/visitor1.ttf', 25)

    titre = font_1.render("Game Of Life", 1, (150, 25, 25))
    titrepos = titre.get_rect(centerx=background.get_width()/2, centery=150)
    background.blit(titre, titrepos)

    demarrer_text = font_2.render("Demarrer", 1, (150, 25, 25))
    demarrer_text_pos = demarrer_text.get_rect(centerx=background.get_width()/2, centery=background.get_width()/2)
    background.blit(demarrer_text, demarrer_text_pos)
    return background

def accueil():
    accueil = True
    demarrer_bouton = pygame.draw.rect(fenetre, [25, 25, 100], [background.get_width()/2.5, background.get_width()/2.2, 150, 40])

    if pygame.font:
        accueil_font()

    fenetre.blit(background, (0, 0))
    pygame.display.flip()

    while accueil:
        mouse_xy = pygame.mouse.get_pos()
        demarrer_on = demarrer_bouton.collidepoint(mouse_xy)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
            elif event.type == MOUSEBUTTONDOWN and demarrer_on:
                accueil = False

def main_font():
    font = pygame.font.Font('fonts/visitor1.ttf', 15)

    init_text = font.render("Initialiser", 1, (255, 255, 255))
    init_text_pos = init_text.get_rect(centerx=55, centery=20)
    background.blit(init_text, init_text_pos)

    start_text = font.render("Start", 1, (255, 255, 255))
    start_text_pos = start_text.get_rect(centerx=55, centery=60)
    background.blit(start_text, start_text_pos)

    stop_text = font.render("Stop", 1, (255, 255, 255))
    stop_text_pos = stop_text.get_rect(centerx=55, centery=110)
    background.blit(stop_text, stop_text_pos)
    return background


fonctionnement = True
lancement = True
generation = 0
temp_pause = 0

accueil()

background.fill((100, 25, 25))

init_bouton = pygame.draw.rect(fenetre, [0, 0, 0], [10, 10, 90, 40])
start_bouton = pygame.draw.rect(fenetre, [0, 0, 0], [10, 60, 90, 40])
stop_bouton = pygame.draw.rect(fenetre, [0, 0, 0], [10, 110, 90, 40])

main_font()

fenetre.blit(background, (0, 0))
pygame.display.flip()

while fonctionnement:
    mouse_xy = pygame.mouse.get_pos()

    init_on = init_bouton.collidepoint(mouse_xy)
    start_on = start_bouton.collidepoint(mouse_xy)
    stop_on = stop_bouton.collidepoint(mouse_xy)

    print('Generation : ',generation)
    plateau = main(plateau)

    if lancement:
        lancement = False
        pause(plateau)

    generation += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fonctionnement = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                fonctionnement = False
        elif event.type == MOUSEBUTTONDOWN and init_on:
            generation = 0
            init()
        elif event.type == MOUSEBUTTONDOWN and stop_on:
            generation = 0
            pause(plateau)

    pygame.time.wait(temp_pause)

#modif cellule par souri
#couleur :
#citoyen = 0 0 0
#cadavre = 50 50 50
#zombie = largeur 20 20
#fond = 0 0 0