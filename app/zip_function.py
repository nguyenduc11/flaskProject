def iterate_two_lists(list1, list2):
    """
    Iterates over two lists of the same length simultaneously.

    Args:
        list1 (list): The first list to iterate over.
        list2 (list): The second list to iterate over.

    Returns:
        None
    """
    if len(list1) != len(list2):
        raise ValueError("The two lists must be of the same length.")

    for item1, item2 in zip(list1, list2):
        print(f"Item from list1: {item1}, Item from list2: {item2}")

def test_iterate_two_lists():
    """
    Test cases for the `iterate_two_lists` function.
    """
    # Test case 1: Lists of the same length
    list1 = [1, 2, 3, 4, 5]
    list2 = ['a', 'b', 'c', 'd', 'e']
    iterate_two_lists(list1, list2)
    # Output:
    # Item from list1: 1, Item from list2: a
    # Item from list1: 2, Item from list2: b
    # Item from list1: 3, Item from list2: c
    # Item from list1: 4, Item from list2: d
    # Item from list1: 5, Item from list2: e

    # Test case 2: Lists of different lengths
    list3 = [1, 2, 3]
    list4 = ['a', 'b', 'c', 'd']
    try:
        iterate_two_lists(list3, list4)
    except ValueError as e:
        print(f"Error: {e}")
    # Output:
    # Error: The two lists must be of the same length.

if __name__ == "__main__":
    test_iterate_two_lists()