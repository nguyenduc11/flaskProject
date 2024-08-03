from app.about import about
from flask import render_template, request, redirect, url_for

@about.route('/about',methods=['GET'])
def about():
    return render_template('about.html')