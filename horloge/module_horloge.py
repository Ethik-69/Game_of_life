#!/usr/bin/env python3
import pixel
import os

def zero(x):
    pixel.marquer(2+x, 1, 0)
    pixel.marquer(3+x, 1, 0)
    pixel.marquer(4+x, 1, 0)
    pixel.marquer(1+x, 2, 0)
    pixel.marquer(1+x, 3, 0)
    pixel.marquer(1+x, 4, 0)
    pixel.marquer(1+x, 5, 0)
    pixel.marquer(1+x, 6, 0)
    pixel.marquer(1+x, 7, 0)
    pixel.marquer(2+x, 8, 0)
    pixel.marquer(3+x, 8, 0)
    pixel.marquer(4+x, 8, 0)
    pixel.marquer(5+x, 2, 0)
    pixel.marquer(5+x, 3, 0)
    pixel.marquer(5+x, 4, 0)
    pixel.marquer(5+x, 5, 0)
    pixel.marquer(5+x, 6, 0)
    pixel.marquer(5+x, 7, 0)

def un(x):
    pixel.marquer(2+x, 2, 0)
    pixel.marquer(3+x, 1, 0)
    pixel.marquer(3+x, 2, 0)
    pixel.marquer(3+x, 3, 0)
    pixel.marquer(3+x, 4, 0)
    pixel.marquer(3+x, 5, 0)
    pixel.marquer(3+x, 6, 0)
    pixel.marquer(3+x, 7, 0)
    pixel.marquer(3+x, 8, 0)
    pixel.marquer(2+x, 8, 0)
    pixel.marquer(4+x, 8, 0)

def deux(x):
    pixel.marquer(1+x, 2, 0)
    pixel.marquer(2+x, 1, 0)
    pixel.marquer(3+x, 1, 0)
    pixel.marquer(4+x, 1, 0)
    pixel.marquer(5+x, 2, 0)
    pixel.marquer(5+x, 3, 0)
    pixel.marquer(4+x, 4, 0)
    pixel.marquer(3+x, 5, 0)
    pixel.marquer(2+x, 6, 0)
    pixel.marquer(1+x, 7, 0)
    pixel.marquer(1+x, 8, 0)
    pixel.marquer(2+x, 8, 0)
    pixel.marquer(3+x, 8, 0)
    pixel.marquer(4+x, 8, 0)
    pixel.marquer(5+x, 8, 0)

def trois(x):
    pixel.marquer(1+x, 2, 0)
    pixel.marquer(2+x, 1, 0)
    pixel.marquer(3+x, 1, 0)
    pixel.marquer(4+x, 1, 0)
    pixel.marquer(5+x, 2, 0)
    pixel.marquer(5+x, 3, 0)
    pixel.marquer(4+x, 4, 0)
    pixel.marquer(3+x, 4, 0)
    pixel.marquer(5+x, 5, 0)
    pixel.marquer(5+x, 6, 0)
    pixel.marquer(5+x, 7, 0)
    pixel.marquer(1+x, 7, 0)
    pixel.marquer(2+x, 8, 0)
    pixel.marquer(3+x, 8, 0)
    pixel.marquer(4+x, 8, 0)

def quatre(x):
    pixel.marquer(4+x, 1, 0)
    pixel.marquer(4+x, 2, 0)
    pixel.marquer(4+x, 3, 0)
    pixel.marquer(4+x, 4, 0)
    pixel.marquer(4+x, 5, 0)
    pixel.marquer(4+x, 6, 0)
    pixel.marquer(4+x, 7, 0)
    pixel.marquer(4+x, 8, 0)
    pixel.marquer(1+x, 5, 0)
    pixel.marquer(2+x, 5, 0)
    pixel.marquer(3+x, 5, 0)
    pixel.marquer(4+x, 5, 0)
    pixel.marquer(5+x, 5, 0)
    pixel.marquer(1+x, 4, 0)
    pixel.marquer(2+x, 3, 0)
    pixel.marquer(3+x, 2, 0)

def cinq(x):
    pixel.marquer(1+x, 1, 0)
    pixel.marquer(2+x, 1, 0)
    pixel.marquer(3+x, 1, 0)
    pixel.marquer(4+x, 1, 0)
    pixel.marquer(5+x, 1, 0)
    pixel.marquer(1+x, 2, 0)
    pixel.marquer(1+x, 3, 0)
    pixel.marquer(1+x, 4, 0)
    pixel.marquer(2+x, 4, 0)
    pixel.marquer(3+x, 4, 0)
    pixel.marquer(4+x, 4, 0)
    pixel.marquer(5+x, 5, 0)
    pixel.marquer(5+x, 6, 0)
    pixel.marquer(5+x, 7, 0)
    pixel.marquer(4+x, 8, 0)
    pixel.marquer(3+x, 8, 0)
    pixel.marquer(2+x, 8, 0)
    pixel.marquer(1+x, 7, 0)

