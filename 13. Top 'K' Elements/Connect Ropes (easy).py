'''

'''


#mycode
from heapq import *



def main():

  print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()



#answer
from heapq import *


def minimum_cost_to_connect_ropes(ropeLengths):
  minHeap = []
  # add all ropes to the min heap
  for i in ropeLengths:
    heappush(minHeap, i)

  # go through the values of the heap, in each step take top (lowest) rope lengths from the min heap
  # connect them and push the result back to the min heap.
  # keep doing this until the heap is left with only one rope
  result, temp = 0, 0
  while len(minHeap) > 1:
    temp = heappop(minHeap) + heappop(minHeap)
    result += temp
    heappush(minHeap, temp)

  return result


def main():

  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))

main()




'''
Time complexity 
Given ‘N’ ropes, we need O(N*logN)to insert all the ropes in the heap. 
In each step, while processing the heap, we take out two elements from the heap and insert one. 
This means we will have a total of ‘N’ steps, having a total time complexity of O(N*logN).

Space complexity #
The space complexity will be O(N) because we need to store all the ropes in the heap.
'''