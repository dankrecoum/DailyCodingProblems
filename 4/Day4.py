"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, 
find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def lowest_positive_missing(array):
   """
    The function that returns the lowest positive integer missing in the given array, all in linear time and constant space
    Supposing the array length >= 2 

    Args:
        array (list): The array to be processed.

    Returns:
        lowest (int): The lowest positive integer missing in the given array
   """
   array.sort() #time complexity in O(nlogn) on average and in worst case

   if (array[-1] <= 0): #only negative numbers or 0
       return 1

   for i in range(len(array)-1): #last element must not be checked to avoid out of range indexing
       if (array[i] >= 0 and (array[i+1] != (array[i] + 1))):
           return array[i] + 1
    
   return array[-1] + 1 #when all the numbers are spaced by 1 from the beginning to the end


if __name__ == '__main__':
    assert 1 == lowest_positive_missing([-1, -10, 0, -43]) #all negative numbers
    assert 2 == lowest_positive_missing([3, 4, -1, 1]) #problem's case
    assert 4 == lowest_positive_missing([2, 5, -65, 34, 0, 3, 1]) #random case with negaive and positive numbers
    assert 0 != lowest_positive_missing([-3, 5, 9, -100000]) #random case that prove that 0 is not considered as in the example
    assert 3 == lowest_positive_missing([-2, -1, 0, 1, 2]) #all numbers are spaced by 1