def six(x):
    pixel.marquer(3+x, 1, 0)
    pixel.marquer(4+x, 1, 0)
    pixel.marquer(2+x, 2, 0)
    pixel.marquer(1+x, 3, 0)
    pixel.marquer(1+x, 4, 0)
    pixel.marquer(2+x, 4, 0)
    pixel.marquer(3+x, 4, 0)
    pixel.marquer(4+x, 4, 0)
    pixel.marquer(1+x, 5, 0)
    pixel.marquer(1+x, 6, 0)
    pixel.marquer(1+x, 7, 0)
    pixel.marquer(5+x, 5, 0)
    pixel.marquer(5+x, 6, 0)
    pixel.marquer(5+x, 7, 0)
    pixel.marquer(2+x, 8, 0)
    pixel.marquer(3+x, 8, 0)
    pixel.marquer(4+x, 8, 0)

def sept(x):
    pixel.marquer(1+x, 1, 0)
    pixel.marquer(2+x, 1, 0)
    pixel.marquer(3+x, 1, 0)
    pixel.marquer(4+x, 1, 0)
    pixel.marquer(5+x, 1, 0)
    pixel.marquer(5+x, 2, 0)
    pixel.marquer(4+x, 3, 0)
    pixel.marquer(4+x, 4, 0)
    pixel.marquer(3+x, 5, 0)
    pixel.marquer(3+x, 6, 0)
    pixel.marquer(2+x, 7, 0)
    pixel.marquer(2+x, 8, 0)

def huit(x):
    pixel.marquer(2+x, 1, 0)
    pixel.marquer(3+x, 1, 0)
    pixel.marquer(4+x, 1, 0)
    pixel.marquer(1+x, 2, 0)
    pixel.marquer(1+x, 3, 0)
    pixel.marquer(5+x, 2, 0)
    pixel.marquer(5+x, 3, 0)
    pixel.marquer(2+x, 4, 0)
    pixel.marquer(3+x, 4, 0)
    pixel.marquer(4+x, 4, 0)
    pixel.marquer(1+x, 5, 0)
    pixel.marquer(1+x, 6, 0)
    pixel.marquer(1+x, 7, 0)
    pixel.marquer(5+x, 5, 0)
    pixel.marquer(5+x, 6, 0)
    pixel.marquer(5+x, 7, 0)
    pixel.marquer(2+x, 8, 0)
    pixel.marquer(3+x, 8, 0)
    pixel.marquer(4+x, 8, 0)

def neuf(x):
    pixel.marquer(2+x, 1, 0)
    pixel.marquer(3+x, 1, 0)
    pixel.marquer(4+x, 1, 0)
    pixel.marquer(1+x, 2, 0)
    pixel.marquer(1+x, 3, 0)
    pixel.marquer(1+x, 4, 0)
    pixel.marquer(5+x, 2, 0)
    pixel.marquer(5+x, 3, 0)
    pixel.marquer(5+x, 4, 0)
    pixel.marquer(5+x, 5, 0)
    pixel.marquer(5+x, 6, 0)
    pixel.marquer(2+x, 5, 0)
    pixel.marquer(3+x, 5, 0)
    pixel.marquer(4+x, 5, 0)
    pixel.marquer(4+x, 7, 0)
    pixel.marquer(2+x, 8, 0)
    pixel.marquer(3+x, 8, 0)

def deux_point(x):
    pixel.marquer(1+x, 2, 0)
    pixel.marquer(1+x, 3, 0)
    pixel.marquer(1+x, 6, 0)
    pixel.marquer(1+x, 7, 0)

def effacer(x):
   for i in range(0, 6):
       for j in range(0, 9):
            pixel.marquer(i+x, j, 1)

def afficher(heure, x):
        if heure == '1':
            effacer(x)
            un(x)
        elif heure == '2':
            effacer(x)
            deux(x)
        elif heure == '3':
            effacer(x)
            trois(x)
        elif heure == '4':
            effacer(x)
            quatre(x)
        elif heure == '5':
            effacer(x)
            cinq(x)
        elif heure == '6':
            effacer(x)
            six(x)
        elif heure == '7':
            effacer(x)
            sept(x)
        elif heure == '8':
            effacer(x)
            huit(x)
        elif heure == '9':
            effacer(x)
            neuf(x)
        elif heure == '0':
            effacer(x)
            zero(x)
        elif heure == ':':
            effacer(x)
            deux_point(x+2)

def test(heure):
    for i in range(0, len(heure)):
        if i == 0:
                afficher(heure[i], 0)
        elif i == 1:
                afficher(heure[i], 6)
        elif i == 2:
                afficher(heure[i], 12)
        elif i == 3:
                afficher(heure[i], 18)
        elif i == 4:
                afficher(heure[i], 24)
        elif i == 5:
                afficher(heure[i], 30)
        elif i == 6:
                afficher(heure[i], 36)
        elif i == 7:
                afficher(heure[i], 42)
