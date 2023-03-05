'''


'''


#mycode
from collections import deque
def print_orders(tasks, prerequisites):
  # TODO: Write your code here
  sortedOrder = []
  
  inDegree = {i: 0 for i in range(tasks)}
  graph = {i: [] for i in range(tasks)} 

  for prerequisite in prerequisites:
    start, end = prerequisite[0], prerequisite[1]
    graph[start].append(end)
    inDegree[end] += 1
  
  sources = deque() 
  for key in inDegree:
    if inDegree[key] == 0:
      sources.append(key)

  print_all_topological_sorts(graph, inDegree, sources, sortedOrder)

def print_all_topological_sorts(graph, inDegree, sources, sortedOrder):
  if sources:
    for vertex in sources:
      sortedOrder.append(vertex)
      next_sources = sources.copy()
      next_sources.remove(vertex)

      for i in graph[vertex]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
          next_sources.append(i)
      
      print_all_topological_sorts(graph, inDegree, next_sources, sortedOrder)

      sortedOrder.remove(vertex)
      for i in graph[vertex]:
        inDegree[i] += 1
  
  if len(sortedOrder) == len(inDegree):
    print(sortedOrder)

def main():
  print("Task Orders: ")
  print_orders(3, [[0, 1], [1, 2]])

  print("Task Orders: ")
  print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

  print("Task Orders: ")
  print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()




#answer



def main():
  print("Task Orders: ")
  print_orders(3, [[0, 1], [1, 2]])

  print("Task Orders: ")
  print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

  print("Task Orders: ")
  print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()



'''
Time and Space Complexity 
If we don’t have any prerequisites, all combinations of the tasks can represent a topological ordering. 
As we know, that there can be N! combinations for ‘N’ numbers, 
therefore the time and space complexity of our algorithm will be O(V! * E) 
where ‘V’ is the total number of tasks and ‘E’ is the total prerequisites. 
We need the ‘E’ part because in each recursive call, at max, we remove (and add back) all the edges.
'''