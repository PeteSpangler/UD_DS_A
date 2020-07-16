"""
Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, 
that would still be an O(n) solution but it will not count as single traversal.

Here is some boilerplate code and test cases to start with:
"""
def sort_012(nums):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    rightpointer = (len(nums)) - 1 # 2s pointer
    leftpointer = 0 # 0s pointer
    middlepointer = 0 # 1s pointer

    while middlepointer <= rightpointer:
        num = nums[middlepointer]
        if num == 0:
            nums[leftpointer], nums[middlepointer] = nums[middlepointer], nums[leftpointer]
            leftpointer += 1
            middlepointer += 1
        if num == 2:
            nums[rightpointer], nums [middlepointer] = nums[middlepointer], nums[rightpointer]
            nums[rightpointer] -= 1
        else:
            middlepointer += 1 

def test_function(nums):
    sorted_array = sort_012(nums)
    print(sorted_array)
    if sorted_array == sorted(nums):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])