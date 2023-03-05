'''

'''


#mycode
from collections import deque

def find_trees(nodes, edges):
  # TODO: Write your code here
  inDegree = {i:0 for i in range(nodes)}
  graph = {i:[] for i in range(nodes)}

  for edge in edges:
    i, j = edge[0], edge[1]
    inDegree[i] += 1
    inDegree[j] += 1
    graph[i].append(j)
    graph[j].append(i)
  
  leaves = deque()
  for key in inDegree:
    if inDegree[key] == 1:
      leaves.append(key)
  
  totalSize = nodes
  while totalSize > 2:
    leafSize = len(leaves)
    totalSize -= leafSize
    for i in range(leafSize):
      vertex = leaves.popleft()
      for i in graph[vertex]:
        inDegree[i] -= 1
        if inDegree[i] == 1:
          leaves.append(i)

  return leaves


def main():
  print("Roots of MHTs: " +
        str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[1, 2], [1, 3]])))


main()



#answer



def main():
  print("Roots of MHTs: " +
        str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[1, 2], [1, 3]])))


main()



'''
Time complexity 
In step ‘d’, each node can become a source only once and each edge will be accessed and removed once. 
Therefore, the time complexity of the above algorithm will be O(V+E), 
where ‘V’ is the total nodes and ‘E’ is the total number of the edges.

Space complexity 
The space complexity will be O(V+E), since we are storing all of the edges for each node in an adjacency list.
'''