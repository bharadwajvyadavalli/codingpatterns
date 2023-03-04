'''

'''



#mycode
def dutch_flag_sort(arr):
  # TODO: Write your code here
  left, i = 0, 0
  right = len(arr)-1

  while i <= right:
    if arr[i] == 0:
      arr[i], arr[left] = arr[left], arr[i]
      left += 1
      i += 1
    elif arr[i] == 2:
      arr[i], arr[right] = arr[right], arr[i]
      right -= 1 
    else:
      i += 1

  return 





'''
Time complexity 
The time complexity of the above algorithm will be O(N) as we are iterating the input array only once.

Space complexity #
The algorithm runs in constant space O(1).
'''