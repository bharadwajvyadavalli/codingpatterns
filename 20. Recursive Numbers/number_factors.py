# Available numbers are 1, 2, and 4


def main():
    target_numbers = [3, 5, 10, 25, 0]

    # You can uncomment the line below and check how this bottom-up solution executes without a time-out
    # target_numbers.append(50)

    for i in range(len(target_numbers)):
        num_ways = count_ways(target_numbers[i])
        print(i+1, ".", "\tNumber of ways to reach the target number ", target_numbers[i], ": ", num_ways, sep="")
        print("-" * 100)
        print()

if __name__ == '__main__':
    main()