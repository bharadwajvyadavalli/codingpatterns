'''

'''


#mycode
def find_target_subsets(num, s):
  dp = [[0 for x in range(2*sum(num)+1)] for y in range(len(num))]
  len_s = sum(num) - s

  for i in range(2*sum(num)+1):
    if i - len_s == num[0]:
      dp[0][i] = 1
    if i - len_s == -num[0]:
      dp[0][i] = 1
  
  for i in range(1,len(num)):
    for j in range(1,2*sum(num)+1):
      if j - num[i] >= 0:
        dp[i][j] += dp[i-1][j - num[i]]
      if j + num[i] <= 2*sum(num):
        dp[i][j] += dp[i-1][j + num[i]]
  return dp[len(num)-1][s+len_s]




#answer
def find_target_subsets(num, s):
  totalSum = sum(num)

  # if 's + totalSum' is odd, we can't find a subset with sum equal to '(s + totalSum) / 2'
  if totalSum < s or (s + totalSum) % 2 == 1:
    return 0

  return count_subsets(num, (s + totalSum) // 2)


# this function is exactly similar to what we have in 'Count of Subset Sum' problem.



def main():
  print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
  print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()


'''
Time and Space complexity 
The above solution has time and space complexity of O(N*S), where ‘N’ represents total numbers and ‘S’ is the desired sum.

We can further improve the solution to use only O(S) space.
'''



def find_target_subsets(num, s):
  totalSum = sum(num)

  # if 's + totalSum' is odd, we can't find a subset with sum equal to '(s +totalSum) / 2'
  if totalSum < s or (s + totalSum) % 2 == 1:
    return 0

  return count_subsets(num, (s + totalSum) // 2)


# this function is exactly similar to what we have in 'Count of Subset Sum' problem
def count_subsets(num, sum):
  n = len(num)
  dp = [0 for x in range(sum+1)]
  dp[0] = 1

  # with only one number, we can form a subset only when the required sum is equal to the number
  for s in range(1, sum+1):
    dp[s] = 1 if num[0] == s else 0

  # process all subsets for all sums
  for i in range(1, n):
    for s in range(sum, -1, -1):
      if s >= num[i]:
        dp[s] += dp[s - num[i]]

  return dp[sum]


def main():
  print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
  print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()
