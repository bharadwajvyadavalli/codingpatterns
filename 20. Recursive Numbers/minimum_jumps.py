


# Driver code
def main():
    inputs = [[7], [1, 0], [2, 3, 1, 1, 4], [2, 1, 1, 1, 4], [1, 1, 3, 6, 9, 3, 0, 1, 3]]

    # Let's uncomment this to see the benefit of using dynamic programming with tabulation
    # inputs.append([2, 9, 4, 6, 1, 4, 7, 10, 0, 3, 9, 7, 4, 10, 5, 9, 3, 9, 7, 7, 10, 1, 8, 5, 9, 3, 1, 5, 9, 7, 7, 6, 3, 9, 7, 0, 1, 9, 9, 0, 9, 4, 9, 6, 2, 9, 3, 7, 6, 4])

    for i in range(len(inputs)):
        print(str(i + 1) + ". " + str(inputs[i]))
        print("Minimum jumps to reach the end:", find_min_jumps(inputs[i]))
        print("-" * 100, "\n", sep="")


if __name__ == "__main__":
    main()