from flask import render_template, redirect, url_for, request, flash
from app.auth import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Add login logic here
        flash('Login functionality is not implemented yet.', 'warning')
        return redirect(url_for('auth.login'))
    return render_template('auth/login.html')
