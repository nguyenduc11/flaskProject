from flask import Flask
from flask_pymongo import PyMongo

# Initialize global mongo object
mongo = None

def create_app():
    global mongo  # Access the global mongo variable

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['MONGO_URI'] = 'mongodb+srv://nguyenduc11:NJtdKiz5DQDU4HE2@clusterflaskweb.refwjuv.mongodb.net/?retryWrites=true&w=majority&appName=ClusterFlaskWeb'

    mongo = PyMongo(app)  # Initialize PyMongo
    # db = mongo.db
    # print(db)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from app.about import about as about_blueprint
    app.register_blueprint(about_blueprint)

    from app.learnhtml import learnhtml as learnhtml_blueprint
    app.register_blueprint(learnhtml_blueprint, url_prefix='/learnhtml')

    from app.mongo import mongo as mongo_blueprint
    app.register_blueprint(mongo_blueprint, url_prefix='/mongo')
    from app.to_do_list import to_do_list as to_do_list_blueprint
    app.register_blueprint(to_do_list_blueprint, url_prefix='/todo')

    from app.math_quiz01 import math_quiz01 as math_quiz01_blueprint
    app.register_blueprint(math_quiz01_blueprint)

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
