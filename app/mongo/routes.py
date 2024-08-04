from app.mongo import mongo
from flask import render_template



@mongo.route('/')
@mongo.route('/basics')
def mongobasics():
    return render_template('mongobasics.html')


@mongo.route('/flask')
def mongoflask():
    return render_template('mongoflask.html')

