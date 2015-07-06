#! /usr/bin/python
# -*- coding:utf-8 -*-
import os

def ouvrir_fichier():
    path_fichier = raw_input('fichier a utiliser : ')
    fichier = open(path_fichier, 'r+')
    contenu_fichier = fichier.read()
    fichier.close()
    os.remove(path_fichier)
    return contenu_fichier, path_fichier

def chiffrer(pos_lettre, cle):
    transfer = []
    retour = ''
    i = 0
    contenu_fichier, path_fichier = ouvrir_fichier()
    nouveau_fichier = open(path_fichier, 'w')
    for lettre in contenu_fichier:
        if lettre == ' ': transfer.append(' ')
        elif lettre.lower() in pos_lettre:
            if i == len(cle) : i = 0
            transfer.append(pos_lettre[lettre.lower()]+pos_lettre[cle[i]])
            i+=1

    for i in range(len(transfer)):
        if transfer[i] == ' ': retour = retour + ' '
        elif transfer[i] > 26 : transfer[i] -= 26
        retour = retour + ''.join([cle for cle, valeur in pos_lettre.items() if valeur==transfer[i]])
    nouveau_fichier.write(retour)
    nouveau_fichier.close()

def dechiffrer(pos_lettre, cle):
    transfer = []
    retour = ''
    i = 0
    contenu_fichier, path_fichier = ouvrir_fichier()
    nouveau_fichier = open(path_fichier, 'w')
    for lettre in contenu_fichier:
        if lettre == ' ': transfer.append(' ')
        elif lettre.lower() in pos_lettre:
            if i == len(cle) : i = 0
            transfer.append(pos_lettre[lettre.lower()]-pos_lettre[cle[i]])
            i+=1

    for i in range(len(transfer)):
        if transfer[i] == ' ': retour = retour + ' '
        elif transfer[i] < 1 : transfer[i] += 26
        retour = retour + ''.join([cle for cle, valeur in pos_lettre.items() if valeur==transfer[i]])
    nouveau_fichier.write(retour)
    nouveau_fichier.close()

def main():
    pos_lettre = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    cle = 'simplonve'
    fonctionnement = True
    while fonctionnement:
        choix = input('crypt 1 ou decrypt 2 : ')
        if choix == 1: chiffrer(pos_lettre, cle)
        elif choix == 2: dechiffrer(pos_lettre, cle)
        else: fonctionnement = False


if __name__ == '__main__':
    main()

#Dans ce mini tutoriel nous allons nous interesser aux dictionnaires dictionary en anglais Les dictionnaires sont des objets de python permettant dassocier à un ensemble de cles keys une ou des valeurs values Par exemple comme pour un carnet dadresses où à un nom de famille key vous pouvez associer differentes informations values prenom adresse numero de telephone entreprise etc Vous vous apercevrez rapidement avec vos applications python que cette fonctionnalite est particulierement interessante dans de nombreuse situations