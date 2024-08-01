from app.mongo import mongo
from flask import render_template

@mongo.route('/mongo')
def mongo_view():
    return render_template('mongo.html')
