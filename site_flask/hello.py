#! /usr/bin/python
# -*- coding:utf-8 -*-
import os
import json
import argparse
import rethinkdb as rdb
from datetime import date
from werkzeug import secure_filename
from rethinkdb.errors import RqlRuntimeError, RqlDriverError
from flask import Flask, request, redirect, flash, render_template
from flask import Flask, g, jsonify, render_template, request, abort

RDB_HOST =  os.environ.get('RDB_HOST') or 'localhost'
RDB_PORT = os.environ.get('RDB_PORT') or 28015
TODO_DB = 'todoapp'

def dbSetup():
    connection = rdb.connect(host=RDB_HOST, port=RDB_PORT)
    try:
        rdb.db_create(TODO_DB).run(connection)
        rdb.db(TODO_DB).table_create('todos').run(connection)
        print 'Database setup completed. Now run the app without --setup.'
    except RqlRuntimeError:
        print 'App database already exists. Run the app without --setup.'
    finally:
        connection.close()

app = Flask(__name__)
app.config.from_object(__name__)

@app.before_request
def before_request():
    try:
        g.rdb_conn = rdb.connect(host=RDB_HOST, port=RDB_PORT, db=TODO_DB)
    except RqlDriverError:
        abort(503, "No database connection could be established.")

@app.teardown_request
def teardown_request(exception):
    try:
        g.rdb_conn.close()
    except AttributeError:
        pass

@app.route('/')
def index():
    mots = ["bonjour", "a", "toi,", "visiteur."]
    da = date.today().isoformat()
    return render_template('corps_index.html', titre="Bienvenue !", mots=mots, date=da)

def requet(nom, date):
    rdb.db('todoapp').table('todos').insert([{ 'name' : nom, 'date' : date}]).run(g.rdb_conn)
    flash('Task Added')



def delete(id):
    rdb.db('todoapp').table("todos").get(id).delete().run(g.rdb_conn)
    flash('Task Deleted : '+id)



@app.route('/todo/', methods=['GET', 'POST'])
def todo():
    if request.method == 'GET':
        flash('ToDo :')
    else:
        if request.method == 'POST':
            if request.form['submit'] == 'add':
                requet(request.form['nom'], request.form['date'])
            elif request.form['submit'] == 'X':
                delete(request.form['del'])
    list_task = list(rdb.table('todos').run(g.rdb_conn))
    return render_template('corps_todo.html', titre="Contact", list_task=list_task)





if __name__ == '__main__':
    app.secret_key = '\xf8\xff\xbc\xfe\xde\x03\x8b\x81\xc9\x9c\xc4\xbe\x95\xa2\xf2'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
