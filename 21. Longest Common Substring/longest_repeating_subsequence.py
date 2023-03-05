


# Driver code
def main():
    inputs = ["abcd", "abddccd", "abbaba", "aaaaba", "abcdaeda"]

    # Let's uncomment this and check the effect of dynamic programming with tabulation
    # inputs.append("abcdefghijklmnopqrstuv")

    for i in range(len(inputs)):
        print(str(i + 1) + ". String: "+str(inputs[i]))
        print("Longest repeating subsequence is", find_LRS(inputs[i]))
        print("-" * 100, "\n", sep="")


if __name__ == "__main__":
    main()