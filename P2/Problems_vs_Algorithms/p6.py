"""
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
"""
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints == []:
        return None
        
    max_num = ints[0]
    min_num = ints[0]
    
    for num in ints:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return (min_num, max_num)
    

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
# Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?
l = [i for i in range(0, 10)]  # a list containing 0 -> 9
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(-10, 10)]  # a list containing -10 -> 9
random.shuffle(l)
print("Pass" if ((-10, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 401)]  # a list containing 0 -> 400
random.shuffle(l)
print("Pass" if ((0, 400) == get_min_max(l)) else "Fail")

l = []  # an empty list
print("Pass" if (None == get_min_max(l)) else "Fail")

# Case 5
l = [i for i in range(-23, -1)]  # a list containing -23 - -2
random.shuffle(l)
print("Pass" if ((-23, -2) == get_min_max(l)) else "Fail")