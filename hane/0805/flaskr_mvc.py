# -*- coding: utf-8 -*-
# all the imports

from flask import request, redirect, url_for,\
    render_template, Flask
#from apps import app
from database import Database
import logging

app = Flask(__name__)

dataStorage = Database()

@app.route('/ascend', methods=['GET'])
def ascend():
    if dataStorage.order == 'descend':
        dataStorage.order = 'ascend'

    return redirect(url_for('show_entries'))

@app.route('/descend', methods=['GET'])
def descend():
    if dataStorage.order == 'ascend':
        dataStorage.order = 'descend'
    return redirect(url_for('show_entries'))

def sort():
    new_list = []
    max_dict = {}
    old_list = dataStorage.database[:]

    while len(old_list) > 0:
        max_count = -100
        for data in old_list:
            if max_count < data['count']:
                max_count = data['count']
                max_dict= data.copy()

        new_list.append(max_dict)
        old_list.remove(max_dict)

    if dataStorage.order == 'ascend':
        dataStorage.database = new_list[:]
    else:
        dataStorage.database = new_list[::-1]


@app.route('/', methods=['GET', 'POST'])
def show_entries():
    sort()
    entries = dataStorage.out()
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    storage = {}

    storage['num'] = dataStorage.num
    storage['count'] = 0
    storage['title'] = request.form['title']
    storage['contents'] = request.form['contents']

    dataStorage.put(storage)
    dataStorage.num += 1

    return redirect(url_for('show_entries'))


@app.route('/del/<idx>', methods = ['GET'])
def del_entry(idx):
    for data in dataStorage.database:
        if int(idx) == data['num']:
            dataStorage.database.remove(data)
            break
    return redirect(url_for('show_entries'))


@app.route('/modify/<idx>', methods = ['GET'])
def modify_entry(idx):
    for i in range(len(dataStorage.database)):
        if int(idx) == dataStorage.database[i]['num']:
            dataStorage.database[i]['title'] = request.args['title']
            dataStorage.database[i]['contents'] = request.args['contents']
            break
    return redirect(url_for('show_entries'))


@app.route('/plus/<idx>', methods = ['GET'])
def plus_entry(idx):
    for i in range(len(dataStorage.database)):
        if int(idx) == dataStorage.database[i]['num']:
            dataStorage.database[i]['count'] += 1
            break
    return redirect(url_for('show_entries'))


@app.route('/minus/<idx>', methods = ['GET'])
def minus_entry(idx):
    for i in range(len(dataStorage.database)):
        if int(idx) == dataStorage.database[i]['num']:
            if dataStorage.database[i]['count'] >0:
                dataStorage.database[i]['count'] -= 1
                break
    return redirect(url_for('show_entries'))





app.run(debug=True, port=5050)
