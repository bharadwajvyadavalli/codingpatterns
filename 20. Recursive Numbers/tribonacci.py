


# Driver code
def main():
    n = [4, 5, 25, 17, 19]

    # Let's uncomment this and check the effect of dynamic programming using memoization

    # n.append(45)

    for i in range(len(n)):
        print((i + 1), ".\tThe ", (n[i]), "th Tribonacci number is:  ",
              tribonacci(n[i]), sep="")
        print("-" * 100, "\n")


if __name__ == '__main__':
    main()