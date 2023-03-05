'''

'''


#mycode
from collections import deque

def can_construct(originalSeq, sequences):
  # TODO: Write your code here
  inDegree = {}
  graph = {}

  for sequence in sequences:
    for i in sequence:
      inDegree[i] = 0
      graph[i] = []

  for sequence in sequences:
    for i in range(1,len(sequence)):
      start, end = sequence[i-1], sequence[i]
      inDegree[end] += 1
      graph[start].append(end)
  
  if len(inDegree) != len(originalSeq):
    return False

  sources = deque()
  for key in inDegree:
    if inDegree[key] == 0:
      sources.append(key)

  sortedOrder = []
  while sources:
    if len(sources) != 1:
      return False
    if originalSeq[len(sortedOrder)] != sources[0]:
      return False
    vertex = sources.popleft()
    sortedOrder.append(vertex)
    for i in graph[vertex]:
      inDegree[i] -= 1
      if inDegree[i] == 0:
        sources.append(i)

  return len(sortedOrder) == len(originalSeq)


def main():
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
  print("Can construct: " +
        str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()




#answer



def main():
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
  print("Can construct: " +
        str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()


'''
Time complexity 
In step ‘d’, each number can become a source only once and each edge (a rule) will be accessed and removed once. 
Therefore, the time complexity of the above algorithm will be O(V+E), 
where ‘V’ is the count of distinct numbers and ‘E’ is the total number of the rules. Since, at most, 
each pair of numbers can give us one rule, we can conclude that the upper bound for the rules is O(N) where ‘N’ is the count of numbers in all sequences. 
So, we can say that the time complexity of our algorithm is O(V+N).

Space complexity 
The space complexity will be O(V+N), since we are storing all of the rules for each number in an adjacency list.
'''