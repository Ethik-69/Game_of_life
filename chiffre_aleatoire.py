#!/usr/bin/env python3
import os
import random
k = 0

while k < 1:

    atrouver = random.randint(0, 501)
    i = 0
    tour = l = 0
    k = 1

    print("un nombre entre 0 et 500 a ete selectionner a vous de le trouver")

    while i < 1:
        userinput = input("entrez un nombre :")

        if type(userinput) != int:
            os.system('clear')
            print("merci d'entrez un nombre")

        elif userinput > 500:
            os.system('clear')
            print("merci d'entrez un nombre entre 0 et 500")

        elif userinput > atrouver:
            os.system('clear')
            print("Le nombre a trouver est plus petit que {0}".format(userinput))
            tour+=1
        elif userinput < atrouver:
            os.system('clear')
            print("Le nombre a trouver est plus grand que {0}".format(userinput))
            tour+=1
        elif userinput == atrouver:
            i = 1

    if tour < 11 :
        print('Bravo vous avez trouver en {} coup'.format(tour))
    else:
        print ('Vous avez trouver en {} coup'.format(tour))

    while l < 1:
        rejouer = raw_input("voulez vous rejouer ? O/N ")

        if rejouer in "Oo":
            k = 0
            os.system('clear')
            break
        elif rejouer in "Nn":
            k = 1
            break
        elif rejouer not in "OoNn":
            l = 0
        os.system('clear')