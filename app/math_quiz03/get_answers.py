def get_answers(request_form):
    """
    Extracts the answer values from an ImmutableMultiDict object and converts them to integers.

    Args:
        request_form (ImmutableMultiDict): The form data from the Flask request.

    Returns:
        list: A list of the answer values as integers.
    """
    answers = []
    for key in request_form:
        if key.startswith('answer'):
            answer_value = request_form[key]
            if answer_value.isdigit():
                answers.append(int(answer_value))
    return answers


if __name__ == '__main__':
    answers = get_answers(request.form)
    print(answers)