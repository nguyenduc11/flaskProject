from flask import Blueprint

# Create a Blueprint for the guess_sum section
guess_sum = Blueprint('guess_sum', __name__, static_folder='static', template_folder='templates')

from app.guess_sum import routes
