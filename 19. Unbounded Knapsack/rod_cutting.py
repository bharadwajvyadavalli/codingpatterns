


# Driver code
def main():
    n = [3, 4, 8, 4, 6]
    lengths = [
        [1, 2, 3],
        [2, 3, 4],
        [2, 1],
        [4, 3, 2, 1],
        [1, 2, 5, 4, 6],
    ]
    prices = [
        [7, 3, 8],
        [2, 7, 8],
        [20, 10],
        [1, 1, 1, 6],
        [2, 8, 9, 10, 11],
    ]

    # Let's uncomment this and check the effect of dynamic programming using tabulation

    # n.append(100)
    # prices.append([i for i in range(1, 200, 2)])
    # lengths.append([i for i in range(1, 101)])

    for i in range(len(n)):
        print(i + 1, ".\trod length: ", n[i], sep="")
        print("\tlengths: ", lengths[i])
        print("\tprices: ", prices[i])
        result = rod_cutting(lengths[i], prices[i], n[i])
        print("\tThe maximum profit found: ", result)
        print("-" * 100, sep="")


if __name__ == "__main__":
    main()