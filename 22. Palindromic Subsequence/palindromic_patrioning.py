


# Driver code
def main():
    inputs = ["radar", "abac", "book", "sleek", "fours"]

    # Let's uncomment this to see the benefit of using dynamic programming with tabulation
    # inputs.append("elwxubtrnarrrjguuqwwoopgwjaaeavczrdubcgfvnxeutcatt")

    for i in range(len(inputs)):
        print(i + 1, ".\t s:", inputs[i], "\n\n\t", \
              "The minimum number of cuts are:", min_cuts(inputs[i]))

        print("-" * 100)


if __name__ == '__main__':
    main()