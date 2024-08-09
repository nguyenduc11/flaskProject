from bokeh.plotting import figure, show, output_file
import numpy as np

def generate_bell_chart_bokeh(scores, title='Bell Curve Distribution of Scores', x_label='Score', y_label='Probability Density'):
    """
    Generate a bell curve chart using Bokeh and return the HTML representation.

    Parameters:
    scores (list): A list of numeric values to be plotted.
    title (str): The title of the chart.
    x_label (str): The label for the x-axis.
    y_label (str): The label for the y-axis.

    Returns:
    str: The HTML representation of the Bokeh plot.
    """
    # Calculate the mean and standard deviation of the scores
    mean = np.mean(scores)
    std_dev = np.std(scores)

    # Create a range of values for the x-axis
    x = np.linspace(min(scores) - 1, max(scores) + 1, 100)

    # Calculate the probability density function (PDF) of the normal distribution
    pdf = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

    # Create the bell curve plot
    p = figure(title=title, x_axis_label=x_label, y_axis_label=y_label, width=500, height=500)
    p.line(x, pdf, color="#007bff", line_width=2)

    # Add dense vertical gridlines
    p.xgrid.grid_line_color = '#f0f0f0'
    p.xgrid.grid_line_width = 1
    p.ygrid.grid_line_color = '#f0f0f0'
    p.ygrid.grid_line_width = 1

    # Save the plot to an HTML file and return the HTML representation
    output_file("bell_curve.html")
    show(p)
    return p.html()


scores=[8,8,9,9,9,10,10,10,10]
generate_bell_chart_bokeh(scores)