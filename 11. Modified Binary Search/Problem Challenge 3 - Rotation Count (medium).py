'''

'''

#mycode


    

def main():
  print(count_rotations([10, 15, 1, 3, 8]))
  print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
  print(count_rotations([1, 3, 8, 10]))


main()



#answer
def count_rotations(arr):
  start, end = 0, len(arr) - 1
  while start < end:
    mid = start + (end - start) // 2

    # if mid is greater than the next element
    if mid < end and arr[mid] > arr[mid + 1]:
      return mid + 1

    # if mid is smaller than the previous element
    if mid > start and arr[mid - 1] > arr[mid]:
      return mid

    if arr[start] < arr[mid]:  # left side is sorted, so the pivot is on right side
      start = mid + 1
    else:  # right side is sorted, so the pivot is on the left side
      end = mid - 1

  return 0  # the array has not been rotated


def main():
  print(count_rotations([10, 15, 1, 3, 8]))
  print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
  print(count_rotations([1, 3, 8, 10]))


main()



'''
Time complexity
This algorithm will run in O(logN) most of the times, 
but since we only skip two numbers in case of duplicates instead of the half of the numbers, 
therefore the worst case time complexity will become O(N).

Space complexity 
The algorithm runs in constant space O(1).
'''
