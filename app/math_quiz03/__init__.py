from flask import Blueprint

# Create a Blueprint for the learnhtml section
math_quiz03 = Blueprint('math_quiz03', __name__, static_folder='static', template_folder='templates')

from app.math_quiz03 import routes
