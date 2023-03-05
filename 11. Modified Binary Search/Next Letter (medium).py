'''

'''


#mycode



def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()



#answer
def search_next_letter(letters, key):
  n = len(letters)
  if key < letters[0] or key > letters[n - 1]:
    return letters[0]

  start, end = 0, n - 1
  while start <= end:
    mid = start + (end - start) // 2
    if key < letters[mid]:
      end = mid - 1
    else: # key >= letters[mid]:
      start = mid + 1

  # since the loop is running until 'start <= end', so at the end of the while loop, 'start == end+1'
  return letters[start % n]


def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()



'''
Time complexity 
Since, we are reducing the search range by half at every step, 
this means that the time complexity of our algorithm will be O(logN)O 
where ‘N’ is the total elements in the given array.

Space complexity 
The algorithm runs in constant space O(1).
'''