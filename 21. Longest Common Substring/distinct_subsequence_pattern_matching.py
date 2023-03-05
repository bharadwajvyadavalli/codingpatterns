# function to calculate the number of subsequences



# driver code
def main():
    input_1_strings = ["bbagbag", "dawawg", "programming", "googlegoogle", "wowowl"]
    input_2_strings = ["bag", "aw", "ram", "gogl", "owl"]

    # let's uncomment the lines below and see the effect of dynamic programming on a large test case

    # input_1_strings.append("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab")
    # input_2_strings.append("abababababababababababababababababababababababababababababababababababababababababababababababababab")

    for i in range(0, len(input_1_strings)):
        print(f"{i + 1}.\tString 1: '{input_1_strings[i]}'")
        print(f"\tString 2: '{input_2_strings[i]}'")
        result = number_of_subsequences(input_1_strings[i], input_2_strings[i])
        print(f"\n\tNumber of distinct subsequences: {result}")
        print("-" * 100)


if __name__ == '__main__':
    main()