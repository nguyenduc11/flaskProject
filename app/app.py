# app/__init__.py
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['MONGO_URI'] = 'mongodb+srv://atlasadmin:BseouAiAnmd5FOy1@cluster0.jp5bm2w.mongodb.net/flask_todo_app?retryWrites=true&w=majority&appName=Cluster0'

mongodb_client = PyMongo(app)
db = mongodb_client.db

from app import routes
