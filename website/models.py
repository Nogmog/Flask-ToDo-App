import datetime
from . import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(300), unique = True)
    category = db.Column(db.String(300))
    complete = db.Column(db.Boolean, default = False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.now())