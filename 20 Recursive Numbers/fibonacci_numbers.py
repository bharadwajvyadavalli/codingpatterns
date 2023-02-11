def get_fibonacci(n):
    # Base case
    if n < 2:
        return n
    # Initializing the lookup table
    lookup_table = [0] * (n + 1)
    lookup_table[0] = 0
    lookup_table[1] = 1

    for i in range(2, n + 1):
        # Storing sum of the two preceding values
        lookup_table[i] = lookup_table[i - 1] + lookup_table[i - 2]

    return lookup_table[n]


# Driver code
def main():
    inputs = [0, 5, 7, 10, 14]

    # Let's uncomment this to see the benefit of using dynamic programming with tabulation
    # inputs.append(60)

    for i in range(len(inputs)):
        print(str(i + 1) + ". " + str(inputs[i]) + "th Fibonacci number is:", get_fibonacci(inputs[i]))
        print("-" * 100, "\n", sep="")


if __name__ == "__main__":
    main()