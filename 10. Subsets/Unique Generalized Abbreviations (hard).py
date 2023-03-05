'''

'''


#mycode





def main():
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("BAT")))
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("code")))


main()




#answer
from collections import deque


class AbbreviatedWord:

  def __init__(self, str, start,  count):
    self.str = str
    self.start = start
    self.count = count


def generate_generalized_abbreviation(word):
  wordLen = len(word)
  result = []
  queue = deque()
  queue.append(AbbreviatedWord(list(), 0, 0))
  while queue:
    abWord = queue.popleft()
    if abWord.start == wordLen:
      if abWord.count != 0:
        abWord.str.append(str(abWord.count))
      result.append(''.join(abWord.str))
    else:
      # continue abbreviating by incrementing the current abbreviation count
      queue.append(AbbreviatedWord(list(abWord.str),
                                   abWord.start + 1, abWord.count + 1))

      # restart abbreviating, append the count and the current character to the string
      if abWord.count != 0:
        abWord.str.append(str(abWord.count))

      newWord = list(abWord.str)
      newWord.append(word[abWord.start])
      queue.append(AbbreviatedWord(newWord, abWord.start + 1, 0))

  return result


def main():
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("BAT")))
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("code")))


main()


'''
Time complexity 
Since we had two options for each character, we will have a maximum of 2^N combinations. 
If you see the visual representation of Example-1 closely you will realize that it is equivalent to a binary tree, 
where each node has two children. This means that we will have 2^N leaf nodes and 2^N-1 intermediate nodes, 
so the total number of elements pushed to the queue will be 2^N + 2^N-1, which is asymptotically equivalent to O(2^N). 
While processing each element, we do need to concatenate the current string with a character. 
This operation will take O(N), so the overall time complexity of our algorithm will be O(N*2^N).

Space complexity 
All the additional space used by our algorithm is for the output list. 
Since we can’t have more than O(2^N) combinations, the space complexity of our algorithm is O(N*2^N).
'''

#Recursive Solution 
def generate_generalized_abbreviation(word):
  result = []
  generate_abbreviation_recursive(word, list(), 0, 0, result)
  return result


def generate_abbreviation_recursive(word, abWord, start, count, result):

  if start == len(word):
    if count != 0:
      abWord.append(str(count))
    result.append(''.join(abWord))
  else:
    # continue abbreviating by incrementing the current abbreviation count
    generate_abbreviation_recursive(
      word, list(abWord), start + 1, count + 1, result)

    # restart abbreviating, append the count and the current character to the string
    if count != 0:
      abWord.append(str(count))
    newWord = list(abWord)
    newWord.append(word[start])
    generate_abbreviation_recursive(word, newWord, start + 1, 0, result)


def main():
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("BAT")))
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("code")))


main()
