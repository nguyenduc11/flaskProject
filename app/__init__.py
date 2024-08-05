from flask import Flask
from pymongo import MongoClient

# Initialize global mongo client and database
client = None
db = None


def create_app():
    global client, db  # Access the global client and db variables

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config[
        'MONGO_URI'] = 'mongodb+srv://nguyenduc11:NJtdKiz5DQDU4HE2@clusterflaskweb.refwjuv.mongodb.net/?retryWrites=true&w=majority&appName=ClusterFlaskWeb'

    # Initialize pymongo client and database
    client = MongoClient(app.config['MONGO_URI'])
    db = client.flask_web  # Access the 'flask_web' database

    # Import and register blueprints
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
    app.register_blueprint(math_quiz01_blueprint, url_prefix='/math')

    from app.math_quiz02 import math_quiz02 as math_quiz02_blueprint
    app.register_blueprint(math_quiz02_blueprint, url_prefix='/math')

    from app.math_quiz03 import math_quiz03 as math_quiz03_blueprint
    app.register_blueprint(math_quiz03_blueprint, url_prefix='/math')

    from app.math_quiz04 import math_quiz04 as math_quiz04_blueprint
    app.register_blueprint(math_quiz04_blueprint, url_prefix='/quiz04')

    from app.math_result import math_result as math_result_blueprint
    app.register_blueprint(math_result_blueprint, url_prefix='/mathresult')

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
