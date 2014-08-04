__author__ = 'HANE'
from flask import request, redirect, url_for,render_template, Flask
from model import Money
app = Flask(__name__)

counter = Money()

@app.route('/', methods = ['GET'])
def final():
    total = counter.total()
    return render_template('view.html', total=total)

@app.route('/minus', methods = ['GET'])
def minus():
    if counter.money > 0:
        counter.money -= 10
    else:
        counter.money = 0
    return redirect(url_for('final'))

@app.route('/plus', methods = ['GET'])
def plus():
    counter.money += 10
    return redirect(url_for('final'))


app.run(debug=True, port=5040)