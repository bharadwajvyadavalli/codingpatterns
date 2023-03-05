


# Driver code
def main():
    nums = [[1, 3, 2, 5], [1, 2, 3, 4], [4, 3, 2, 1], [5, 5, 5, 5, 5], [9, 6, 4, 5, 6, 3]]

    # Let's uncomment this to see the benefit of using dynamic programming with tabulation
    # nums.append([1, 6, 4, 8, 2, 9, 4, 1, 7, 11, 23, 65, 34, 23, 45, 34, 34, 32, 32, 21, 67, 89, 76, 77, 66, 44, 89, 0, 1, 2, 3, 5, 4, 2, 5, 6, 43, 2, 4, 5, 2, 55, 66, 1, 6, 4, 8, 2, 9, 4, 1, 7, 11, 23, 65, 34, 23, 45, 34, 34, 32, 32, 21, 67, 89, 76, 77, 66, 44, 89, 0, 1, 2, 3, 5, 4, 2, 5, 6, 43, 2, 4, 5, 2, 55, 66])

    for i in range(0, len(nums)):
        print(i + 1, ".\tNums: ", nums[i], sep="")
        result = LAS(nums[i])
        print("\n\tThe Length of Longest Alternating Subsequence is: ", result, sep="")
        print("-" * 100, "\n", sep="")


if __name__ == '__main__':
    main()