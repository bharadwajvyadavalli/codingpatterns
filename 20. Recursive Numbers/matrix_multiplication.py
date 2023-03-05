

# Driver code
def main():
    dims = [[3, 3, 2, 1], [4, 3, 2, 1], [2, 2, 2], [1, 1, 1], [13, 16, 11, 99, 3]]

    # Let's uncomment this to see the benefit of using dynamic programming with tabulation
    # dims.append([13, 16, 11, 99, 3, 13, 16, 11, 99, 3, 13, 16, 11, 99, 3, 13, 16, 11, 99, 3, 13, 16, 11, 99, 3, 13, 16, 11, 99, 3])

    for i in range(len(dims)):
        print(i + 1, ".\tInput dims: ", dims[i], sep="")
        result = min_multiplications(dims[i])
        print("\n\tThe least number of primitive multiplications possible: ", result, sep="")
        print("-" * 100, "\n", sep="")


if __name__ == '__main__':
    main()