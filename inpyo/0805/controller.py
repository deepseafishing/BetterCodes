# -*- coding: utf-8 -*-
#all the imports

from flask import request, redirect, url_for,render_template, Flask
#from apps import app
from model import Database
import logging

app = Flask(__name__)

dataStorage = Database()


@app.route('/', methods=['GET', 'POST'])
def all_count():
    entries = dataStorage.out()
    return render_template('view.html', entries=entries)

@app.route('/add', methods=['POST'])
def setting():
    dataStorage.count = 0
    return redirect(url_for('all_count'))



@app.route('/plus', methods=['GET'])
def plus_money():
    dataStorage.count += 100

    return redirect(url_for('all_count'))


@app.route('/dis', methods=['GET'])

def dis_money():
    dataStorage.count -= 100

    return redirect(url_for('all_count'))


app.run(debug=True, port=5023)
