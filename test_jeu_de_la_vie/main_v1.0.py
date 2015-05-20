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

def main():
    k = 0
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
            pixel.afficher(0)
            print(k)


pixel.initialiser(largeur, hauteur, zoom)
viemorte = []

pixel.marquer(2, 2, 0)
pixel.marquer(2, 3, 0)
pixel.marquer(2, 4, 0)
pixel.marquer(2, 5, 0)

tour = int(input('combien de tour ?'))
z = 0
while z < tour:
    main()
    z += 1



#for i in range(0, 1000000):
#	pixel.marquer(x[randint(2, 97)], y[randint(2, 97)], 0)
#	pixel.marquer(x[randint(2, 97)], y[randint(2, 97)], 1)
#	pixel.afficher(0.0001) #pause de 0.0001 sec
#	print(pixel.lire(5, 6))
pixel.afficher()

#2 le jeu de la vie : http://lionel.chaussade.free.fr/Site_3/Accueil_files/TP6.pdf






pixel.marquer(i, j, ?)
plateau2 = lire()
plateau = numpy.zeros((100, 100), dtype=numpy.uint32)
test()
True - 0
False - 1

#for i in range(0, 100):
for i in range(0, 51):
    j = i
    pixel.marquer(i, j, 0)
    pixel.afficher(0.01)
    i2 = 100 - i
    j2 = 100 - j
    pixel.marquer(i2, j2, 0)
    pixel.afficher(0.01)
    i3 = i
    j3 = 100 - j
    pixel.marquer(i3, j3, 0)
    pixel.afficher(0.01)
    i4 = 100 - i
    j4 = j
    pixel.marquer(i4, j4, 0)
    pixel.afficher(0.01)

for i in range(50, 101):
    j = i
    pixel.marquer(i, 50, 0)
    pixel.afficher(0.01)

    pixel.marquer(50, i, 0)
    pixel.afficher(0.01)

    i2 = 100 - i

    pixel.marquer(i2, 50, 0)
    pixel.afficher(0.01)

    pixel.marquer(50, i2, 0)
    pixel.afficher(0.01)









50/50



input()


