# -*- coding: utf-8 -*-
# all the imports
from flask import request, redirect, url_for,\
    render_template, Flask
#from apps import app
from database import Database

app = Flask(__name__)
dataStorage = Database()

@app.route('/', methods=['GET', 'POST'])
def index():
    money = dataStorage.out()
    return render_template('index.html', money=money)

@app.route('/plus', methods=['GET'])
def plus():
    dataStorage.money += 10
    return redirect(url_for('index'))

@app.route('/minus', methods=['GET'])
def minus():
    if dataStorage.money == 0:
        dataStorage.money == 0
    else:
        dataStorage.money -= 10
    return redirect(url_for('index'))

app.run(debug=True, port=5040)




