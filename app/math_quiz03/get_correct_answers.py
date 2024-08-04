def get_correct_answers(list1, list2):
    """
    Sums the corresponding elements from two input lists and returns a new list.

    Args:
        list1 (list): A list of integers.
        list2 (list): Another list of integers.

    Returns:
        list: A new list where each element is the sum of the corresponding elements from the input lists.
    """
    if len(list1) != len(list2):
        raise ValueError("Input lists must have the same length.")

    result = []
    for i in range(len(list1)):
        result.append(list1[i] - list2[i])

    return result


if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [5, 6, 7, 8]
    print(get_correct_answers(list1, list2))
