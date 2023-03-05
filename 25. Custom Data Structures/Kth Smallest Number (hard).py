


def main():

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()



#1. Brute-force
import math


def find_Kth_smallest_number(nums, k):
  # to handle duplicates, we will keep track of previous smallest number and its index
  previousSmallestNum, previousSmallestIndex = -math.inf, -1
  currentSmallestNum, currentSmallestIndex = math.inf, -1
  for i in range(k):
    for j in range(len(nums)):
      if nums[j] > previousSmallestNum and nums[j] < currentSmallestNum:
        # found the next smallest number
        currentSmallestNum = nums[j]
        currentSmallestIndex = j
      elif nums[j] == previousSmallestNum and j > previousSmallestIndex:
        # found a number which is equal to the previous smallest number; since numbers can repeat,
        # we will consider 'nums[j]' only if it has a different index than previous smallest
        currentSmallestNum = nums[j]
        currentSmallestIndex = j
        break  # break here as we have found our definitive next smallest number

    # current smallest number becomes previous smallest number for the next iteration
    previousSmallestNum = currentSmallestNum
    previousSmallestIndex = currentSmallestIndex
    currentSmallestNum = math.inf

  return previousSmallestNum


def main():

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()



'''
Time & Space Complexity 
The time complexity of the above algorithm will be O(N*K). The algorithm runs in constant space O(1).
'''



#2. Brute-force using Sorting
def find_Kth_smallest_number(nums, k):
  return sorted(nums)[k-1]


def main():

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()



'''
Time & Space Complexity 
Sorting will take O(NlogN)O(NlogN) and if we are not using an in-place sorting algorithm, we will need O(N)O(N) space.
'''


#3. Using Max-Heap
from heapq import *


def find_Kth_smallest_number(nums, k):
  maxHeap = []
  # put first k numbers in the max heap
  for i in range(k):
    heappush(maxHeap, -nums[i])

  # go through the remaining numbers of the array, if the number from the array is smaller than the
  # top(biggest) number of the heap, remove the top number from heap and add the number from array
  for i in range(k, len(nums)):
    if -nums[i] > maxHeap[0]:
      heappop(maxHeap)
      heappush(maxHeap, -nums[i])

  # the root of the heap has the Kth smallest number
  return -maxHeap[0]


def main():

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()



'''
Time & Space Complexity 
The time complexity of the above algorithm is O(K*logK + (N-K)*logK) which is asymptotically equal to O(N*logK). 
The space complexity will be O(K) because we need to store ‘K’ smallest numbers in the heap.
'''

'''
4. Using Min-Heap 
Also discussed in Kth Smallest Number, we can use a Min Heap to find the Kth smallest number. 
We can insert all the numbers in the min-heap and then extract the top ‘K’ numbers from the heap to find the Kth smallest number.

Time & Space Complexity 
Inserting all numbers in the heap will take O(N*logN) and extracting ‘K’ numbers will take O(K*logN). 
Overall, the time complexity of this algorithm will be O(N*logN+K*logN) and the space complexity will be O(N).
'''





def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()
