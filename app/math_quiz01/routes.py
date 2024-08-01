from app.math_quiz01 import math_quiz01
from flask import render_template, request, redirect, url_for
import random


@math_quiz01.route('/quiz01', methods=['GET', 'POST'])
def math_quiz01():
    if request.method == 'POST':
        if 'submit' in request.form:
            user_answers = []
            for i in range(1, 11):
                answer_key = f'answer{i}'
                if answer_key in request.form:
                    user_answers.append(int(request.form[answer_key]))
                else:
                    user_answers.append(0)
            score = calculate_score(user_answers)
            correct_answers = get_correct_answers(user_answers)
            return render_template('quiz01.html', score=score, correct_answers=correct_answers)
        elif 'restart' in request.form:
            return redirect(url_for('math_quiz01.math_quiz01'))
    else:
        questions = generate_questions()
        return render_template('quiz01.html', questions=questions)


def calculate_score(user_answers):
    """
        Calculates the user's score based on their answers.

        Args:
            user_answers (list): A list of the user's answers for each question.

        Returns:
            int: The user's score.
        """
    correct_answers = get_correct_answers(user_answers)
    return len(correct_answers)

def get_correct_answers(user_answers):
    """
    Generates the correct answers for each question.

    Args:
        user_answers (list): A list of the user's answers for each question.

    Returns:
        list: A list of the correct answers for each question.
    """
    correct_answers = []
    for i in range(1, 11):
        num1 = random.randint(10, 20)
        num2 = random.randint(1, 9)
        correct_answer = num1 - num2
        correct_answers.append(correct_answer)
    return correct_answers


def generate_questions():
    """
    Generates a list of 10 math questions.

    Returns:
        list: A list of 10 math questions.
    """
    questions = []
    for i in range(1, 11):
        num1 = random.randint(10, 20)
        num2 = random.randint(1, 9)
        question = f"{num1} - {num2} = ?"
        questions.append(question)
    return questions


