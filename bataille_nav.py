#!/usr/bin/env python3
import os
import random
import sys

l = 1

def faire_plateau():
    plateau = []
    for x in range(0, 5):
        plateau.append(["O"] * 5)
    return plateau

def print_plateau(plateau):
    for row in plateau:
                print " ".join(row)

while l == 1:
    plateau = faire_plateau()
    tour = 0
    k = 0
    j = 0
    while k == 0:
        bateaux = random.randint(0, len(plateau)-1)
        bateauy = random.randint(0, len(plateau)-1)
        bateau2x = random.randint(0, len(plateau)-1)
        bateau2y = random.randint(0, len(plateau)-1)

        if bateau2x == bateaux and bateau2y == bateauy:
            k = 0
        else:
            k = 1

    while j < 2:
        print_plateau(plateau)
        tirx = input('tir x :')
        tiry = input('tir y :')

        if tirx > len(plateau) or tiry > len(plateau):
            os.system('clear')
            print('merci de tirer dans l\'eau')
            continue

        elif tirx == bateaux and tiry == bateauy:
            plateau[tiry-1][tirx-1] = '1'
            os.system('clear')
            print('bateau 1 couler!')
            j += 1
            tour += 1
            continue

        elif tirx == bateau2x and tiry == bateau2y:
            plateau[tiry-1][tirx-1] = '2'
            os.system('clear')
            print('bateau 2 couler!')
            j += 1
            tour += 1
            continue

        elif plateau[tiry-1][tirx-1] == 'x':
            os.system('clear')
            print('deja tirer ici')
            continue

        else:
            plateau[tiry-1][tirx-1] = 'x'
            tour += 1
            os.system('clear')
            continue

    raw_input()

    print('vous avez trouver en {0} coup'.format(tour))
    l = input('voulez vous rejouer : O=1 N=0 :')