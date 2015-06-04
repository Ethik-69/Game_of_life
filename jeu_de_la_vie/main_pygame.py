#!/usr/bin/env python3
import random
import pygame
import pygame.gfxdraw
from pygame.locals import *

#i = x = abscisse
#j = y = ordonee
largeur = 180
hauteur = 150
taille_pixel = 4

pygame.init()

fenetre = pygame.display.set_mode((taille_pixel*largeur, taille_pixel*hauteur), RESIZABLE)

background = pygame.Surface(fenetre.get_size())
background = background.convert()
background.fill((255, 255, 255))

pygame.display.set_caption('Game Of Life')

def init_plateau():
    ##############################################
    'met les plateau a 0'
    ##############################################
    plateau=[]
    plateau0=[]
    for i in range(hauteur):
        plateau.append([0]*largeur)
        plateau0.append([0]*largeur)
    return plateau, plateau0

def afficher(plateau):
    ##############################################
    'affiche euh... l\'affichage'
    ##############################################
    for i in range(hauteur):
        for j in range(largeur):
            if plateau[i][j] == 0: couleur = [0, 0, 0]
            elif plateau[i][j] == 1: couleur = [255, 255, 255]
            elif plateau[i][j] == 2: couleur = [150, 20, 20]
            else : couleur = [0, 100, 0]
            fenetre.fill(couleur, (i * taille_pixel+120, j * taille_pixel, taille_pixel - 1, taille_pixel - 1))
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
            elif nb_vivante > 3 : plateau2[i][j] = 2
            elif nb_vivante < 2 : plateau2[i][j] = 0
    return plateau2

def main(plateau):
    ##############################################
    'main'
    ##############################################
    plateau2 = etat_suivant(plateau)
    afficher(plateau2)
    return plateau2

def aleatoire():
    ##############################################
    'change l\'etat des cellules aleatoirement'
    ##############################################
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
    ##############################################
    'boucle infinie de... la pause'
    ##############################################
    pause = True
    while pause:
        mouse_xy = pygame.mouse.get_pos()
        aleatoire_on = aleatoire_bouton.collidepoint(mouse_xy)
        start_on = start_bouton.collidepoint(mouse_xy)
        reinitialisation_on = reinitialisation_bouton.collidepoint(mouse_xy)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause = False
            elif event.type == MOUSEBUTTONDOWN:
                if start_on:
                    pause = False
                elif aleatoire_on:
                    aleatoire()
                    afficher(plateau)
                elif reinitialisation_on:
                    plateau, plateau0 = init_plateau()
                    afficher(plateau)
                elif mouse_xy[0] > 120:
                    if plateau[(mouse_xy[0]-120)/4][mouse_xy[1]/4] == 0:
                        plateau[(mouse_xy[0]-120)/4][mouse_xy[1]/4] = 1
                        afficher(plateau)
                    else:
                        plateau[(mouse_xy[0]-120)/4][mouse_xy[1]/4] = 0
                        afficher(plateau)
    return plateau

def accueil_font():
    ##############################################
    'import les police et place le text de l\'accueil'
    ##############################################
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
    ##############################################
    'boucle infinie de l\'accueil'
    ##############################################
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
    ##############################################
    'import la police et place les text des boutons'
    ##############################################
    font = pygame.font.Font('fonts/visitor1.ttf', 15)

    init_text = font.render("Aleatoire", 1, (255, 255, 255))
    init_text_pos = init_text.get_rect(centerx=55, centery=23)
    background.blit(init_text, init_text_pos)

    start_text = font.render("Start", 1, (255, 255, 255))
    start_text_pos = start_text.get_rect(centerx=55, centery=63)
    background.blit(start_text, start_text_pos)

    stop_text = font.render("Stop", 1, (255, 255, 255))
    stop_text_pos = stop_text.get_rect(centerx=55, centery=103)
    background.blit(stop_text, stop_text_pos)

    stop_text = font.render("Reinitialisation", 1, (255, 255, 255))
    stop_text_pos = stop_text.get_rect(centerx=60, centery=143)
    background.blit(stop_text, stop_text_pos)
    return background

fonctionnement = True
lancement = True
generation = 0
temp_pause = 0
plateau, plateau0 = init_plateau()

accueil()

background.fill((40, 40, 40))

aleatoire_bouton = pygame.draw.rect(fenetre, [0, 0, 0], [10, 10, 90, 25])
start_bouton = pygame.draw.rect(fenetre, [0, 0, 0], [10, 60, 90, 25])
stop_bouton = pygame.draw.rect(fenetre, [0, 0, 0], [10, 100, 90, 25])
reinitialisation_bouton = pygame.draw.rect(fenetre, [0, 0, 0], [10, 130, 90, 25])

main_font()

fenetre.blit(background, (0, 0))
pygame.display.flip()

while fonctionnement:
    mouse_xy = pygame.mouse.get_pos()
    aleatoire_on = aleatoire_bouton.collidepoint(mouse_xy)
    start_on = start_bouton.collidepoint(mouse_xy)
    stop_on = stop_bouton.collidepoint(mouse_xy)
    reinitialisation_on = reinitialisation_bouton.collidepoint(mouse_xy)

    plateau = main(plateau)

    if lancement:
        lancement = False
        plateau = pause(plateau)

    generation += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fonctionnement = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                fonctionnement = False
        elif event.type == MOUSEBUTTONDOWN:
            if aleatoire_on:
                generation = 0
                aleatoire()
            elif stop_on:
                generation = 0
                plateau = pause(plateau)
            elif reinitialisation_on:
                plateau, plateau0 = init_plateau()
            else:
                if mouse_xy[0] > 120:
                    if plateau[(mouse_xy[0]-120)/4][mouse_xy[1]/4] == 0:
                        plateau[(mouse_xy[0]-120)/4][mouse_xy[1]/4] = 1
                    else:
                        plateau[(mouse_xy[0]-120)/4][mouse_xy[1]/4] = 0

    pygame.time.wait(temp_pause)
