"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of
all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [
3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def array_product(array):
    """
    The function that returns the product of all the numbers of an array

    Args:
        array: The array to be processed.

    Returns:
        product (int): The product of all the array's numbers
    """
    product = 1
    for i in array:
        product *= i
    return product


def new_array(array):
    """
    The function that takes an array and returns a new array such that each element at index i of the new array is
    the product of all the numbers in the original array except the one at i.

    Args:
        array: The array to be processed.

    Returns:
        new_array (list): The new array such as asked in the problem
    """
    product = array_product(array)
    return [int(product / item) for item in array]


def new_array_without_division(array):
    """
    The function that takes an array and returns a new array such that each element at index i of the new array is
    the product of all the numbers in the original array except the one at i.
    Same as the previous one but without division.

    Args:
        array: The array to be processed.

    Returns:
        new_array (list): The new array with such as asked in the problem
    """
    new_array = []
    for item in array:
        array_without_item = list(array)
        array_without_item.remove(item)
        new_array.append(array_product(array_without_item))
    return new_array


if __name__ == '__main__':
    test_array = [1, 2, 3, 4, 5]
    expected_array = [120, 60, 40, 30, 24]
    assert new_array(test_array) == expected_array
    assert new_array_without_division(test_array) == expected_array
