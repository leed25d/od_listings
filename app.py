import os
import dumper
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
db.reflect()

class Listing(db.Model):
    __tablename__ = 'listings'
    ##id = db.Column(db.Integer, primary_key=True)

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/listings')
def listings():
    ary= Listing.query.all()
    for r in range(50):
        pass
    ret= dumper.dump(ary[0])
    return ret

if __name__ == '__main__':
    app.run()
