from flask import Blueprint

# Create a Blueprint for the learnhtml section
math_result = Blueprint('math_result', __name__, static_folder='static', template_folder='templates')

from app.math_result import routes
