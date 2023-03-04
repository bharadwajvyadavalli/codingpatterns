'''

'''





def main():
  print(circular_array_loop_exists([1, 2, -1, 2, 2]))
  print(circular_array_loop_exists([2, 2, -1, 2]))
  print(circular_array_loop_exists([2, 1, -1, -2]))


main()



'''
Time Complexity 
The above algorithm will have a time complexity of O(N^2) where ‘N’ is the number of elements in the array. 
This complexity is due to the fact that we are iterating all elements of the array and trying to find a cycle for each element.

Space Complexity 
The algorithm runs in constant space O(1).

An Alternate Approach 
In our algorithm, we don’t keep a record of all the numbers that have been evaluated for cycles. 
We know that all such numbers will not produce a cycle for any other instance as well. 
If we can remember all the numbers that have been visited, our algorithm will improve to O(N) as, then, each number will be evaluated for cycles only once. 
We can keep track of this by creating a separate array however the space complexity of our algorithm will increase to O(N).
'''