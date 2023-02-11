def tribonacci(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    # Creating an array
    dp = [0] * (n + 1)
    # First three tribonacci numbers
    dp[1], dp[2] = 1, 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]


# Driver code
def main():
    n = [4, 5, 25, 17, 19]

    # Let's uncomment this and check the effect of dynamic programming using memoization

    # n.append(45)

    for i in range(len(n)):
        print((i + 1), ".\tThe ", (n[i]), "th Tribonacci number is:  ",
              tribonacci(n[i]), sep="")
        print("-" * 100, "\n")


if __name__ == '__main__':
    main()