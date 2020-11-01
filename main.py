#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
import pygame
from pygame.locals import *


class GameOfLife:
    def __init__(self):
        self.width = 200
        self.height = 170
        self.pixel_size = 4
        self.less = 1
        self.more = 2

        pygame.init()

        self.get_font()

        self.window = pygame.display.set_mode(
            (self.pixel_size * self.width, self.pixel_size * self.height), RESIZABLE
        )

        self.background = pygame.Surface(self.window.get_size())
        self.background = self.background.convert()
        self.background.fill((255, 255, 255))

        pygame.display.set_caption("Game Of Life")

    def get_font(self):
        self.welcome_font_1 = pygame.font.Font("fonts/visitor1.ttf", 40)
        self.welcome_font_2 = pygame.font.Font("fonts/visitor1.ttf", 25)
        self.main_font = pygame.font.Font("fonts/visitor1.ttf", 15)

    def run(self):
        self.welcome_screen()

    def blit_welcome_font(self):
        """
        Import fonts and blit them on screen
        """
        title = self.welcome_font_1.render("Game Of Life", 1, (150, 25, 25))
        title_pos = title.get_rect(centerx=self.background.get_width() / 2, centery=150)
        self.background.blit(title, title_pos)

        start_text = self.welcome_font_2.render("Start", 1, (150, 25, 25))
        start_text_pos = start_text.get_rect(
            centerx=self.background.get_width() / 2,
            centery=self.background.get_width() / 2.2,
        )
        self.background.blit(start_text, start_text_pos)

    def welcome_screen(self):
        """
        Display welcome screen
        """
        welcome = True

        start_bouton = pygame.draw.rect(
            self.window,
            [25, 25, 100],
            [
                self.background.get_width() / 2.5,
                self.background.get_width() / 2.4,
                150,
                40,
            ],
        )

        if pygame.font:
            self.blit_welcome_font()

        self.window.blit(self.background, (0, 0))
        pygame.display.flip()

        while welcome:
            mouse_xy = pygame.mouse.get_pos()
            start_on = start_bouton.collidepoint(mouse_xy)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        quit()

                elif event.type == MOUSEBUTTONDOWN and start_on:
                    welcome = False
                    self.main_screen()

    def blit_main_font(self):
        """
        Import fonts and blit them on buttons
        """
        init_text = self.main_font.render("Aleatoire", 1, (255, 255, 255))
        init_text_pos = init_text.get_rect(centerx=55, centery=23)
        self.background.blit(init_text, init_text_pos)

        start_text = self.main_font.render("Start", 1, (255, 255, 255))
        start_text_pos = start_text.get_rect(centerx=55, centery=63)
        self.background.blit(start_text, start_text_pos)

        stop_text = self.main_font.render("Stop", 1, (255, 255, 255))
        stop_text_pos = stop_text.get_rect(centerx=55, centery=103)
        self.background.blit(stop_text, stop_text_pos)

        stop_text = self.main_font.render("Reinitialisation", 1, (255, 255, 255))
        stop_text_pos = stop_text.get_rect(centerx=60, centery=143)
        self.background.blit(stop_text, stop_text_pos)

        self.more_text = self.main_font.render("Plus", 1, (255, 255, 255))
        self.more_text_pos = self.more_text.get_rect(centerx=60, centery=183)
        self.background.blit(self.more_text, self.more_text_pos)

        self.less_text = self.main_font.render("Moins", 1, (255, 255, 255))
        self.less_text_pos = self.less_text.get_rect(centerx=60, centery=223)
        self.background.blit(self.less_text, self.less_text_pos)

    def main_screen(self):
        run = True
        self.init_grid()

        self.background.fill((40, 40, 40))
        self.create_buttons()
        self.blit_main_font()

        self.window.blit(self.background, (0, 0))
        pygame.display.flip()

        self.pause()

        while run:
            mouse_xy = pygame.mouse.get_pos()
            self.get_collide_point(mouse_xy)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False

                elif event.type == MOUSEBUTTONDOWN:
                    if self.random_grid_on:
                        self.random_grid()

                    elif self.stop_on:
                        self.pause()

                    elif self.reinitialisation_on:
                        self.init_grid()

                    elif self.more_on:
                        self.more += 1
                        self.less += 1

                    elif self.less_on:
                        self.less -= 1
                        self.more -= 1

                    else:
                        if mouse_xy[0] > 120:
                            if self.grid[(mouse_xy[0] - 120) / 4][mouse_xy[1] / 4] == 0:
                                self.grid[(mouse_xy[0] - 120) / 4][mouse_xy[1] / 4] = 1

                            else:
                                self.grid[(mouse_xy[0] - 120) / 4][mouse_xy[1] / 4] = 0

            self.next_state()
            self.display()
            pygame.time.wait(0)

    def pause(self):
        """
        Pause screen
        """
        pause = True

        while pause:
            mouse_xy = pygame.mouse.get_pos()
            self.get_collide_point(mouse_xy)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pause = False

                elif event.type == MOUSEBUTTONDOWN:
                    if self.start_on:
                        pause = False

                    elif self.random_grid_on:
                        self.random_grid()

                    elif self.reinitialisation_on:
                        self.init_grid()

                    elif mouse_xy[0] > 120:
                        if self.grid[(mouse_xy[0] - 120) / 4][mouse_xy[1] / 4] == 0:
                            self.grid[(mouse_xy[0] - 120) / 4][mouse_xy[1] / 4] = 1

                        else:
                            self.grid[(mouse_xy[0] - 120) / 4][mouse_xy[1] / 4] = 0

                    elif self.more_on:
                        self.more += 1
                        self.less += 1

                    elif self.less_on:
                        self.less -= 1
                        self.more -= 1

            self.display()

    def create_buttons(self):
        self.random_grid_bouton = pygame.draw.rect(
            self.window, [0, 0, 0], [10, 10, 90, 25]
        )
        self.start_bouton = pygame.draw.rect(self.window, [0, 0, 0], [10, 59, 90, 25])
        self.stop_bouton = pygame.draw.rect(self.window, [0, 0, 0], [10, 99, 90, 25])
        self.reinitialisation_bouton = pygame.draw.rect(
            self.window, [0, 0, 0], [0, 130, 120, 25]
        )
        self.less_bouton = pygame.draw.rect(self.window, [0, 0, 0], [10, 210, 90, 25])
        self.more_bouton = pygame.draw.rect(self.window, [0, 0, 0], [10, 170, 90, 25])

    def get_collide_point(self, mouse_xy):
        self.random_grid_on = self.random_grid_bouton.collidepoint(mouse_xy)
        self.start_on = self.start_bouton.collidepoint(mouse_xy)
        self.stop_on = self.stop_bouton.collidepoint(mouse_xy)
        self.reinitialisation_on = self.reinitialisation_bouton.collidepoint(mouse_xy)
        self.less_on = self.less_bouton.collidepoint(mouse_xy)
        self.more_on = self.more_bouton.collidepoint(mouse_xy)

    def init_grid(self):
        self.grid = [[0] * self.width for i in range(self.height)]

    def random_grid(self):
        """
        Init random grid
        """
        for i in range(self.height):
            for j in range(self.width):
                rd = random.random()

                if rd > 0.6:
                    self.grid[i][j] = 1

                else:
                    self.grid[i][j] = 0

    def display(self):
        """
        Change grid cell's color
        """
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == 0:
                    colour = [0, 0, 0]

                elif self.grid[i][j] == 1:
                    colour = [255, 255, 255]

                elif self.grid[i][j] == 2:
                    colour = [0, 80, 80]

                else:
                    colour = [0, 100, 0]

                self.window.fill(
                    colour,
                    (
                        i * self.pixel_size + 120,
                        j * self.pixel_size,
                        self.pixel_size - 1,
                        self.pixel_size - 1,
                    ),
                )

        pygame.display.flip()

    def next_state(self):
        """
        Computes next state
        """
        buffer = [[0] * self.width for i in range(self.height)]

        for i in range(self.height - self.less):
            for j in range(self.width - self.less):
                nb_alive_cells = self.alive(i, j)

                if nb_alive_cells == 3:
                    buffer[i][j] = 1

                elif nb_alive_cells == 2:
                    buffer[i][j] = self.grid[i][j]

                elif nb_alive_cells > 3:
                    buffer[i][j] = 2

                elif nb_alive_cells < 2:
                    buffer[i][j] = 0

        self.grid = buffer

    def alive(self, i, j):
        """
        Computes Alive cells
        """
        alive_cells = 0

        for x in range(i - self.less, i + self.more):
            for y in range(j - self.less, j + self.more):
                if self.grid[x][y] == 1:
                    alive_cells += 1

        if self.grid[i][j] == 1:
            alive_cells -= 1

        return alive_cells


if __name__ == "__main__":
    obj = GameOfLife()
    obj.run()
