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

