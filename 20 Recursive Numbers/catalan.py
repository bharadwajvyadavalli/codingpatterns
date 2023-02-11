def catalan(n):
    # tabulating
    dp = [None] * (n + 1)
    # handling the base case
    dp[0] = 1
    # iterating to fill up the tabulation table
    for i in range(1, n + 1):
        # initializing the i-th value to 0
        dp[i] = 0
        # iterate from 0 to i; according to formula of catalan i.e.
        # C0*Ci + C1*Ci-1 + ... Ci*C0
        for j in range(i):
            # C(j) * C(i-j-1)
            dp[i] += (dp[j] * dp[i - j - 1])
    return dp[n]


# Driver code to test the above function
if __name__ == '__main__':

    n_list = [0, 1, 2, 4, 6]

    # Let's uncomment this to see the benefit of using dynamic programming with tabulation
    # n_list.append(22)

    for i in range(len(n_list)):
        print(i + 1, ".\tn: ", n_list[i], sep="")
        print("\n\tnth catalan number:", catalan(n_list[i]))
        print('-' * 100)