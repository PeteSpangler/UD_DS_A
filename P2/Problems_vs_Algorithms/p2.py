def rotated_array_search(nums, x):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == x:
            return mid
    # This section is to check if the pivot is on the right or left side of the array
        if not (nums[low] <= nums[mid]) == (nums[low] <=x):
            if nums[low] > x:
                low = mid + 1
            else:
                high = mid - 1
            continue
        if nums[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def linear_search(nums, x):
    for index, element in enumerate(nums):
        if element == x:
            return index
    return -1

def test_function(test_case):
    nums = test_case[0]
    x = test_case[1]
    if linear_search(nums, x) == rotated_array_search(nums, x):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6, 7, 8], 11])
test_function([[], 1])

