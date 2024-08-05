from flask import Blueprint

# Create a Blueprint for the learnhtml section
math_quiz04 = Blueprint('math_quiz04', __name__, static_folder='static', template_folder='templates')

from app.math_quiz04 import routes
