#! /usr/bin/python
# -*- coding:utf-8 -*-
import os
import demjson
import rethinkdb as rdb
from rethinkdb.errors import RqlRuntimeError, RqlDriverError
RDB_HOST =  os.environ.get('RDB_HOST') or 'localhost'
RDB_PORT = os.environ.get('RDB_PORT') or 28015
TODO_DB = 'partage'

rdb.connect(host=RDB_HOST, port=RDB_PORT, db=TODO_DB).repl()

def dbSetup():
    connection = rdb.connect(host=RDB_HOST, port=RDB_PORT)
    rdb.db_create(TODO_DB).run(connection)
    rdb.db(TODO_DB).table_create('lien').run(connection)
    print 'Database setup completed. Now run the app without --setup.'
dbSetup()

def requet(titre, url, description, categorie):
    rdb.db('partage').table('lien').insert([{ 'titre' : titre, 'url' : url, 'description' : description, 'categorie' : categorie}]).run()

def select_categorie(from_url, title):
    if 'nextinpact' in from_url :categorie = 'articles'
    elif 'phonandroid' in from_url :categorie = 'articles'
    elif 'futura-sciences' in from_url :categorie = 'articles'
    elif 'semageek' in from_url :categorie = 'articles'
    elif 'github' in from_url:categorie = 'github'
    elif 'youtube' in from_url:categorie = 'videos'
    elif 'doc.ubuntu' in from_url:categorie = 'docs'
    elif 'openclassrooms' in from_url:categorie = 'e-learning'
    elif 'commitstrip' in from_url:categorie = 'detente'
    elif 'allocine' in from_url:categorie = 'detente'
    elif 'twitter' in from_url: categorie = 'poubelle'
    elif 'twitter' in title: categorie = 'poubelle'
    else : categorie = 'divers'
    return categorie

def recup(path_fichier):
    nom_champ = ['title', 'from_url' ,'text']
    emp_fichier = open(path_fichier, 'r+')
    fichier = emp_fichier.read()
    fichier_decod = demjson.decode(fichier)
    for i in range(len(fichier_decod)):
        if 'attachments' in fichier_decod[i]:
            atta = fichier_decod[i]['attachments'][0]
            for k in range(len(nom_champ)):
                if 'title' in atta: title = atta['fallback']
                else: title = atta['fallback']
                if 'from_url' in atta: from_url = atta['from_url']
                else: from_url =' '
                if 'text' in atta: text = atta['text']
                else: text =' '
                categorie = select_categorie(from_url, title)
            if categorie != 'poubelle':requet(title, from_url, text, categorie)
            print('-------------------------------')

dossier = os.listdir('import_json')

for i in range(len(dossier)):
    path_dossier = 'import_json/' + dossier[i]
    fichier = os.listdir(path_dossier)
    for j in range(len(fichier)):
        path_fichier = path_dossier + '/' + fichier[j]
        recup(path_fichier)