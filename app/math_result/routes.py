from flask import render_template, request, redirect, url_for, session, jsonify
import requests
import datetime
import json
from app import db  # Import the global db object
from bson.json_util import dumps

from app.math_result import math_result


@math_result.route('/quiz03', methods=['GET'])
def get_math_result03():
    result = list(db.math_quiz03.find())

    data = json.loads(dumps(list(result)))

    test_dates = []
    for item in data:
        test_date = convert_mongodb_date(item['timestamp']['$date'])

        test_dates.append(test_date)

    new_data = []
    for item, test_date in zip(data, test_dates):
        item['timestamp'] = test_date
        new_data.append(item)

    # print(f'new_data {new_data}')
    return render_template('math_result.html', data=new_data, )



@math_result.route('/quiz04', methods=['GET'])
def get_math_result04():
    result = list(db.math_quiz04.find())

    data = json.loads(dumps(list(result)))

    test_dates = []
    for item in data:
        test_date = convert_mongodb_date(item['timestamp']['$date'])

        test_dates.append(test_date)

    new_data = []
    for item, test_date in zip(data, test_dates):
        item['timestamp'] = test_date
        new_data.append(item)

    # print(f'new_data {new_data}')
    return render_template('math_result.html', data=new_data, )


def convert_mongodb_date(mongodb_date_str):
    """
    Converts a MongoDB-style datetime string to a 'yyyy-mm-dd' format.

    Args:
        mongodb_date_str (str): A MongoDB-style datetime string in the format 'YYYY-MM-DDThh:mm:ss.sssZ'.

    Returns:
        str: The datetime in 'yyyy-mm-dd' format.
    """
    date_time = datetime.datetime.strptime(mongodb_date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    return date_time.strftime('%Y-%m-%d')
