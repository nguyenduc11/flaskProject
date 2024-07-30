# app/routes.py
from flask import render_template, request, redirect, url_for, flash
from app import app, db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Add your login logic here
        flash('Login functionality is not implemented yet.', 'warning')
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Add your registration logic here
        flash('Registration functionality is not implemented yet.', 'warning')
        return redirect(url_for('register'))
    return render_template('register.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/todo')
def todos():
    tasks = list(db.tasks.find())
    return render_template('todo.html', tasks=tasks)
