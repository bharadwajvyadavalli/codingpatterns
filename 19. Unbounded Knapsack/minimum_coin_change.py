


# Driver Code

def main():
    coins = [[1, 3, 4, 5], [1, 2, 3], [2, 3, 7], [1, 3, 9], [1, 4, 6, 9]]
    total = [7, 5, 1, 4, 11]

    # Let's uncomment this to see the benefit of using dynamic programming with tabulation

    # coins.append([34, 10, 415, 200])
    # total.append(610)

    for i in range(len(total)):
        print(str(i + 1) + ".\tThe minimum number of coins required to find " + \
              str(total[i]) + " from " + str(coins[i]) + " is: " + \
              str(coin_change(coins[i], total[i])))
        print("-" * 100)


if __name__ == '__main__':
    main()