from app.mongo import mongo
from flask import render_template

@mongo.route('/mongo')
def mongo():
    return render_template('mongo.html')
