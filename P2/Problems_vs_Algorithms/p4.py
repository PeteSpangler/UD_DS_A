"""
Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, 
that would still be an O(n) solution but it will not count as single traversal.

Here is some boilerplate code and test cases to start with:
"""
def sort_012(nums):
    next_pos_0 = 0 #pointer for 0s
    next_pos_2 = len(nums) - 1 #pointer for 2s

    front_index = 0 #iterator

    while front_index <= next_pos_2:
        if nums[front_index] == 0:
            nums[front_index] = nums[next_pos_0]
            nums[next_pos_0] = 0
            next_pos_0 += 1
            front_index += 1
        elif nums[front_index] == 2:           
            nums[front_index] = nums[next_pos_2] 
            nums[next_pos_2] = 2
            next_pos_2 -= 1
        else:
            front_index += 1
    return nums

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
test_function([0,1,2])
test_function([])
test_function([0,2])
test_function([2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,2,2,2,2,1,2,1,2,1,2,1,2,0,0,1,2,0,2,2,0,0,0,0])