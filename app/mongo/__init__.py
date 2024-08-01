from flask import Blueprint

# Create a Blueprint for the learnhtml section
mongo = Blueprint('mongo', __name__, static_folder='static', template_folder='templates')

from app.mongo import routes
