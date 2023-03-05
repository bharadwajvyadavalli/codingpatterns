


# driver code
def main():
    input_1_strings = ["abcd", "educativeisfun", "cpprocks", "abcf", "dynamic"]
    input_2_strings = ["efgh", "algorithmsarefun", "cppisfun", "bdcf", "programming"]

    # let's uncomment the two lines below and see the effect of dynamic programming on a large test case

    # input_1_strings.append("iloveprogrammingbutprogrammingdoesnotloveme")
    # input_2_strings.append("computersarefastprogrammerskeepthemslow")

    for i in range(len(input_1_strings)):
        print(i + 1, ".", "\tString 1: ", input_1_strings[i], sep="")
        print("\tString 2: ", input_2_strings[i], sep="")
        length = shortest_common_supersequence(input_1_strings[i], input_2_strings[i])
        print("\tLength of Shortest Common Super-sequence: ", length, sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()