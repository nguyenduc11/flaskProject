from flask import render_template, request, redirect, url_for, session,jsonify
import requests
import datetime
import json
from app import db  # Import the global db object
from bson.json_util import dumps

from app.math_result import math_result
@math_result.route('/quiz03', methods=['GET'])
def get_math_result03():
    result = list(db.math_quiz03.find())
    # print(f'result {result}')
    # Convert the cursor object to a list of dictionaries
    data = json.loads(dumps(list(result)))

    # print(f'data {data}')
    # print(type(data))

    test_dates = []
    for item in data:
        test_date = convert_mongodb_date(item['timestamp']['$date'])

        test_dates.append(test_date)
    # print(test_dates)
    # data.append(test_dates)
    # print(data)/
    return render_template('math_result.html', data=data, test_dates=test_dates)

@math_result.route('/quiz04', methods=['GET'])
def get_math_result04():
    result = list(db.math_quiz04.find())
    # print(f'result {result}')
    # Convert the cursor object to a list of dictionaries
    data = json.loads(dumps(list(result)))

    # print(f'data {data}')
    # print(type(data))

    test_dates = []
    for item in data:
        test_date = convert_mongodb_date(item['timestamp']['$date'])

        test_dates.append(test_date)
    # print(test_dates)
    # data.append(test_dates)
    # print(data)/
    return render_template('math_result.html', data=data, test_dates=test_dates)


def convert_mongodb_date(mongo_date_str):
    try:
        # Print debugging information
        print(f"Python version: {datetime.__version__}")
        print(f"Datetime module: {datetime}")
        print(f"Fromisoformat method: {getattr(datetime.datetime, 'fromisoformat', 'Not found')}")

        # Parse the MongoDB date string
        mongo_date = datetime.datetime.fromisoformat(mongo_date_str.replace('Z', '+00:00'))

        # Convert to dd/mm/yy format
        formatted_date = mongo_date.strftime("%d/%m/%y")

        return formatted_date
    except AttributeError as e:
        print(f"AttributeError occurred: {e}")
        print("Falling back to alternative method...")

        # Alternative method using strptime
        mongo_date = datetime.datetime.strptime(mongo_date_str.split('.')[0], "%Y-%m-%dT%H:%M:%S")
        return mongo_date.strftime("%d/%m/%y")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
