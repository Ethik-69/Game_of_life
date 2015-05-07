#!/usr/bin/env python3
from random import randint
import os
import pixel

largeur = 100
hauteur = 100
zoom = 5
#x = int(input('x :'))
#y = int(input('y :'))
l = 500
x = y = []

#remplie tableau x et y
for i in range(0, l):
	x.append(i)
	y.append(i)

def cadre():
	for i in range(0, 200):
#haut
			pixel.marquer(0, y[i])
#gauche			
			pixel.marquer(x[i], 0)
#droite	
			pixel.marquer(199, y[i])
#bas
			pixel.marquer(x[i], 199)

#test les 8 case autour de x, y
def testviemort(x, y):
    viemorte = []
    viemorte.append(int(pixel.lire(x-1, y-1)))
    viemorte.append(int(pixel.lire(x, y-1)))
    viemorte.append(int(pixel.lire(x+1, y-1)))
    viemorte.append(int(pixel.lire(x+1, y)))
    viemorte.append(int(pixel.lire(x+1, y+1)))
    viemorte.append(int(pixel.lire(x, y+1)))
    viemorte.append(int(pixel.lire(x-1, y+1)))
    viemorte.append(int(pixel.lire(x-1, y)))
    return viemorte

pixel.initialiser(largeur, hauteur, zoom)
viemorte = []

pixel.marquer(2, 2, 0)
pixel.marquer(2, 3, 0)
pixel.marquer(2, 4, 0)
pixel.marquer(2, 5, 0)


k = 0
z = 1
while z == 1:
    for i in range(1, 99):
        for j in range(1, 99):
            k += 1
            viemorte = testviemort(i, j)
            vivante = viemorte.count(0)
            if vivante == 2:
                pixel.marquer(i, j, 0)
            elif vivante == 3:
                pixel.marquer(i, j, 0)
            elif vivante < 2:
                pixel.marquer(i, j, 1)
            elif vivante > 3:
                pixel.marquer(i, j, 1)
            elif vivante == 3:
                pixel.marquer(i, j, 0)
            pixel.afficher(0.0000000000000000000000000000000001)

print(k)


#for i in range(0, 1000000):
#	pixel.marquer(x[randint(2, 97)], y[randint(2, 97)], 0)
#	pixel.marquer(x[randint(2, 97)], y[randint(2, 97)], 1)
#	pixel.afficher(0.0001) #pause de 0.0001 sec
#	print(pixel.lire(5, 6))
pixel.afficher()

#2 le jeu de la vie : http://lionel.chaussade.free.fr/Site_3/Accueil_files/TP6.pdf
