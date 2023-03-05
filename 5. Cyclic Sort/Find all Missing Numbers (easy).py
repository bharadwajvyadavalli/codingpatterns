'''

'''


#mycode
def find_missing_numbers(nums):
  missingNumbers = []
  # TODO: Write your code here
  i=0
  while i < len(nums):
    j=nums[i]-1
    if i !=j and j!= nums[j] -1:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1
  for i in range(len(nums)):
    if i != nums[i]-1:
      missingNumbers.append(i+1)
  return missingNumbers

'''
Be careful about i != j and nums[i] != nums[j]
when there are duplicates in index i, then using i!=j as condition, while will keep looping
using nums[i] != nums[j] can avoid this problem, because duplicates means there exists nums[i] = nums[j]

2 4 1 2

i=0
4 2 1 2
2 2 1 4
i=1
2 2 1 4
i=2
1 2 2 4
i=3
1 2 2 4
'''


#mycode2 
def find_missing_numbers(nums):
  missingNumbers = []
  # TODO: Write your code here
  for i in range(len(nums)):
    j=abs(nums[i])-1
    if nums[j] >= 0:
      nums[j] = -nums[j]
  
  for i in range(len(nums)):
    if nums[i] > 0:
      missingNumbers.append(i+1)
  return missingNumbers



#answer
def find_missing_numbers(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  missingNumbers = []

  for i in range(len(nums)):
    if nums[i] != i + 1:
      missingNumbers.append(i + 1)

  return missingNumbers


def main():
  print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
  print(find_missing_numbers([2, 4, 1, 2]))
  print(find_missing_numbers([2, 3, 2, 1]))


main()


'''
Time complexity 
The time complexity of the above algorithm is O(n).

Space complexity 
Ignoring the space required for the output array, the algorithm runs in constant space O(1).
'''
