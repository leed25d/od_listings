import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class Listings(db.Model):
    __tablename__ = 'listings'
    id = db.Column(db.Integer, primary_key=True)

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/listings')
def listings():
    ret=''
    ary= Listings.query.all()
    return "%d rows" % (len(ary))

    for r in range(50):
        ret += str(ary[r])
    return ret

if __name__ == '__main__':
    app.run()
