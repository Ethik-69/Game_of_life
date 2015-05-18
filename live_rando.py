#!/usr/bin/env python3
import random
import os

nb_atrouver = random.randint(0, 501)

print('un nombre entre 0 et 500 a ete trouve, a vous de le retrouver')

verification = False
compteur_tour = 0

while verification == False:

    nombre_entre = int(input('Entrez un nombre : '))

    if nombre_entre > 500 or nombre_entre < 0:
        print("Merci d'entrer un nombre entre 0 et 500 !")

    elif nombre_entre < nb_atrouver:
        os.system('clear')
        print("le nombre a trouver est plus grand que {}".format(nombre_entre))
        compteur_tour += 1


    elif nombre_entre > nb_atrouver:
        os.system('clear')
        print("le nombre a trouver est plus petit que {}".format(nombre_entre))
        compteur_tour += 1


    else:
        os.system('clear')
        print("Vous avez trouve en {} tours, c'etait {}".format(compteur_tour, nb_atrouver))
        verification = True
