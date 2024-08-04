from flask import Blueprint

# Create a Blueprint for the math_quiz02 section
math_quiz02 = Blueprint('math_quiz02', __name__, static_folder='static', template_folder='templates')

from app.math_quiz02 import routes
