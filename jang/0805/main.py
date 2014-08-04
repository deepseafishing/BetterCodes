# -*- coding: utf-8 -*-
# all the imports
from flask import redirect, url_for,\
    render_template, Flask
#from apps import app
from database import Database


app = Flask(__name__)

dataStorage = Database()

@app.route('/')
def show_entries():
    return render_template('index.html', money = dataStorage.money)

@app.route('/add')
def add_money():
    dataStorage.up()
    return redirect(url_for('show_entries'))

@app.route('/del')
def del_money():
    dataStorage.down()
    return redirect(url_for('show_entries'))

app.run(debug=True)

