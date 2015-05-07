#!/usr/bin/env python3
from random import randint
import os
import pixel
import module_horloge
from time import localtime, strftime

largeur = 50
hauteur = 10
zoom = 5
l = 300
k = 1

pixel.initialiser(largeur, hauteur, zoom)

while k == 1:
    heure = strftime("%H:%M:%S", localtime())
    module_horloge.test(heure)
    pixel.afficher(1)