from flask import render_template, request, redirect, url_for, session
import requests
import json

from app.math_quiz03 import math_quiz03
from app.math_quiz03.quiz03_app import TestApp
from app.math_quiz03.generate_question import generate_questions
from app.math_quiz03.get_answers import get_answers
from app.math_quiz03.get_correct_answers import get_correct_answers
from app.math_quiz03.check_user_score import check_user_score
from app import db  # Import the global db object
from datetime import datetime

app_logic = TestApp()


@math_quiz03.route('/quiz03', methods=['GET', 'POST'])
def math_quiz03():
    if request.method == "GET":
        # Start a new round and store list1 and list2 in session
        app_logic.start_new_round()
        session['list1'] = app_logic.list1
        session['list2'] = app_logic.list2

        questions = generate_questions(session['list1'], session['list2'])
        return render_template('quiz03.html', questions=questions)

    elif request.method == 'POST':
        if 'submit' in request.form:
            # Retrieve list1 and list2 from session
            list1 = session.get('list1')
            list2 = session.get('list2')

            original_questions = generate_questions(list1, list2)
            # Get user answers
            user_guess = get_answers(request.form)

            score = check_user_score(list1, list2, user_guess)
            correct_answers = get_correct_answers(list1, list2)
            # Get user information
            # Get the user's IP address
            user_ip = request.remote_addr

            # Get the user's location based on their IP address
            location_data = get_location_data(user_ip)

            # Get the user's browser information
            user_agent = request.headers.get('User-Agent')
            # Get timestamp
            timestamp = datetime.now()
            # Add data to database
            quiz_result = {
                "original_questions": original_questions,
                "user_guess": user_guess,
                "correct_answers": correct_answers,
                "score": score,
                "timestamp": timestamp,
                "location_data": location_data,
                "user_agent": user_agent
            }
            db.math_quiz03.insert_one(quiz_result)

            return render_template('result.html',
                                   original_questions=original_questions,
                                   user_guess=user_guess,
                                   correct_answers=correct_answers,
                                   score=score)

    elif 'restart' in request.form:
        app_logic.start_new_round()
        session['list1'] = app_logic.list1
        session['list2'] = app_logic.list2
        return redirect(url_for('math_quiz03.math_quiz03'))



def get_location_data(ip_address):
    """
    Function to get the location data based on the IP address.
    """
    url = f"http://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    location_data = json.loads(response.text)
    return location_data

