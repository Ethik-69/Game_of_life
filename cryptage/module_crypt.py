import os

def cryptage(path_fichier, cle):
    if path_fichier != '':
        fichier = open(path_fichier, 'r+')
        a_chiffrer = fichier.read()
        dejachiffrer = ''
        for lettre in a_chiffrer:
            if lettre in cle:
                index = cle.index(lettre)
                index += 3
                if index > 52:
                    index -= 52
                dejachiffrer = dejachiffrer + cle[index]
        nouveau_fichier = open('crypt_'+path_fichier, 'w')
        nouveau_fichier.write(dejachiffrer)
        nouveau_fichier.close()
        os.remove(path_fichier)

def decryptage(path_fichier, cle):
    fichier = open(path_fichier, 'r+')
    dejachiffrer = fichier.read()
    dechiffrer = ''
    for lettre in dejachiffrer:
        if lettre in cle:
            index = cle.index(lettre)
            index -= 3
            if index < 0:
                index += 52
            dechiffrer = dechiffrer + cle[index]
    nouveau_fichier = open('decrypt'+path_fichier, 'w')
    nouveau_fichier.write(dechiffrer)
    nouveau_fichier.close()
    os.remove(path_fichier)