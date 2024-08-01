from flask import Flask
from flask_pymongo import PyMongo

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['MONGO_URI'] = 'mongodb+srv://atlasadmin:BseouAiAnmd5FOy1@cluster0.jp5bm2w.mongodb.net/flask_todo_app?retryWrites=true&w=majority'

    mongo = PyMongo(app)
    db = mongo.db

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.learnhtml import learnhtml as learnhtml_blueprint
    app.register_blueprint(learnhtml_blueprint, url_prefix='/learnhtml')

    from app.mongo import mongo as mongo_blueprint
    app.register_blueprint(mongo_blueprint, url_prefix='/')



    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
