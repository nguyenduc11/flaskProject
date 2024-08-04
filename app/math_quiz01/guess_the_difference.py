import random

from plotly import graph_objects as go, io as pio


class GuessDifferenceApp:
    def __init__(self):
        self.correct_sum = None
        self.number1 = None
        self.number2 = None
        self.start_new_round()

    def start_new_round(self):
        while True:
            self.number1 = random.randint(11, 20)
            self.number2 = random.randint(1, 9)
            if self.number1 - self.number2 < 10:
                break
        self.correct_sum = None

    def check_sum(self, user_guess):
        correct_sum = self.number1 - self.number2
        if user_guess == correct_sum:
            self.correct_sum = correct_sum
            return True, correct_sum
        else:
            return False, correct_sum

    def generate_chart(self):
        numbers = [self.number1, self.number2]
        labels = ['Số bị trừ', 'Số trừ']
        colors = ['#3498db', '#2ecc71']  # Blue, Green

        if self.correct_sum is not None:
            numbers.append(self.correct_sum)
            labels.append('Sum')
            colors.append('#e74c3c')  # Red
            numbers.extend([10, self.correct_sum - 10])
            labels.extend(['Ten 10', 'Difference'])
            colors.extend(['#f39c12', '#9b59b6'])  # Orange, Purple

        bars = []
        for i, (num, label, color) in enumerate(zip(numbers, labels, colors)):
            for j in range(num):
                bars.append(go.Bar(
                    y=[label],
                    x=[1],
                    base=[j],
                    marker=dict(color=color, line=dict(color='black', width=1)),
                    name=label,
                    orientation='h',
                    width=0.5
                ))

        layout = go.Layout(
            title='Numbers to Add' if self.correct_sum is None else 'Numbers and Sum',
            xaxis=dict(title='Values', dtick=1, gridcolor='black', zerolinecolor='black', zerolinewidth=2),
            yaxis=dict(title='Elements', dtick=1, gridcolor='black'),
            barmode='stack',
            plot_bgcolor='#f8f9fa',
            paper_bgcolor='#f8f9fa',
            showlegend=False,
            shapes=[
                # Red thick line at y=10
                dict(
                    type="line",
                    x0=10, x1=10,
                    y0=0, y1=len(labels),
                    line=dict(
                        color="red",
                        width=4
                    )
                )
            ]
        )

        fig = go.Figure(data=bars, layout=layout)
        plot_html = pio.to_html(fig, full_html=False)
        return plot_html
