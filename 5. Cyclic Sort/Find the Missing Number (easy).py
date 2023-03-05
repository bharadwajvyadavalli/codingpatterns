'''

'''

#mycode
def find_missing_number(nums):
  # TODO: Write your code here
  for i in range(len(nums)):
    if abs(nums[i]) < len(nums):
      nums[abs(nums[i])] = -nums[abs(nums[i])] 
  
  for i in range(len(nums)):
    if nums[i] > 0:
      return i
  return len(nums)

#answer



def main():
  print(find_missing_number([4, 0, 3, 1]))
  print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()



'''
Time complexity 
The time complexity of the above algorithm is O(n). 
In the while loop, although we are not incrementing the index i when swapping the numbers, 
this will result in more than ‘n’ iterations of the loop, 
but in the worst-case scenario, the while loop will swap a total of ‘n-1’ numbers and once a number is at its correct index, 
we will move on to the next number by incrementing i. 
In the end, we iterate the input array again to find the first number missing from its index, 
so overall, our algorithm will take O(n) + O(n-1) + O(n)  which is asymptotically equivalent to O(n).

Space complexity 
The algorithm runs in constant space O(1).
'''