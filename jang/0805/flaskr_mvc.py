# -*- coding: utf-8 -*-
# all the imports
import operator
from flask import request, redirect, url_for,\
    render_template, Flask
#from apps import app
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
    storage={}
    storage['num'] = dataStorage.num
    storage['count'] = 0
    storage['title'] = request.form['title']
    storage['contents'] = request.form['contents']

    dataStorage.put(storage)
    dataStorage.num +=1
    return redirect(url_for('show_entries'))

@app.route('/del/<idx>', methods=["GET","POST"])
def del_entry(idx):
    for data in dataStorage.database:
        if data["num"] == int(idx):
            dataStorage.database.remove(data)
            break
    return redirect(url_for('show_entries'))

@app.route('/modify/<idx>',methods=["GET","POST"])
def modify_entry(idx) :
    for i in range(len(dataStorage.database)):
        if dataStorage.database[i]['num'] == int(idx):
            dataStorage.database[i]['title'] = request.args['title']
            dataStorage.database[i]['contents'] = request.args['contents']
            break
    return redirect(url_for('show_entries'))

@app.route('/like/<idx>',methods=["GET","POST"])
def like_entry(idx) :
    for i in range(len(dataStorage.database)):
        if int(idx) == dataStorage.database[i]['num']:
            dataStorage.database[i]['count']+=1
            break
    if dataStorage.sorting == 0 :
        for j in range(len(dataStorage.database)):
            for i in range(len(dataStorage.database)-1):
                if dataStorage.database[i]['count'] < dataStorage.database[i+1]['count']:
                    temp = dataStorage.database[i]
                    dataStorage.database[i] = dataStorage.database[i+1]
                    dataStorage.database[i+1] = temp
    elif dataStorage.sorting == 1 :
        for j in range(len(dataStorage.database)):
            for i in range(len(dataStorage.database)-1):
                if dataStorage.database[i]['count'] > dataStorage.database[i+1]['count']:
                    temp = dataStorage.database[i]
                    dataStorage.database[i] = dataStorage.database[i+1]
                    dataStorage.database[i+1] = temp
    return redirect(url_for('show_entries'))

@app.route('/dislike/<idx>',methods=["GET","POST"])
def dislike_entry(idx) :
    for i in range(len(dataStorage.database)):
        if int(idx) == dataStorage.database[i]['num']:
            dataStorage.database[i]['count']-=1
            if dataStorage.database[i]['count'] <=0:
                dataStorage.database[i]['count'] = 0
            break
    if dataStorage.sorting == 0 :
        for j in range(len(dataStorage.database)):
            for i in range(len(dataStorage.database)-1):
                if dataStorage.database[i]['count'] < dataStorage.database[i+1]['count']:
                    temp = dataStorage.database[i]
                    dataStorage.database[i] = dataStorage.database[i+1]
                    dataStorage.database[i+1] = temp
    elif dataStorage.sorting == 1:
        for j in range(len(dataStorage.database)):
            for i in range(len(dataStorage.database)-1):
                if dataStorage.database[i]['count'] > dataStorage.database[i+1]['count']:
                    temp = dataStorage.database[i]
                    dataStorage.database[i] = dataStorage.database[i+1]
                    dataStorage.database[i+1] = temp

    return redirect(url_for('show_entries'))

@app.route('/dsd/<idx>',methods=["GET","POST"])
def sort(idx):
    if int(idx) == 0:
        dataStorage.sorting = 0
        for j in range(len(dataStorage.database)):
            for i in range(len(dataStorage.database)-1):
                if dataStorage.database[i]['count'] < dataStorage.database[i+1]['count']:
                    temp = dataStorage.database[i]
                    dataStorage.database[i] = dataStorage.database[i+1]
                    dataStorage.database[i+1] = temp
    elif int(idx) == 1:
        dataStorage.sorting =1
        for j in range(len(dataStorage.database)):
            for i in range(len(dataStorage.database)-1):
                if dataStorage.database[i]['count'] > dataStorage.database[i+1]['count']:
                    temp = dataStorage.database[i]
                    dataStorage.database[i] = dataStorage.database[i+1]
                    dataStorage.database[i+1] = temp

    return redirect(url_for('show_entries'))


app.run(debug=True)

