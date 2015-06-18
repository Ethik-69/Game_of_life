#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from tkinter import *
import module_crypt

cle = 'abcdefghijklmno pqrstuvwxyz\'\"!:;.,?ABCDEFGHIJKLM\nNOPQRSTUVWXYZ'

def crypt():
    module_crypt.cryptage(entree.get(), cle)

def decrypt():
    module_crypt.decryptage(entree.get(), cle)

fenetre = Tk()

label = Label(fenetre, text = "Hello World\n Etrez le nom d'un fichier et choisissez")
label.pack()

value = StringVar()
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()

bouton_crypt=Button(fenetre, text="Crypter", command=crypt)
bouton_crypt.pack()

bouton_decrypt=Button(fenetre, text="Decrypter", command=decrypt)
bouton_decrypt.pack()

bouton_fermer=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton_fermer.pack()

fenetre.mainloop()

