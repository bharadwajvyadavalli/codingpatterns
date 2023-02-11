def house_thief(money):
    # Stopping criteria
    stop = len(money)
    # Base case
    if stop == 0:
        return 0

    memo = [0] * (stop + 1)
    memo[1] = money[0]
    for i in range(1, stop):
        # stores the maximum of the following two values at memo[i+1]:
        # 1. The combined sum of money in the current house alongwith
        # the maximum theft possible from the previous of the previous house.
        # 2. The maximum theft possible till the previous house, we should refer to memo to get this value.
        memo[i + 1] = max(money[i] + memo[i - 1], memo[i])
    return memo[stop]


# Driver code
def main():
    lists = [[2, 7, 9, 31, 33, 4, 99, 1, 2, 3, 15, 34, 23, 11, 9, 1, 4], [1, 2, 3, 1],
             [4, 6, 3, 9, 3, 8, 3], [1, 5, 7, 3, 7, 2, 3], [2, 7, 9, 3, 1]]

    # Let's uncomment this to see the benefit of using dynamic programming with bottom-up approach

    # lists.append([2, 7, 9, 31, 33, 56, 78, 59, 85, 7, 3, 74, 6, 3, 9, 3, 8,
    # 30, 1, 2, 5, 10, 30, 50, 4, 99, 202, 150, 33, 65, 79, 2, 3, 1 , 2, 3,
    # 15, 34, 23, 11, 9, 8, 5, 78, 89, 12, 56, 78, 23, 90, 66, 5, 7, 9, 1, 4])

    for i in lists:
        print('Maximum Theft in example', i, 'is', house_thief(i))
        print("-" * 100, "\n", sep="")


if __name__ == '__main__':
    main()