from flask import Blueprint

# Create a Blueprint for the learnhtml section
math_quiz01 = Blueprint('math_quiz01', __name__, static_folder='static', template_folder='templates')

from app.math_quiz01 import routes
