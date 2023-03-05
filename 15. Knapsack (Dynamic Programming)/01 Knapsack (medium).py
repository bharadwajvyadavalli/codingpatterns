'''
'''



#Basic Solution
def solve_knapsack(profits, weights, capacity):
  return knapsack_recursive(profits, weights, capacity, 0)


def knapsack_recursive(profits, weights, capacity, currentIndex):
  # base checks
  if capacity <= 0 or currentIndex >= len(profits):
    return 0

  # recursive call after choosing the element at the currentIndex
  # if the weight of the element at currentIndex exceeds the capacity, we  shouldn't process this
  profit1 = 0
  if weights[currentIndex] <= capacity:
    profit1 = profits[currentIndex] + knapsack_recursive(
      profits, weights, capacity - weights[currentIndex], currentIndex + 1)

  # recursive call after excluding the element at the currentIndex
  profit2 = knapsack_recursive(profits, weights, capacity, currentIndex + 1)

  return max(profit1, profit2)


def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()


'''
Time and Space complexity 
The time complexity of the above algorithm is exponential O(2^n), 
where ‘n’ represents the total number of items. This can also be confirmed from the above recursion tree. 
As we can see, we will have a total of ‘31’ recursive calls – calculated through (2^n) + (2^n) - 1, 
which is asymptotically equivalent to O(2^n).

The space complexity is O(n). This space will be used to store the recursion stack. 
Since the recursive algorithm works in a depth-first fashion, 
which means that we can’t have more than ‘n’ recursive calls on the call stack at any time.
'''



#Top-down Dynamic Programming with Memoization
def solve_knapsack(profits, weights, capacity):
  # create a two dimensional array for Memoization, each element is initialized to '-1'
  dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
  return knapsack_recursive(dp, profits, weights, capacity, 0)


def knapsack_recursive(dp, profits, weights, capacity, currentIndex):

  # base checks
  if capacity <= 0 or currentIndex >= len(profits):
    return 0

  # if we have already solved a similar problem, return the result from memory
  if dp[currentIndex][capacity] != -1:
    return dp[currentIndex][capacity]

  # recursive call after choosing the element at the currentIndex
  # if the weight of the element at currentIndex exceeds the capacity, we
  # shouldn't process this
  profit1 = 0
  if weights[currentIndex] <= capacity:
    profit1 = profits[currentIndex] + knapsack_recursive(
      dp, profits, weights, capacity - weights[currentIndex], currentIndex + 1)

  # recursive call after excluding the element at the currentIndex
  profit2 = knapsack_recursive(
    dp, profits, weights, capacity, currentIndex + 1)

  dp[currentIndex][capacity] = max(profit1, profit2)
  return dp[currentIndex][capacity]


def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()


'''
Time and Space complexity 
Since our memorization array dp[profits.length][capacity+1] stores the results for all subproblems, 
we can conclude that we will not have more than N*C subproblems (where ‘N’ is the number of items and ‘C’ is the knapsack capacity). 
This means that our time complexity will be O(N*C).

The above algorithm will use O(N*C) space for the memorization array. 
Other than that we will use O(N) space for the recursion call-stack. 
So the total space complexity will be O(N*C + N), which is asymptotically equivalent to O(N*C).
'''


#Bottom-up Dynamic Programming



def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()


'''
Time and Space complexity 
The above solution has the time and space complexity of O(N*C), where ‘N’ represents total items and ‘C’ is the maximum capacity.
'''






def main():
  print("Total knapsack profit: " +
        str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)))
  print("Total knapsack profit: " +
        str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)))


main()


'''
Time and Space complexity 
The above solution the has time and space complexity of O(N*S), 
where ‘N’ represents total numbers and ‘S’ is the total sum of all the numbers.
'''
