from app.math_quiz02 import math_quiz02
from flask import render_template, request
from app.math_quiz02.guess_the_sum import GuessSumApp

app_logic = GuessSumApp()

@math_quiz02.route('/quiz02', methods=["GET", "POST"])
def guess_sum():
    if request.method == "POST":
        if 'new_round' in request.form:
            app_logic.start_new_round()
            plot_html = app_logic.generate_chart()
            return render_template("math_quiz02.html", number1=app_logic.number1, number2=app_logic.number2,
                                   plot_html=plot_html)

        user_guess = request.form.get("sum")
        if user_guess:
            try:
                user_guess = int(user_guess)
                correct, correct_sum = app_logic.check_sum(user_guess)
                if correct:
                    plot_html = app_logic.generate_chart()
                    message = f"OK. Tổng là {correct_sum}."
                    return render_template("math_quiz02.html", number1=app_logic.number1, number2=app_logic.number2,
                                           message=message, plot_html=plot_html, show_new_round=True)
                else:  # wrong answer
                    message = f"Sai. Kết quả đúng là {correct_sum}."
                    plot_html = app_logic.generate_chart()
                    return render_template("math_quiz02.html", number1=app_logic.number1, number2=app_logic.number2,
                                           message=message, plot_html=plot_html)
            except ValueError:
                message = "Invalid input. Please enter a valid number."
                plot_html = app_logic.generate_chart()
                return render_template("math_quiz02.html", number1=app_logic.number1, number2=app_logic.number2,
                                       message=message, plot_html=plot_html)

    app_logic.start_new_round()
    plot_html = app_logic.generate_chart()
    return render_template("math_quiz02.html", number1=app_logic.number1, number2=app_logic.number2,
                           plot_html=plot_html)
