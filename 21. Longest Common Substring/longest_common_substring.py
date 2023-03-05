


# Driver code
def main():
    s1 = ["educative", "bcdcdcd", "arefun", "yourocks", "abc"]
    s2 = ["education", "aacdcdcd", "isfun", "youawesome", "def"]

    # Let's uncomment this to see the benefit of using dynamic programming with tabulation
    # s1.append("ypzrvyigwdiqrnbglvviozqzruvmwivgvqvrfhqi")
    # s2.append("wdiqrnbglvviozqzruvmwivgvqvrfhqiypzrvyigwdiqrn")

    for i in range(0, len(s1)):
        print(i + 1, ".\tString 1: \"", s1[i], "\" \n\tString 2: \"", s2[i], "\"", sep="")
        result = lcs_length(s1[i], s2[i])
        print("\n\tThe Length of Longest Common Substring is: ", result, sep="")
        print("-" * 100, "\n", sep="")


if __name__ == '__main__':
    main()