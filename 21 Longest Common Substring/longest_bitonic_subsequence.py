def lbs_length(nums):
    n = len(nums)
    lis_forward = [1] * n
    lis_backward = [1] * n
    result = 1

    # Populating the lis_forward array
    for i in range(n):
        for j in range(i):
            if (nums[i] > nums[j] and lis_forward[i] < 1 + lis_forward[j]):
                lis_forward[i] = 1 + lis_forward[j]

    # Populating the lis_backward array
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n, 1):
            if (nums[i] > nums[j] and lis_backward[i] < 1 + lis_backward[j]):
                lis_backward[i] = 1 + lis_backward[j]

    # Calculating the length of the bitonic subsequence at every index and
    # selecting the maximum one
    for i in range(n):
        length = lis_forward[i] + lis_backward[i] - 1
        result = max(result, length)

    return result


# Driver code
def main():
    inputs = [[10], [1, 8], [2, 4, 1], [6, 5, 3, 7, 10, 1, 2],
              [1, 4, 9, 2, 16, 20]]

    # You can uncomment the lines below and check how this recursive solution causes a time-out
    # inputs.append([23, 11, 12, 10, 15, 12, 6, 15, 18, 4, 14, 2, 13, 25, 27, 21, 2, 17, 18, 30, 22, 25, 10, 27, 10, 22, 21, 24, 26, 12, 26, 12, 3, 16, 4, 20, 18, 1, 5, 12, 10, 1, 14, 21, 15, 17, 21, 18, 13, 30, 20, 10, 5, 16, 9, 4, 25, 10, 8, 15, 2, 1, 13, 9, 12, 13, 6, 28, 6, 26, 8, 20, 29, 9, 5, 14, 13, 30, 7, 3, 2, 24, 28, 21, 7, 19, 14, 22, 28, 2, 20, 8, 6, 27, 12, 8, 27, 2, 27, 30, 8, 23, 16, 27, 25, 3, 1, 3, 5, 18, 2, 13, 18, 28, 2, 25, 20, 5, 11, 2, 28, 15, 15, 12, 25, 24, 17, 30, 17, 7, 18, 23, 13, 4, 4, 23, 23, 18, 16, 18, 14, 11, 26, 26, 22, 21, 23, 24, 24, 25, 20, 28, 18, 17, 21, 14, 16, 8, 19, 23, 26, 24, 28, 18, 26, 9, 22, 14, 15, 1, 11, 23, 20, 16, 4, 16, 5, 30, 19, 18, 6, 14, 23, 2, 1, 22, 29, 3, 29, 22, 30, 10, 30, 12, 17, 3, 12, 22, 8, 22])

    for i in range(len(inputs)):
        print(i + 1, ".\t nums:", inputs[i], "\n\n\t", \
              "The length of the longest bitonic subsequence is: ", lbs_length(inputs[i]))

        print("-" * 100)


if __name__ == '__main__':
    main()