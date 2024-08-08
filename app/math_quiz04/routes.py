from flask import render_template, request, redirect, url_for, session
import requests
import json
from datetime import datetime

from app.math_quiz04 import math_quiz04
from app.math_quiz04.quiz04_app import Quiz04App
from app.math_quiz04.generate_question import generate_questions
from app.math_quiz04.get_answers import get_answers
from app.math_quiz04.get_correct_answers import get_correct_answers
from app.math_quiz04.check_user_score import check_user_score
from app import db

app_logic = Quiz04App()


@math_quiz04.route('/quiz04', methods=['GET', 'POST'])
def math_quiz04_route():
    if request.method == "GET":
        return handle_get_request()
    elif request.method == 'POST':
        if 'submit' in request.form:
            return handle_submit_request()
        elif 'restart' in request.form:
            return handle_restart_request()


def handle_get_request():
    app_logic.start_new_round()
    session['list1'], session['list2'] = app_logic.list1, app_logic.list2
    questions = generate_questions(session['list1'], session['list2'])
    return render_template('quiz04.html', questions=questions)


def handle_submit_request():
    list1, list2 = session.get('list1'), session.get('list2')
    original_questions = generate_questions(list1, list2)
    user_guess = get_answers(request.form)
    score = check_user_score(list1, list2, user_guess)
    correct_answers = get_correct_answers(list1, list2)
    user_marks = check_user_marks(list1, list2, user_guess)

    quiz_result = {
        "original_questions": original_questions,
        "user_guess": user_guess,
        "correct_answers": correct_answers,
        "user_marks": user_marks,
        "score": score,
        "timestamp": datetime.now(),
        "location_data": get_location_data(request.remote_addr),
        "user_agent": request.headers.get('User-Agent')
    }
    db.math_quiz04.insert_one(quiz_result)

    return render_template('result04.html',
                           original_questions=original_questions,
                           user_guess=user_guess,
                           user_marks=user_marks,
                           correct_answers=correct_answers,
                           score=score)


def handle_restart_request():
    app_logic.start_new_round()
    session['list1'], session['list2'] = app_logic.list1, app_logic.list2
    return redirect(url_for('math_quiz04.math_quiz04_route'))


def get_location_data(ip_address):
    url = f"http://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    return json.loads(response.text)


def check_user_marks(list1, list2, user_answers):
    user_marks = []
    for i in range(len(list1)):
        if user_answers[i] == list1[i] + list2[i]:
            user_marks.append(True)
        else:
            user_marks.append(False)
    return user_marks
