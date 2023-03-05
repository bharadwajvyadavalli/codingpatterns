'''

'''



#mycode
from collections import deque

def find_order(words):
  # TODO: Write your code here
  inDegree = {}
  graph = {}
  for word in words:
    for char in word:
      inDegree[char] = 0
      graph[char] = []
  
  for i in range(len(words)-1):
    word1, word2 = words[i], words[i+1]
    for j in range(min(len(word1),len(word2))):
      if word1[j] != word2[j]:
        inDegree[word2[j]] += 1
        graph[word1[j]].append(word2[j])
        break
  
  sources = deque()
  for key in inDegree:
    if inDegree[key] == 0:
      sources.append(key)
  
  
  sortedOrder = []
  while sources:
    vertex = sources.popleft()
    sortedOrder.append(vertex)

    for i in graph[vertex]:
      inDegree[i] -= 1
      if inDegree[i] == 0:
        sources.append(i)

  return "".join(sortedOrder)


def main():
  print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
  print("Character order: " + find_order(["cab", "aaa", "aab"]))
  print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()




#answer



def main():
  print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
  print("Character order: " + find_order(["cab", "aaa", "aab"]))
  print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()



'''
Time complexity 
In step ‘d’, each task can become a source only once and each edge (a rule) will be accessed and removed once. 
Therefore, the time complexity of the above algorithm will be O(V+E), 
where ‘V’ is the total number of different characters and ‘E’ is the total number of the rules in the alien language. 
Since, at most, each pair of words can give us one rule, therefore, 
we can conclude that the upper bound for the rules is O(N) where ‘N’ is the number of words in the input. 
So, we can say that the time complexity of our algorithm is O(V+N).

Space complexity 
The space complexity will be O(V+N), since we are storing all of the rules for each character in an adjacency list.
'''