#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import sys, os, random

def clear():
    os.system('clear')

def test_special(chaine):
    if len(chaine) != 5:
        return False
    else:
        for lettre in chaine:
            if '0' <= lettre <= '9' or 'a' <= lettre <= 'z' or 'A' <= lettre <= 'Z':
                return False
        return True

while 1:
    print('entrez un mot en minuscules (entre 6 et 10 caractères) :')
    min = input()
    clear()
    if min.islower() and 6 <= len(min) <= 10:
        break
    else:
        print('louper, recommence !')
        continue

while 1:
    print('entrez un mot en majuscules (entre 6 et 10 caractères) :')
    maj = input()
    clear()
    if maj.isupper() and 6 <= len(maj) <= 10:
        break
    else:
        print('louper, recommence !')
        continue

while 1:
    try:
        print('entrez cinq chiffres :')
        chiffre = int(input())
        clear()
        if len(str(chiffre)) != 5:
            print('louper, recommence !')
            continue
        else:
            break
    except:
        print('louper, recommence !')
        continue

while 1:
    print('entrez cinq caractères spéciaux :')
    car_spec = input()
    clear()
    if test_special(car_spec) == True:
        break
    else:
        print('louper, recommence !')
        continue

base_mdp = min+maj+str(chiffre)+car_spec
mdp = ''

while len(base_mdp) > 0:
    rand = random.randint(0, len(base_mdp)-1)
    mdp = mdp + base_mdp[rand]
    base_mdp = base_mdp[:rand]+base_mdp[rand+1:]

print(mdp)
