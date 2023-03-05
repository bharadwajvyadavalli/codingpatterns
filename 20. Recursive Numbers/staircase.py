


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