from flask import request, redirect, url_for, \
    render_template, Flask
# from apps import app
from apps.models.database import Database

app = Flask(__name__)

dataStorage = Database()

@app.route('/', methods = ['GET'])
def show_total():
    total = dataStorage.out()
    return render_template('show_total.html', total = total)

@app.route('/deposit', methods = ['GET'])
def add_money():
    dataStorage.total += 10
    total = dataStorage.total
    return render_template('show_total.html', total=total)

@app.route('/withdraw', methods = ['GET'])
def wd_money():
    if dataStorage.total > 9 :
        dataStorage.total -= 10
    else :
        dataStorage.total -= 0
    total = dataStorage.total
    return render_template('show_total.html', total=total)

app.run(debug=True, port=5040)