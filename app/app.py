from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['MONGO_URI'] = 'mongodb+srv://atlasadmin:BseouAiAnmd5FOy1@cluster0.jp5bm2w.mongodb.net/flask_todo_app?retryWrites=true&w=majority'

mongo = PyMongo(app)
db = mongo.db

@app.route('/')
@app.route('/todos')
def todos():
    if not db:
        return jsonify({"message": "Database connection is not initialized.", "status": "error"})
    try:
        tasks = list(db.tasks.find())  # Ensure 'tasks' is the correct collection name
        return render_template('todo.html', tasks=tasks)
    except Exception as e:
        return jsonify({"message": str(e), "status": "error"}), 500

@app.route('/add_todo', methods=['POST'])
def add_todo():
    try:
        title = request.form.get('title')
        description = request.form.get('description')
        if title and description:
            db.tasks.insert_one({"title": title, "description": description, "completed": False})
        return redirect(url_for('todos'))
    except Exception as e:
        return jsonify({"message": str(e), "status": "error"}), 500

@app.route('/edit_todo/<task_id>', methods=['GET', 'POST'])
def edit_todo(task_id):
    try:
        if request.method == 'POST':
            title = request.form.get('title')
            description = request.form.get('description')
            if title and description:
                db.tasks.update_one({'_id': ObjectId(task_id)}, {"$set": {"title": title, "description": description}})
            return redirect(url_for('todos'))
        task = db.tasks.find_one({"_id": ObjectId(task_id)})
        return render_template('edit_todo.html', task=task)
    except Exception as e:
        return jsonify({"message": str(e), "status": "error"}), 500

@app.route('/delete_todo/<task_id>', methods=['POST'])
def delete_todo(task_id):
    try:
        db.tasks.delete_one({"_id": ObjectId(task_id)})
        return redirect(url_for('todos'))
    except Exception as e:
        return jsonify({"message": str(e), "status": "error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
