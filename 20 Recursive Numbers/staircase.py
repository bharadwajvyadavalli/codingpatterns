def count_ways(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    # Initialize lookup table
    lookup_table = [0 for x in range(n + 1)]

    # Setting the first three values
    lookup_table[0] = 1
    lookup_table[1] = 1
    lookup_table[2] = 2

    for i in range(3, n + 1):
        # Fill up the table by summing up previous three values
        lookup_table[i] = lookup_table[i - 1] + lookup_table[i - 2] + lookup_table[i - 3]

        # Return the nth Fibonacci number
    return lookup_table[n]


# Driver code
def main():
    inputs = [0, 4, 3, 5, 6]

    # Let's uncomment this and check the effect of dynamic programming using tabulation
    # inputs.append(100)

    for i in range(len(inputs)):
        print(i + 1, ".\t Steps:", inputs[i], "\n\n\t", \
              "Number of ways:", count_ways(inputs[i]))

        print("-" * 100)


if __name__ == '__main__':
    main()