'''

'''

#mycode


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()



#answer
from heapq import *


def find_Kth_smallest(lists, k):
  minHeap = []

  # put the 1st element of each list in the min heap
  for i in range(len(lists)):
    heappush(minHeap, (lists[i][0], 0, lists[i]))

  # take the smallest(top) element form the min heap, if the running count is equal to k return the number
  numberCount, number = 0, 0
  while minHeap:
    number, i, list = heappop(minHeap)
    numberCount += 1
    if numberCount == k:
      break
    # if the array of the top element has more elements, add the next element to the heap
    if len(list) > i+1:
      heappush(minHeap, (list[i+1], i+1, list))

  return number


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()



'''
Time complexity 
Since we’ll be going through at most ‘K’ elements among all the arrays, 
and we will remove/add one element in the heap in each step, 
the time complexity of the above algorithm will be O(K*logM) where ‘M’ is the total number of input arrays.

Space complexity 
The space complexity will be O(M) because, at any time, 
our min-heap will be storing one number from all the ‘M’ input arrays.
'''


'''
Similar Problems 
Problem 1: Given ‘M’ sorted arrays, find the median number among all arrays.

Solution: This problem is similar to our parent problem with K=Median. 
So if there are ‘N’ total numbers in all the arrays we need to find the K’th minimum number where K=N/2K.

Problem 2: Given a list of ‘K’ sorted arrays, merge them into one sorted list.

Solution: This problem is similar to Merge K Sorted Lists except that 
the input is a list of arrays compared to LinkedLists. 
To handle this, we can use a similar approach as discussed in our parent problem 
by keeping a track of the array and the element indices.
'''