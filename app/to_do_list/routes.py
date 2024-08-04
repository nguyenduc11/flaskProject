from flask import request, jsonify, render_template, redirect, url_for
from bson import ObjectId
from app import db  # Import the global db object
from app.to_do_list import to_do_list

# Define the blueprint


@to_do_list.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task = {
        "task": data.get("task"),
        "description": data.get("description"),
        "priority": data.get("priority"),
        "status": data.get("status"),
        "due_date": data.get("due_date")
    }
    result = db.to_do_list.insert_one(task)
    return jsonify({"_id": str(result.inserted_id)}), 201

@to_do_list.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = []
    for task in db.to_do_list.find():
        task['_id'] = str(task['_id'])
        tasks.append(task)
    return render_template('to_do_list.html', tasks=tasks)

@to_do_list.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    task = db.to_do_list.find_one({"_id": ObjectId(task_id)})
    if task:
        task['_id'] = str(task['_id'])
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@to_do_list.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    updated_task = {
        "task": data.get("task"),
        "description": data.get("description"),
        "priority": data.get("priority"),
        "status": data.get("status"),
        "due_date": data.get("due_date")
    }
    result = db.to_do_list.update_one({"_id": ObjectId(task_id)}, {"$set": updated_task})
    if result.modified_count > 0:
        return jsonify({"message": "Task updated successfully"})
    return jsonify({"error": "Task not found or no changes made"}), 404

@to_do_list.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    result = db.to_do_list.delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count > 0:
        return jsonify({"message": "Task deleted successfully"})
    return jsonify({"error": "Task not found"}), 404
