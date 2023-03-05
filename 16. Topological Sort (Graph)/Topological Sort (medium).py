'''


'''



#mycode
from collections import deque

def topological_sort(vertices, edges):
  sortedOrder = []
  # TODO: Write your code here
  inDegree={i:0 for i in range(vertices)}
  graph = {i:[] for i in range(vertices)}

  for edge in edges:
    in_node, out_node = edge[0], edge[1]
    graph[in_node].append(out_node)
    inDegree[out_node] += 1
  
  sources = deque()
  for key in graph:
    if inDegree[key] == 0:
      sources.append(key)

  while sources:
    in_node = sources.popleft()
    sortedOrder.append(in_node)

    for i in graph[in_node]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
          sources.append(i)
          
  if len(sortedOrder) != vertices:
    return []

  return sortedOrder


def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()





#answer



def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()



'''
Time Complexity 
In step ‘d’, each vertex will become a source only once and each edge will be accessed and removed once. 
Therefore, the time complexity of the above algorithm will be O(V+E), 
where ‘V’ is the total number of vertices and ‘E’ is the total number of edges in the graph.

Space Complexity 
The space complexity will be O(V+E), since we are storing all of the edges for each vertex in an adjacency list.
'''



'''
Similar Problems 
Problem 1: Find if a given Directed Graph has a cycle in it or not.

Solution: If we can’t determine the topological ordering of all the vertices of a directed graph, the graph has a cycle in it. This was also referred to in the above code:

    if (sortedOrder.size() != vertices) // topological sort is not possible as the graph has a cycle
      return new ArrayList<>();
'''