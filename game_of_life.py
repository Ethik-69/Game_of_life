#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
import pygame
from pygame.locals import *


def main():
    #x = abscisse
    #y = ordonee
    width = 200
    height = 170
    pixel_size = 4
    less = 1
    more = 2

    pygame.init()

    fenetre = pygame.display.set_mode((pixel_size*width, pixel_size*height), RESIZABLE)

    background = pygame.Surface(fenetre.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    pygame.display.set_caption('Game Of Life')

    def init_grid():
        ##############################################
        """Initialise la grille"""
        ##############################################
        grid = [[0]*width for i in xrange(height)]
        return grid

    def display(grid):
        ##############################################
        """Change la couleur des cases de la grille"""
        ##############################################
        for i in xrange(height):
            for j in xrange(width):
                if grid[i][j] == 0:
                    colour = [0, 0, 0]
                elif grid[i][j] == 1:
                    colour = [255, 255, 255]
                elif grid[i][j] == 2:
                    colour = [0, 80, 80]
                else :
                    colour = [0, 100, 0]
                fenetre.fill(colour, (i * pixel_size+120, j * pixel_size, pixel_size - 1, pixel_size - 1))
        pygame.display.flip()

    def next_state(grid):
        def alive(i, j):
            ##############################################
            """Renvoi le nombre de cellules vivante voisine"""
            ##############################################
            alive_cells = 0

            for x in xrange(i-less, i+more):
                for y in xrange(j-less, j+more):
                    if grid[x][y] == 1:
                        alive_cells += 1
            if grid[i][j] == 1:
                alive_cells -= 1
            return alive_cells
        ##############################################
        """calcul l'etat suivant"""
        ##############################################
        buffer = [[0]*width for i in xrange(height)]
        for i in xrange(height-less):
            for j in xrange(width-less):
                nb_alive_cells = alive(i, j)
                if nb_alive_cells == 3:
                    buffer[i][j] = 1
                elif nb_alive_cells == 2:
                    buffer[i][j] = grid[i][j]
                elif nb_alive_cells > 3:
                    buffer[i][j] = 2
                elif nb_alive_cells < 2:
                    buffer[i][j] = 0
        return buffer

    def switch_buffer(grid):
        buffer = next_state(grid)
        display(buffer)
        return buffer

    def random_grid():
        ##############################################
        """Génère une grille aléatoire"""
        ##############################################
        for i in xrange(height):
            for j in xrange(width):
                rd = random.random()
                if rd > 0.6:
                    grid[i][j] = 1
                elif rd < 0.1:
                    grid[i][j] = 2
                else:
                    grid[i][j] = 0

    def pause(grid):
        ##############################################
        """Boucle infinie de la pause"""
        ##############################################
        global less
        global more
        pause = True
        while pause:
            mouse_xy = pygame.mouse.get_pos()
            random_grid_on = random_grid_bouton.collidepoint(mouse_xy)
            start_on = start_bouton.collidepoint(mouse_xy)
            reinitialisation_on = reinitialisation_bouton.collidepoint(mouse_xy)
            less_on = less_bouton.collidepoint(mouse_xy)
            more_on = more_bouton.collidepoint(mouse_xy)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pause = False
                elif event.type == MOUSEBUTTONDOWN:
                    if start_on:
                        pause = False
                    elif random_grid_on:
                        random_grid()
                        display(grid)
                    elif reinitialisation_on:
                        grid = init_grid()
                        display(grid)
                    elif mouse_xy[0] > 120:
                        if grid[(mouse_xy[0]-120)/4][mouse_xy[1]/4] == 0:
                            grid[(mouse_xy[0]-120)/4][mouse_xy[1]/4] = 1
                            display(grid)
                        else:
                            grid[(mouse_xy[0]-120)/4][mouse_xy[1]/4] = 0
                            display(grid)
                    elif more_on:
                        more += 1
                        less += 1
                        print(more, less)
                    elif less_on:
                        less -= 1
                        more -= 1
                        print(more, less)
        return grid

    def welcome_font():
        ##############################################
        """Importe les polices et place le text de l'accueil"""
        ##############################################
        font_1 = pygame.font.Font('fonts/visitor1.ttf', 40)
        font_2 = pygame.font.Font('fonts/visitor1.ttf', 25)

        titre = font_1.render("Game Of Life", 1, (150, 25, 25))
        titrepos = titre.get_rect(centerx=background.get_width()/2, centery=150)
        background.blit(titre, titrepos)

        demarrer_text = font_2.render("Demarrer", 1, (150, 25, 25))
        demarrer_text_pos = demarrer_text.get_rect(centerx=background.get_width()/2, centery=background.get_width()/2.2)
        background.blit(demarrer_text, demarrer_text_pos)
        return background

    def welcome_screen():
        ##############################################
        """Boucle infinie de l'accueil"""
        ##############################################
        welcome = True
        demarrer_bouton = pygame.draw.rect(fenetre, [25, 25, 100], [background.get_width()/2.5, background.get_width()/2.4, 150, 40])

        if pygame.font:
            welcome_font()

        fenetre.blit(background, (0, 0))
        pygame.display.flip()

        while welcome:
            mouse_xy = pygame.mouse.get_pos()
            demarrer_on = demarrer_bouton.collidepoint(mouse_xy)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        quit()
                elif event.type == MOUSEBUTTONDOWN and demarrer_on:
                    welcome = False

    def main_font():
        ##############################################
        """Import la police et place les text des boutons"""
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

        more_text = font.render("Plus", 1, (255, 255, 255))
        more_text_pos = more_text.get_rect(centerx=60, centery=183)
        background.blit(more_text, more_text_pos)

        less_text = font.render("Moins", 1, (255, 255, 255))
        less_text_pos = less_text.get_rect(centerx=60, centery=223)
        background.blit(less_text, less_text_pos)
        return background

    fonctionnement = True
    lancement = True
    generation = 0
    temp_pause = 0
    grid = init_grid()

    welcome_screen()

    background.fill((40, 40, 40))
    random_grid_bouton = pygame.draw.rect(fenetre, [0, 0, 0], [10, 10, 90, 25])
    start_bouton = pygame.draw.rect(fenetre, [0, 0, 0], [10, 59, 90, 25])
    stop_bouton = pygame.draw.rect(fenetre, [0, 0, 0], [10, 99, 90, 25])
    reinitialisation_bouton = pygame.draw.rect(fenetre, [0, 0, 0], [0, 130, 120, 25])
    less_bouton = pygame.draw.rect(fenetre, [0, 0, 0], [10, 210, 90, 25])
    more_bouton = pygame.draw.rect(fenetre, [0, 0, 0], [10, 170, 90, 25])

    main_font()

    fenetre.blit(background, (0, 0))
    pygame.display.flip()

    while fonctionnement:
        mouse_xy = pygame.mouse.get_pos()
        random_grid_on = random_grid_bouton.collidepoint(mouse_xy)
        start_on = start_bouton.collidepoint(mouse_xy)
        stop_on = stop_bouton.collidepoint(mouse_xy)
        reinitialisation_on = reinitialisation_bouton.collidepoint(mouse_xy)
        less_on = less_bouton.collidepoint(mouse_xy)
        more_on = more_bouton.collidepoint(mouse_xy)

        grid = switch_buffer(grid)

        if lancement:
            lancement = False
            grid = pause(grid)

        generation += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fonctionnement = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    fonctionnement = False
            elif event.type == MOUSEBUTTONDOWN:
                if random_grid_on:
                    generation = 0
                    random_grid()
                elif stop_on:
                    generation = 0
                    grid = pause(grid)
                elif reinitialisation_on:
                    grid = init_grid()
                elif more_on:
                    more += 1
                    less += 1
                elif less_on:
                    less -= 1
                    more -= 1
                else:
                    if mouse_xy[0] > 120:
                        if grid[(mouse_xy[0]-120)/4][mouse_xy[1]/4] == 0:
                            grid[(mouse_xy[0]-120)/4][mouse_xy[1]/4] = 1
                        else:
                            grid[(mouse_xy[0]-120)/4][mouse_xy[1]/4] = 0

        pygame.time.wait(0)

if __name__ == '__main__':
    main()
