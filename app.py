import os
import dumper
from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from geojson import Feature, Point, FeatureCollection

##  from sqlalchemy import *
##  from sqlalchemy.orm import *
##  from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
db.reflect()

class Listing(db.Model):
    __tablename__ = 'listings'

@app.route('/')
def hello():
    return "Hello World!"

feat_props= ("id", "price", "street", "bedrooms", "bathrooms", "sq_ft")

@app.route('/listings')
def listings():
    ary= Listing.query.all()
    collection= FeatureCollection()
    print "collection has %d entries" % (len(collection))
    for r in range(2):
        feature = Feature(geometry=Point(ary[r].long, ary[r].lat))
        feature.properties= {k:r[k] for k in feat_props}
        dumper.dump(feature)
        collection.append(feature)

    return(jsonify(collection))

if __name__ == '__main__':
    app.run()
