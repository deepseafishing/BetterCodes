# -*- coding: utf-8 -*-
# all the imports

from flask import request, redirect, url_for, \
    render_template, Flask
# from apps import app
from database import Database
import logging

app = Flask(__name__)

dataStorage = Database()


@app.route('/', methods=['GET', 'POST'])
def show_entries():
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


@app.route('/del/<idx>', methods=['GET'])
def del_entry(idx):  # del/idx : it comes in via string -- so have to convert to int
    for data in dataStorage.database:  #it is copied 'data'
        if int(idx) == data['num']:
            dataStorage.database.remove(data)
            break  #if you want to del num.2, you can just go around the loop until num2. (not the whole!)
            #if int(idx) == dataStorage.database[i]['num'] :
            #dataStorage.database.pop(i)

    return redirect(url_for('show_entries'))


@app.route('/modify/<idx>', methods=['GET'])
def modify_entry(idx):
    for i in range(len(dataStorage.database)):  #
        if int(idx) == dataStorage.database[i]['num']:
            dataStorage.database[i]['title'] = request.args['title']  #args : b/c "GET"
            dataStorage.database[i]['contents'] = request.args['contents']
            break

    return redirect(url_for('show_entries'))


@app.route('/plus/<idx>', methods=['GET'])
def plus_entry(idx):
    for i in range(len(dataStorage.database)):  #
        if int(idx) == dataStorage.database[i]['num']:
            dataStorage.database[i]['count'] += 1
            break

    return redirect(url_for('show_entries'))

@app.route('/desc', methods=['GET'])
def desc_entry():

    new_list = []
    max_dict = {}
    old_list = dataStorage.database[:]

    while len(old_list) > 0:
        max_count = -100
        for data in old_list:
            if max_count < data['count']:  #max_count : 가장 좋아요 숫자가 높은 글에 좋아요를 저장하게 위해
                max_count = data['count']
                max_dict = data.copy() #

        new_list.append(max_dict)
        old_list.remove(max_dict)

        dataStorage.database = new_list[:]

    return redirect(url_for('show_entries'))

@app.route('/minus/<idx>', methods = ['GET'])
def minus_entry(idx):
    for i in range(len(dataStorage.database)):
        if int(idx) == dataStorage.database[i]['num']:
            if dataStorage.database[i]['count'] > 0 :
                dataStorage.database[i]['count'] -= 1
                break

    return redirect(url_for('show_entries'))

@app.route('/asc', methods=['GET'])
def asc_entry():

    new_list2 = []
    min_dict = {}
    old_list2 = dataStorage.database[:]

    while len(old_list2) > 0:
        min_count = 1000
        if min_count < 0 :
            break
        for item in old_list2:
            if min_count > item['count']:
                min_count = item['count']
                min_dict = item.copy()

        new_list2.append(min_dict)
        old_list2.remove(min_dict)

        dataStorage.database = new_list2[:]

    return redirect(url_for('show_entries'))


app.run(debug=True, port=5040)
