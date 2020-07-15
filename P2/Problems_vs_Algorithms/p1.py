"""
Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the floor_sqrtwer would be 4.

If the given number is 27, the floor_sqrtwer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

Here is some boilerplate code and test cases to start with:
"""
def sqrt(x):
  
   if (x == 0 or x ==1):
      
      return x
   
   low = 1
   high = x
   while (low <= high):
      mid_num = (low + high) // 2
      if (mid_num*mid_num == x):
         return mid_num
      if (mid_num * mid_num < x):
         low = mid_num + 1
         floor_sqrt = mid_num
      else:
         high = mid_num - 1
   return floor_sqrt

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")