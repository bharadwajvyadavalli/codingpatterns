


def main():
    sizes = [[1, 2, 3], [2, 3, 5], [2, 3], [3, 5, 7], [3, 5]]
    n = [5, 5, 7, 13, 7]

    # Let's uncomment this and check the effect of dynamic programming using tabulation

    # sizes.append([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    # n.append(1500)

    for i in range(len(n)):
        print(str(i + 1) + ".\tThe maximum number of sizes that can make up the n of " + \
              str(n[i]) + " from " + str(sizes[i]) + " is: " + \
              str(count_ribbon_pieces(n[i], sizes[i])))
        print("-" * 100)


if __name__ == '__main__':
    main()