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
    ##print "ary has %d entries" % (len(ary))
    features= list()
    ##print "collection has %d entries" % (len(collection))
    for r in range(2):
        print "r= %d" %(r)
        feature = Feature(geometry=Point((ary[r].long, ary[r].lat)), 
                              properties={})
        try:
            feature.properties= {k:ary[r][k] for k in feat_props}
        except Exception, e:
            print "properties exception %s" % (e)

        dumper.dump(feature)
        features.append(feature)
    
    try:
        collection= FeatureCollection(features)
    except Exception, e:
        print "collection exception %s" % (e)
    retcode= jsonify(collection)
    print retcode
    return(retcode)

if __name__ == '__main__':
    app.run()
