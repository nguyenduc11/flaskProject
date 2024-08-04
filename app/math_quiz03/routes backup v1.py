from app.math_quiz03 import math_quiz03
from flask import render_template, request, redirect, url_for
import random
from app.math_quiz03.quiz03_app import TestApp
from app.math_quiz03.generate_question import generate_questions
from app.math_quiz03.get_answers import get_answers
from app.math_quiz03.get_correct_answers import get_correct_answers
from app.math_quiz03.check_user_score import check_user_score

app_logic = TestApp()
# app_logic.start_new_round()
list1 = app_logic.list1
list2 = app_logic.list2
print('routes')
print(app_logic.list1)
print(app_logic.list2)

@math_quiz03.route('/quiz03', methods=['GET', 'POST'])
def math_quiz03():
    if request.method == "GET":
        print('get')
        questions = generate_questions(list1, list2)
        print(list1)
        print(list2)
        print(f"questions {questions}")
        # app_logic.start_new_round()
        return render_template('quiz03.html', questions=questions)
    elif request.method == 'POST':
        if 'submit' in request.form:
            print('submit')
            original_questions = generate_questions(list1, list2)
            # get user answers
            user_guess = get_answers(request.form)
            print(user_guess)

            # score = app_logic.check_score(user_guess)
            score = check_user_score(list1, list2,user_guess)
            print(f'score {score}')
            correct_answers = get_correct_answers(list1, list2)
            app_logic.start_new_round()
        return render_template('result.html',
                               original_questions=original_questions,
                               user_guess=user_guess,
                               correct_answers=correct_answers,
                               score=score)
    elif 'restart' in request.form:
        app_logic.start_new_round()
        return redirect(url_for('math_quiz03.math_quiz03'))
