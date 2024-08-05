from flask import render_template, request, redirect, url_for, session,jsonify
import requests
import json
from app import db  # Import the global db object
from bson.json_util import dumps

from app.math_result import math_result
@math_result.route('/quiz03', methods=['GET'])
def get_math_result():
    result = list(db.math_quiz03.find())
    # print(f'result {result}')
    # Convert the cursor object to a list of dictionaries
    data = json.loads(dumps(list(result)))
    return jsonify(data)
    # return render_template('math_result.html', result=result)
