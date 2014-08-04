from flask import redirect, url_for,render_template, Flask

class Database(object):
    def __init__(self):
        self.database = []
        self.num = 0
        self.order = 'ascend'
    def put(self, storage):
        self.database.append(storage)
    def out(self):
        return self.database


