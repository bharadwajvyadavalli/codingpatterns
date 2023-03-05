


# Driver code
def main():
    inputs = [[5, 4, 4, 7, 2, 9], [3, 25, 4, 12, 2], [3, 7, 4, 12, 2],
              [1, 1, 1, 1000, 1], [45, 2, 9, 87, 9, 12, 54, 56]]

    # Let's uncomment this and check the effect of dynamic programming using tabulation

    # inputs.append([4, 11, 15, 17, 18, 25, 26, 29, 32, 35, 37, 42, 43, 45, 46,
    # 		       48, 49, 55, 62, 66, 67, 68, 70, 78, 83, 88, 92, 94, 96, 100])

    for i in range(len(inputs)):
        print(i + 1, ".\t nums:", inputs[i], "\n\n\t", \
              "The minimum subarray sum is:", minimum_subarray_sum_difference(inputs[i]))

        print("-" * 100)


if __name__ == '__main__':
    main()