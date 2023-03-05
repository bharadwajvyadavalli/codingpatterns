'''

'''

#mycode
from heapq import *

class MedianOfAStream:

  minHeap = []
  maxHeap = []

  def insert_num(self, num):
   # TODO: Write your code here
    if not self.minHeap or num <= -self.minHeap[0]:
      heappush(self.minHeap, -num)
    else:
      heappush(self.maxHeap, num)
    
    if len(self.minHeap) > len(self.maxHeap) + 1:
      heappush(self.maxHeap, -heappop(self.minHeap))
    elif len(self.minHeap) < len(self.maxHeap):
      heappush(self.minHeap,-heappop(self.maxHeap))


  def find_median(self):
    # TODO: Write your code here
    if len(self.maxHeap) == len(self.minHeap):
      return (self.maxHeap[0] - self.minHeap[0]) / 2
    else:
      return -self.minHeap[0]


def main():
  medianOfAStream = MedianOfAStream()
  medianOfAStream.insert_num(3)
  medianOfAStream.insert_num(1)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(5)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(4)
  print("The median is: " + str(medianOfAStream.find_median()))


main()



#answer
from heapq import *





def main():
  medianOfAStream = MedianOfAStream()
  medianOfAStream.insert_num(3)
  medianOfAStream.insert_num(1)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(5)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(4)
  print("The median is: " + str(medianOfAStream.find_median()))


main()




'''
Time complexity 
The time complexity of the insertNum() will be O(logN) due to the insertion in the heap. 
The time complexity of the findMedian() will be O(1) as we can find the median from the top elements of the heaps.

Space complexity 
The space complexity will be O(N) because, as at any time, we will be storing all the numbers.
'''