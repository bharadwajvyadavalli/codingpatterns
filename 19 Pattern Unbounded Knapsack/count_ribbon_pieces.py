import math


def count_ribbon_pieces(n, sizes):
    # create the array to store the results
    dp = [-1] * (n + 1)
    dp[0] = 0
    # calculate the results for all combinations
    # and select the maximum
    for i in range(1, n + 1):
        for c in sizes:
            if i - c >= 0 and dp[i - c] != -1:
                dp[i] = max(dp[i], 1 + dp[i - c])

    if dp[n] != -1:
        return dp[n]
    else:
        return -1


def main():
    sizes = [[1, 2, 3], [2, 3, 5], [2, 3], [3, 5, 7], [3, 5]]
    n = [5, 5, 7, 13, 7]

    # Let's uncomment this and check the effect of dynamic programming using tabulation

    # sizes.append([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    # n.append(1500)

    for i in range(len(n)):
        print(str(i + 1) + ".\tThe maximum number of sizes that can make up the n of " + \
              str(n[i]) + " from " + str(sizes[i]) + " is: " + \
              str(count_ribbon_pieces(n[i], sizes[i])))
        print("-" * 100)


if __name__ == '__main__':
    main()