#! /usr/bin/python
# -*- coding:utf-8 -*-
# Définition d'un serveur réseau gérant un système de CHAT.
# Utilise les threads pour gérer les connexions clientes en parallèle.
import socket, sys, os, threading

# Adresse ip et port utilisés
HOST = os.environ.get('RDB_HOST') or '127.0.0.1'
PORT = 10001

class ThreadClient(threading.Thread):
    '''Thread pour gérer la connexion avec un client'''
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn
        self.nom = ''

    def run(self):
        # Dialogue avec le client :
        while 1:
            msgClient = str(self.connexion.recv(1024))
            msgClient = msgClient[2:len(msgClient)-1]
            if msgClient[:15] == 'identification-':
                self.nom = msgClient[15:]
                message = "New user : " + self.nom
                for client in conn_client:
                    if client != self.getName(): # ne pas le renvoyer à l'émetteur
                        conn_client[client].send(message.encode())
            else:
                if msgClient.upper() == "FIN" or msgClient == "":
                    break
                message = "%s**%s" % (self.nom, msgClient)
                print(message)
                # Faire suivre le message à tous les autres clients :
                for client in conn_client:
                    if client != self.getName(): # ne pas le renvoyer à l'émetteur
                        conn_client[client].send(message.encode())

        # Fermeture de la connexion :
        self.connexion.close()      # couper la connexion côté serveur
        del conn_client[self.getName()]        # supprimer son entrée dans le dictionnaire
        print("Client %s déconnecté." % self.nom)
        # Le thread se termine ici

# Initialisation du serveur - Mise en place du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()
print("Serveur prêt, en attente de requêtes ...")
mySocket.listen(5)

# Attente et prise en charge des connexions demandées par les clients :
conn_client = {} # dictionnaire des connexions clients
while 1:
    connexion, adresse = mySocket.accept()
    # Créer un nouvel objet thread pour gérer la connexion :
    th = ThreadClient(connexion)
    th.start()
    # Mémoriser la connexion dans le dictionnaire :
    it = th.getName() # identifiant du thread
    conn_client[it] = connexion
    print("Client %s connecté, adresse IP %s, port %s." %\
           (it, adresse[0], adresse[1]))
    # Dialogue avec le client :
    connexion.send("Connection établie. (avec marteau, tourne vis, scie...)".encode())