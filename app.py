import os
import dumper
from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy
from geojson import Feature, Point, FeatureCollection

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
db.reflect()

class Listing(db.Model):
    __tablename__ = 'listings'

feat_props= ("id", "price", "street", "status", "bedrooms", "bathrooms", "sq_ft")

@app.route('/listings')
def listings():
    l_query= Listing.query
    min_price= request.args.get('min_price', type=int)
    if min_price is not None:
        l_query= l_query.filter(Listing.price >= min_price)
    max_price= request.args.get('max_price', type=int)
    if max_price is not None:
        l_query= l_query.filter(Listing.price <= max_price)

    min_bed= request.args.get('min_bed', type=int)
    if min_bed is not None:
        l_query= l_query.filter(Listing.bedrooms >= min_bed)
    max_bed= request.args.get('max_bed', type=int)
    if max_bed is not None:
        l_query= l_query.filter(Listing.bedrooms <= max_bed)

    min_bath= request.args.get('min_bath', type=int)
    if min_bath is not None:
        l_query= l_query.filter(Listing.bathrooms >= min_bath)
    max_bath= request.args.get('max_bath', type=int)
    if max_bath is not None:
        l_query= l_query.filter(Listing.bathrooms <= max_bath)

    features= list()
    for entry in l_query.all():
        feature = Feature(geometry=Point((entry.long, entry.lat)))
        feature.properties= {k:getattr(entry, k) for k in feat_props}
        features.append(feature)
        
    retcode= jsonify(FeatureCollection(features))
    return(retcode)

if __name__ == '__main__':
    app.run()
