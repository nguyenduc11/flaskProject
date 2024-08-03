import random
def generate_questions():
    """
    Generates a list of 10 math questions.

    Returns:
        list: A list of 10 math questions.
    """
    questions = []
    results = []
    for i in range(1, 11):
        num1 = random.randint(10, 20)
        num2 = random.randint(1, 9)
        question = f"{num1} - {num2} = ?"
        questions.append(question)
        result = num1 - num2
        results.append(result)
    return {"questions": questions, "results": results}

input = generate_questions()
print(input['questions'])
print(input['results'])


def get_person_info():
    person_info = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }
    return person_info

name, age, city = get_person_info().values()
print(f"Name: {name}, Age: {age}, City: {city}")

class AdditionApp:
    def __init__(self, input_num1, input_num2):
        self.number1 = input_num1
        self.number2 = input_num2

    def sum(self):
        return self.number1 + self.number2

test1 = AdditionApp(5, 6)
print(test1.number1)
print(test1.number2)

test1_sum = test1.sum()
print(test1_sum)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def report(self):
        return f"The radius of this circle is {self.radius}"

    def area(self):
        return 3.14 * (self.radius ** 2)

    def circumference(self):
        return 2 * 3.14 * self.radius


circleA = Circle(5)
print(circleA.report())
print(circleA.area())
print(circleA.circumference())



