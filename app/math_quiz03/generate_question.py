import random


def generate_questions(list1, list2):
    """
    Generates a list of 10 math questions.

    Returns:
        list: A list of 10 math questions.
    """
    questions = []
    for num1, num2 in zip(list1, list2):
        problem = str(num1) + '-' + str(num2) + '=' + '?'
        questions.append(problem)
    return questions

if __name__ == '__main__':
    questions = generate_questions()
    print(questions)
