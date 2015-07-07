#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
nombre = int(sys.argv[1])

def est_premier(nombre):
    if nombre <=1:
        renvoi = str(nombre) + ' est premier'
        print(renvoi)
    else:
        check = 3
        retour = 0

        while check < nombre+1:
            if check % nombre == 0:
                retour += 1
            check += 2

        if retour == 0:
            renvoi = str(nombre) + ' n\'est pas premier'
            print(renvoi)
        else:
            renvoi = str(nombre) + ' est premier'
            print(renvoi)


if __name__=='__main__' : est_premier(nombre)

