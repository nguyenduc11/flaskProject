from flask import Blueprint

# Create a Blueprint for the learnhtml section
learnhtml = Blueprint('learnhtml', __name__)

from app.learnhtml import routes
