"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def add_up_to(array, k):
    """
    Function that return whether two numbers of an array add up to a given int k

    Args :
        array (list): The array to be processed
        k (int): The integer that that can be the sum of two numbers of the array

    Returns :
        add_up (bool): The boolean value that is True when two numbers of the array add up to k
    """
    add_up = False
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] + array[j] == k:
                return not add_up
    return add_up


def add_up_to_bonus(array, k):
    """
    Function that return whether two numbers of an array add up to a given int k
    Same as the previous one but does the process in one pass

    Args :
        array (list): The array to be processed
        k (int): The integer that that can be the sum of two numbers of the array

    Returns :
        add_up (bool): The boolean value that is True when two numbers of the array add up to k
    """
    add_up = False
    for i in range(len(array)):
        if (k - array[i]) in array[:(i+1)]:
            return not add_up
    return add_up


if __name__ == '__main__':
    print(add_up_to([10, 15, 3, 7], 25))
    print(add_up_to_bonus([10, 15, 3, 7], 25))
