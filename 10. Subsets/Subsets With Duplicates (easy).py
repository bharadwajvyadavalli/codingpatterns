'''

'''

#mycode



def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()



#answer
def find_subsets(nums):
  # sort the numbers to handle duplicates
  list.sort(nums)
  subsets = []
  subsets.append([])
  startIndex, endIndex = 0, 0
  for i in range(len(nums)):
    startIndex = 0
    # if current and the previous elements are same, create new subsets only from the subsets
    # added in the previous step
    if i > 0 and nums[i] == nums[i - 1]:
      startIndex = endIndex + 1
    endIndex = len(subsets) - 1
    for j in range(startIndex, endIndex+1):
      # create a new subset from the existing subset and add the current element to it
      set = list(subsets[j])
      set.append(nums[i])
      subsets.append(set)
  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()


'''
Time complexity 
Since, in each step, the number of subsets could double (if not duplicate) as we add each element to all the existing subsets, 
the time complexity of the above algorithm is O(2^N), where ‘N’ is the total number of elements in the input set. 
This also means that, in the end, we will have a total of O(2^N) subsets at the most.

Space complexity 
All the additional space used by our algorithm is for the output list. Since at most we will have a total of O(2^N) subsets, 
the space complexity of our algorithm is also O(2^N).
'''