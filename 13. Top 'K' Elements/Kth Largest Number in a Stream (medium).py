'''

'''


#mycode
from heapq import *




def main():

  kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
  print("4th largest number is: " + str(kthLargestNumber.add(6)))
  print("4th largest number is: " + str(kthLargestNumber.add(13)))
  print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()



#answer
from heapq import *


class KthLargestNumberInStream:
  minHeap = []

  def __init__(self, nums, k):
    self.k = k
    # add the numbers in the min heap
    for num in nums:
      self.add(num)

  def add(self, num):
    # add the new number in the min heap
    heappush(self.minHeap, num)

    # if heap has more than 'k' numbers, remove one number
    if len(self.minHeap) > self.k:
      heappop(self.minHeap)

    # return the 'Kth largest number
    return self.minHeap[0]


def main():

  kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
  print("4th largest number is: " + str(kthLargestNumber.add(6)))
  print("4th largest number is: " + str(kthLargestNumber.add(13)))
  print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()



'''
Time complexity 
The time complexity of the add() function will be O(logK) since we are inserting the new number in the heap.

Space complexity 
The space complexity will be O(K) for storing numbers in the heap.
'''