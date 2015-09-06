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
    ##ary= Listing.query.all()
    try:
        l_query= Listing.query
        min_price= request.args.get('min_price', type=int)
        if min_price is not None:
            l_query= l_query.filter(Listing.price >= min_price)
        max_price= request.args.get('max_price', type=int)
        if max_price is not None:
            l_query= l_query.filter(Listing.price <= max_price)

##        min_bed= request.args.get('min_bed', type=int)
##        if min_bed is not None:
##            l_query= l_query.filter(Listing.min_bed >= min_bed)
##        max_bed= request.args.get('max_bed', type=int)
##        if max_bed is not None:
##            l_query= l_query.filter(Listing.max_bed <= max_bed)
##
##        min_bath= request.args.get('min_bath', type=int)
##        if min_bath is not None:
##            l_query= l_query.filter(Listing.min_bath >= min_bath)
##        max_bath= request.args.get('max_bath', type=int)
##        if max_bath is not None:
##            l_query= l_query.filter(Listing.max_bath <= max_bath)

    except Exception, e:
        print "exception %s" % (str(e))
    try:
        features= list()
        ary= l_query.all()
        ##print "%d entried: %s" % (len(q_list), dumper.dumps(q_list))

        for r, entry in enumerate(ary):
            feature = Feature(geometry=Point((ary[r].long, ary[r].lat)))
            feature.properties= {k:getattr(ary[r], k) for k in feat_props}
            features.append(feature)

        retcode= jsonify(FeatureCollection(features))

    except Exception, e:
        print "exception2 %s" % (str(e))

    return(retcode)

if __name__ == '__main__':
    app.run()
