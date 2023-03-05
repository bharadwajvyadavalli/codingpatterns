'''

'''

#Basic Solution



def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 9])))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
  print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()



#Top-down Dynamic Programming with Memoization
def can_partition(num):
  s = sum(num)
  dp = [[-1 for x in range(s+1)] for y in range(len(num))]
  return can_partition_recursive(dp, num, 0, 0, 0)


def can_partition_recursive(dp, num, currentIndex, sum1, sum2):
  # base check
  if currentIndex == len(num):
    return abs(sum1 - sum2)

  # check if we have not already processed similar problem
  if dp[currentIndex][sum1] == -1:
    # recursive call after including the number at the currentIndex in the first set
    diff1 = can_partition_recursive(
      dp, num, currentIndex + 1, sum1 + num[currentIndex], sum2)

    # recursive call after including the number at the currentIndex in the second set
    diff2 = can_partition_recursive(
      dp, num, currentIndex + 1, sum1, sum2 + num[currentIndex])

    dp[currentIndex][sum1] = min(diff1, diff2)

  return dp[currentIndex][sum1]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 9])))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
  print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()




#Bottom-up Dynamic Programming



def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 9])))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
  print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()


'''
Time and Space complexity 
The above solution has the time and space complexity of O(N*S), 
where ‘N’ represents total numbers and ‘S’ is the total sum of all the numbers.
'''

