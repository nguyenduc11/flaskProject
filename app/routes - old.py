# app/routes.py
from flask import render_template, request, redirect, url_for, flash, jsonify
from app import app, db


from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import ColumnDataSource

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





@app.route('/todos')
def todos():
    tasks = list(db.tasks.find())
    return render_template('todos.html', tasks=tasks)








@app.route('/todos', methods=['POST'])
def add_todo():
    print(request)
    title = request.form.get('title')
    description = request.form.get('description')
    if title and description:
        db.tasks.insert_one({'title': title, 'description': description, 'completed': False})
        return redirect("/")
    else:
        return jsonify({'error': 'Title and description are required.'}), 400




def generate_column_chart_html(number1, number2, number3):
    # Create a new plot
    plot = figure(title="Column Chart")

    # Create a ColumnDataSource with the data
    data = {'x': ['Number 1', 'Number 2', 'Number 3'], 'y': [number1, number2, number3]}
    source = ColumnDataSource(data=data)

    # Add the column glyph to the plot
    plot.vbar(x='x', top='y', width=0.9, source=source)

    # Generate the HTML for the plot
    script, div = components(plot)
    return script, div



@app.route('/bokeh', methods=['GET', 'POST'])
def bokeh_view():
    if request.method == 'POST':
        number1 = int(request.form.get('number1'))
        number2 = int(request.form.get('number2'))
        number3 = int(request.form.get('number3'))
        script, div = generate_column_chart_html(number1, number2, number3)
        return render_template('bokeh.html', plot_html=script + div)
    else:
        return render_template('bokeh.html')

