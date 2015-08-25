#! /usr/bin/python
# -*- coding:utf-8 -*-
# Définition d'un client réseau gérant en parallèle l'émission et la réception des messages (utilisation de 2 THREADS).
import socket, sys, os, threading

host = os.environ.get('RDB_HOST') or '127.0.0.1'
port = 10001
print('Entrez un pseudo :')
pseudo = input()

class ThreadReception(threading.Thread):
    '''objet thread gérant la réception des messages'''
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn           # réf. du socket de connexion
        self._stopevent = threading.Event()

    def run(self):
        while 1:
            nom = ''
            message_recu = self.connexion.recv(1024)
            message_recu = str(message_recu.decode())
            for index in range(len(message_recu)):
                if message_recu[index] == '*' and message_recu[index+1] == '*':
                    nom = message_recu[:index] + ' : '
                    message_recu = message_recu[index+2:]
                    break
                else:
                    nom = ''
            print('--> ' + nom + message_recu)
            if message_recu == '' or message_recu.upper() == 'FIN':
                break
        # Le thread <réception> se termine ici.
        # On force la fermeture du thread <émission> :

        print('Client arrêté. Connexion interrompue.')
        self.connexion.close()


class ThreadEmission(threading.Thread):
    '''objet thread gérant l'émission des messages'''
    def __init__(self, conn, pseudo):
        threading.Thread.__init__(self)
        self.connexion = conn           # réf. du socket de connexion
        self.identification = 'identification-'+pseudo
        self.connexion.send(self.identification.encode())

    def run(self):
        while 1:
            message_emis = input()
            self.connexion.send(message_emis.encode())

# Programme principal - Établissement de la connexion :
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    connexion.connect((host, port))
except socket.error:
    print('La connexion a échoué.')
    sys.exit()

# Dialogue avec le serveur : on lance deux threads pour gérer
# indépendamment l'émission et la réception des messages :
th_E = ThreadEmission(connexion, pseudo)
th_R = ThreadReception(connexion)
th_E.start()
th_R.start()