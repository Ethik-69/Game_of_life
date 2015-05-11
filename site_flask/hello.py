#! /usr/bin/python
# -*- coding:utf-8 -*-
#from PIL import image
from StringIO import StringIO
from flask import render_template
from datetime import date
from flask import Flask, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    mots = ["bonjour", "a", "toi,", "visiteur."]
    da = date.today().isoformat()
    return render_template('corps_index.html', titre="Bienvenue !", mots=mots, date=da)


@app.route('/test/')
def test():
        nom = "CHAMIK"
        prenom = "Ethan"
        return "Je suis : {} - {}".format(nom, prenom) + ' nous sommes ici : ' + request.path


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
       return render_template('contact.html', titre="Contact")
    else:
        return render_template('contact.html', titre="Contact")

#@app.route('/contact/')
#def contact():
#    return render_template('contact.html', titre="Contact")


if __name__ == '__main__':
    app.run(debug=True)