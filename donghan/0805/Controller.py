# -*- coding: utf-8 -*-
from flask import request, url_for, redirect,\
    render_template, Flask

from models.Money import Moneycheck

app = Flask(__name__)

money_amount = Moneycheck()

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html', money_amount = money_amount.amount)

@app.route('/plus', methods=['GET'])
def plus():
    money_amount.amount += 10
    return redirect(url_for('index'))

@app.route('/minus', methods=['GET'])
def minus():
    if money_amount.amount >= 10:
        money_amount.amount -= 10

    return redirect(url_for('index'))

app.run(debug=True)
