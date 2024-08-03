from flask import Blueprint

# Create a Blueprint for the learnhtml section
about = Blueprint('about', __name__, static_folder='static', template_folder='templates')

from app.about import routes
