# P1:
Given the expected time complexity of O(log n), a binary search algorithm approach was ideal. Binary search in this problem was implemented by checking if the square of the middle value was equal to the target value. If the squared middle value is to larger, decrement the high value by 1. If the square middle value is too low, increase the low value by 1. (Additionally, set this variable as the floor_sqrt to be returned, according to the problem statement the closest whole number to the square root is the expected output.) Loop through this algorithm until the target value is found. 

Thus, the time complexity is O(log n) because it is binary search and the space complexity is 
O(1) because there is not additional space needed for the calculations to find the output. 

# P2:
This has a similar solution to P1: binary search is implemented on the given array to identify the target value. The variation comes in the rotated array parameter, which is checked in the binary search algorithm’s implementation in lines 20-29. This is a variation of the usual increment/decrement low/high values in a vanilla binary search algorithm. This is to see if the pivot point from which the array has been rotated is on the right or left side of the array, to then set up the algorithm to work on the correct side of the array. Time Complexity is O(log n) because of the use of binary search and time complexity is O(1) because the algorithm does not use extra space to run. 

# P3:
This problem statement indicates the array must be sorted before the calculations to find the two max sums are done. The expected time complexity of O(n log n) indicates a mergesort or heapsort approach. I chose a mergesort approach, utilizing the mergesort code from the sorting algorithm section in this unit, only flipping the less than operator in line 64 so the array is sorted in descending order. With a sorted array, the two max sums are the odd/even indices, as shown in lines 31 and 32. The time complexity of this is roughly O(n log n) and the space complexity is O(n) due to mergesort needing additional arrays to do its magic. 

# P4:
To sort the given array of 0,1,2 in one pass, three pointers are used. A pointer as the iterator through the whole array, a pointer for the 0s, and a pointer for the 2s, and by swapping values of 0s and 2s as necessary, the 1s end up in the middle where they should be. This is a one pass solution (linear time complexity O(n)) with O(1) space complexity.

# P5:
This problem was implemented with a Trie, as in the problem statement is titled "Autocomplete with Tries". Using the Trie structure as shown in the Basic algorithm section of this unit, space and time complexity are good for the proposed purpose. The time complexity for a Trie depends on the # of words in the Trie and length of the word that is being inserted or searched for, so O(word length * number of total words in trie). Space complexity is O(total words - shared letters between those words) so worst case it could be O(n) space. 

# P6:
This is done in a single traversal and in O(n) time using linear search. There is no need to sort the list to find the minimum and maximum integer, a simple linear search comparing the values as the list is iterated fufills the stated problem statement. Time complexity is O(n) and space complexity is O(1).

# P7:
Similar to the Trie used in P5, the worst case  time complexity here are linked to the number of nodes/number of path_parts to insert/find. So that would be O(# of nodes * # of path_parts). Space complexity is worst case O(n) unless nodes share similar paths, which would reduce the space complexity marginially. 