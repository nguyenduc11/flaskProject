from flask import render_template, request, redirect, url_for, session, jsonify
import requests
import datetime
import json
from app import db  # Import the global db object
from bson.json_util import dumps
import plotly.graph_objects as go
from app.math_result import math_result
import numpy as np


@math_result.route('/quiz03', methods=['GET'])
def get_math_result03():
    result = list(db.math_quiz03.find())

    data = json.loads(dumps(list(result)))
    scores = [item['score'] for item in data if item['score']]
    # print(f'scores {scores}')
    plot_html = generate_chart(scores)
    bell_chart_html = generate_bell_chart(scores)
    test_dates = []
    for item in data:
        test_date = convert_mongodb_date(item['timestamp']['$date'])

        test_dates.append(test_date)

    new_data = []
    for item, test_date in zip(data, test_dates):
        item['timestamp'] = test_date
        new_data.append(item)

    # print(f'new_data {new_data}')
    return render_template('math_result.html', data=new_data, plot_html=plot_html, bell_chart_html=bell_chart_html)


@math_result.route('/quiz04', methods=['GET'])
def get_math_result04():
    result = list(db.math_quiz04.find())

    data = json.loads(dumps(list(result)))
    scores = [item['score'] for item in data if item['score']]
    # print(f'scores {scores}')
    plot_html = generate_chart(scores)
    bell_chart_html = generate_bell_chart(scores)
    test_dates = []
    for item in data:
        test_date = convert_mongodb_date(item['timestamp']['$date'])

        test_dates.append(test_date)

    new_data = []
    for item, test_date in zip(data, test_dates):
        item['timestamp'] = test_date
        new_data.append(item)

    # print(f'new_data {new_data}')
    return render_template('math_result.html', data=new_data, plot_html=plot_html, bell_chart_html=bell_chart_html)


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


def generate_chart(scores, title='Tổng kết', x_label='Điểm', y_label='Số lượng', bar_gap=0.1):
    """
    Generate a histogram chart using Plotly and return the HTML representation.

    Parameters:
    scores (list): A list of numeric values to be plotted.
    title (str): The title of the chart.
    x_label (str): The label for the x-axis.
    y_label (str): The label for the y-axis.
    bar_gap (float): The gap between the bars in the histogram (0.0 to 1.0).

    Returns:
    str: The HTML representation of the Plotly chart.
    """
    # Create the histogram
    fig = go.Figure(data=[go.Histogram(x=scores)])

    # Customize the layout
    fig.update_layout(
        title=dict(text=title, x=0.5),  # Center the title
        xaxis_title=x_label,
        yaxis_title=y_label,
        bargap=bar_gap,
        plot_bgcolor='white',  # Set the plot background color
        paper_bgcolor='white',  # Set the paper background color
        font=dict(color='#333333'),  # Set the font color
        margin=dict(t=50, b=50, l=50, r=50), # Adjust the margins
        width=500,
        height=500
    )

    # Add gridlines
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#f0f0f0')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#f0f0f0', nticks=20)
    # Add the exact count on top of each bar
    fig.update_traces(texttemplate='%{y:.0f}')
    fig.update_layout(bargap=0.1, bargroupgap=0.1)
    # Return the plot as HTML
    return fig.to_html()


def generate_bell_chart(scores, title='Bell Curve Distribution of Scores', x_label='Score',
                        y_label='Probability Density'):
    """
    Generate a bell curve chart using Plotly and return the HTML representation.

    Parameters:
    scores (list): A list of numeric values to be plotted.
    title (str): The title of the chart.
    x_label (str): The label for the x-axis.
    y_label (str): The label for the y-axis.

    Returns:
    str: The HTML representation of the Plotly chart.
    """
    # Calculate the mean and standard deviation of the scores
    mean = np.mean(scores)
    std_dev = np.std(scores)

    # Create a range of values for the x-axis
    x = np.linspace(min(scores) - 1, max(scores) + 1, 100)

    # Calculate the probability density function (PDF) of the normal distribution
    pdf = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

    # Create the bell curve plot
    fig = go.Figure(data=[go.Scatter(x=x, y=pdf, mode='lines', line=dict(color='#007bff', width=2))])

    # Customize the layout
    fig.update_layout(
        title=dict(text=title, x=0.5, font=dict(size=20)),
        xaxis_title=x_label,
        yaxis_title=y_label,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='#333333'),
        margin=dict(t=50, b=50, l=50, r=50),
        width=500,
        height=500
    )

    # Add dense vertical gridlines
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#f0f0f0', nticks=10)
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#f0f0f0')

    # Return the plot as HTML
    return fig.to_html()



