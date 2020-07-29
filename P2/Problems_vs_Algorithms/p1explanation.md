Given the expected time complexity of O(log n), a binary search algorithm approach was ideal. Binary search in this problem was implemented by checking if the square of the middle value was equal to the target value. If the squared middle value is to larger, decrement the high value by 1. If the square middle value is too low, increase the low value by 1. (Additionally, set this variable as the floor_sqrt to be returned, according to the problem statement the closest whole number to the square root is the expected output.) Loop through this algorithm until the target value is found. Thus, the time complexity is O(log n) because it is binary search and the time complexity is O(1) because there is not additional space needed for the calculations to find the output. 