#! /usr/bin/python
# -*- coding:utf-8 -*-
from tkinter import *
import socket, sys, os, threading

class ThreadReception(threading.Thread):
    '''objet thread gérant la réception des messages'''
    def __init__(self, chat):
        threading.Thread.__init__(self)
        self.connexion = chat.connexion # réf. du socket de connexion
        self.liste_message = chat.liste_message
        self._stopevent = threading.Event()

    def run(self):
        while 1:
            nom = ''
            message_recu = self.connexion.recv(1024)
            message_recu = str(message_recu.decode())
            # Découpe le message reçu pour récupérer le nom de l'expéditeur du message
            for index in range(len(message_recu)):
                if message_recu[index] == '*' and message_recu[index+1] == '*':
                    nom = message_recu[:index] + ' : '
                    message_recu = message_recu[index+2:]
                    break
                else:
                    nom = ''
            if message_recu == '' or message_recu.upper() == 'FIN':
                break
            self.liste_message.insert(END, nom + message_recu) # Affichage du message

        print('Client arrêté. Connexion interrompue.')
        self.connexion.close()

class ThreadEmission(threading.Thread):
    '''objet thread gérant l'émission des messages'''
    def __init__(self, chat):
        threading.Thread.__init__(self)
        self.pseudo = chat.pseudo
        self.connexion = chat.connexion # réf. du socket de connexion
        self.identification = 'identification-'+chat.pseudo
        self.connexion.send(self.identification.encode()) # Envoi message "d'identification"

    def envoi(self, message):
        message = "%s" % str(message)
        self.connexion.send(message.encode())

class Accueil(object):
    def __init__(self):
        self.nom = ''
        self.fenetre = Tk() # Initialise la fenetre
        self.fenetre.title('Chat')
        self.affichage_selection_nom()

    def init_nom(self):
        self.nom = self.pseudo.get()
        self.host = self.host.get()
        self.port = self.port.get()
        # Efface les widgets présents
        self.label_pseudo.grid_forget()
        self.label_host.grid_forget()
        self.label_port.grid_forget()
        self.entree_pseudo.grid_forget()
        self.entree_host.grid_forget()
        self.entree_port.grid_forget()
        self.bouton_ok.grid_forget()
        main = Chat(self)

    def Intercepte(self):
        print("Interception de la fermeture de la fenetre")
        self.fenetre.destroy()

    def affichage_selection_nom(self):
        # Crée et place les widgets
        self.label_pseudo = Label(self.fenetre, text = "Pseudo :")
        self.label_pseudo.grid(row=0,column=1, sticky=W)
        self.pseudo = StringVar()
        self.pseudo.set('test')
        self.entree_pseudo = Entry(self.fenetre, textvariable=self.pseudo, width=30)
        self.entree_pseudo.grid(row=0,column=2)

        self.label_host = Label(self.fenetre, text = "Hôte :")
        self.label_host.grid(row=1,column=1, sticky=W)
        self.host = StringVar()
        self.host.set('127.0.0.1')
        self.entree_host = Entry(self.fenetre, textvariable=self.host, width=30)
        self.entree_host.grid(row=1,column=2)

        self.label_port = Label(self.fenetre, text = "Port :")
        self.label_port.grid(row=2,column=1, sticky=W)
        self.port = StringVar()
        self.port.set('10000')
        self.entree_port = Entry(self.fenetre, textvariable=self.port, width=30)
        self.entree_port.grid(row=2,column=2)

        self.bouton_ok=Button(self.fenetre, text="Ok", command=self.init_nom)
        self.bouton_ok.grid(row=4,column=0)

        self.fenetre.protocol("WM_DELETE_WINDOW", self.Intercepte) # Intercepte la fermeture de l'App pour le faire 'correctement'
        self.fenetre.mainloop()

class Chat(object):
    def __init__(self, user):
        self.fenetre = user.fenetre
        self.pseudo = str(user.nom)
        self.host = user.host
        self.port = int(user.port)
        self.connecter = False
        self.main()

    def init_connection(self):
        '''Initialise la connection avec le serveur'''
        self.connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.connexion.connect((self.host, self.port))
            self.connecter = True
        except socket.error:
            print('La connexion a échoué.')
            sys.exit()

        # Dialogue avec le serveur : on lance deux threads pour gérer
        # indépendamment l'émission et la réception des messages :
        self.th_E = ThreadEmission(self)
        self.th_R = ThreadReception(self)

    def envoi(self):
        message = self.message.get() # Récupère la valeur de message
        self.message.set('') # Initialise une valeur par default
        self.th_E.envoi(message)
        message = self.pseudo + ' : ' + message
        self.liste_message.insert(END, message)

    def Intercepte(self):
        self.th_E.envoi(" s'est deconnecter")
        self.fenetre.destroy()

    def main(self):
        self.liste_message = Listbox(self.fenetre)
        self.liste_message.grid(row=0,column=0, columnspan=4, sticky=W+E+N+S)

        self.label_message = Label(self.fenetre, text = "Message :")
        self.label_message.grid(row=1,column=0)

        self.message = StringVar()
        self.entree = Entry(self.fenetre, textvariable=self.message, width=30)
        self.entree.grid(row=1,column=1)

        self.bouton_envoyer=Button(self.fenetre, text="Envoyer", command=self.envoi)
        self.bouton_envoyer.grid(row=1,column=2)

        if self.connecter == False:
            self.init_connection()
            self.th_E.start()
            self.th_R.start()

        self.fenetre.protocol("WM_DELETE_WINDOW", self.Intercepte)
        self.fenetre.mainloop()

if __name__ == '__main__':
    test = Accueil()