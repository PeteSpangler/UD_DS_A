This problem statement indicates the array must be sorted before the calculations to find the two max sums are done. The expected time complexity of O(n log n) indicates a mergesort or heapsort approach. I chose a mergesort approach, utilizing the mergesort code from the sorting algorithm section in this unit, only flipping the less than operator in line 64 so the array is sorted in descending order. With a sorted array, the two max sums are the odd/even indices, as shown in lines 31 and 32. The time complexity of this is roughly O(n log n) and the space complexity is O(n) due to mergesort needing additional arrays to do its magic. 