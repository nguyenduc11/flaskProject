from flask import Blueprint

# Create a Blueprint for the to-do list section
to_do_list = Blueprint('to_do_list', __name__, static_folder='static', template_folder='templates')

# Import the routes after creating the Blueprint
from app.to_do_list import routes
