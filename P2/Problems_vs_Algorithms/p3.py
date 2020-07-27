"""
Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. 
You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers 
cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the 
expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as 
these when there are more than one possible answers, return any one.

Here is some boilerplate code and test cases to start with:
"""
def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 1:
        return [input_list[0], 0]
#edge / sanity check above and below this line
    if len(input_list) == 0:
        return []

    merged_list = mergesort(input_list) 
    left_arr = merged_list[0::2] 
    right_arr = merged_list[1::2] 
#iterating over odd/even merged_list(s) into the two max sums by taking every other number 
    left_arr_string = '' 
    for num in left_arr: 
        left_arr_string += str(num) 

    right_arr_string = '' 
    for num in right_arr: 
        right_arr_string += str(num) 

    return [int(left_arr_string), int(right_arr_string)]
    
def mergesort(input_list):
#this implementation comes from the mergesort chapter in the sorted algorithms chapter
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2
    left = input_list[:mid]
    right = input_list[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1
    merged += left[left_index:]
    merged += right[right_index:]
    return merged


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

#Edge cases 
test_function([[], []]) 
test_function([[1], [1, 0]]) 
#Normal cases 
test_function([[1, 2, 3, 4, 5], [542, 31]]) 
test_function([[4, 6, 2, 5, 9, 8], [964, 852]]) 
test_function([[2, 3], [3, 2]]) 
test_function([[5, 4, 2], [54, 2]]) 
