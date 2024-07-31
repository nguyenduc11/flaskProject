from app.learnhtml import learnhtml
from flask import render_template

@learnhtml.route('/learnhtml')
def placeholder():
    return render_template('learnhtml/placeholder.html')
