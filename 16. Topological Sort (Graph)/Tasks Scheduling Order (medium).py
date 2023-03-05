'''

'''


#mycode



def main():
  print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()



#answer



def main():
  print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()



'''
Time complexity 
In step ‘d’, each task can become a source only once and each edge (prerequisite) will be accessed and removed once. 
Therefore, the time complexity of the above algorithm will be O(V+E), 
where ‘V’ is the total number of tasks and ‘E’ is the total number of prerequisites.

Space complexity 
The space complexity will be O(V+E), since we are storing all of the prerequisites for each task in an adjacency list.
'''

'''
Similar Problems 
Course Schedule: There are ‘N’ courses, labeled from ‘0’ to ‘N-1’. 
Each course has some prerequisite courses which need to be completed before it can be taken. 
Given the number of courses and a list of prerequisite pairs, 
write a method to find the best ordering of the courses that a student can take in order to finish all courses.

Solution: This problem is exactly similar to our parent problem. In this problem, we have courses instead of tasks.
'''