


# Driver code to test the above function
if __name__ == '__main__':

    str1_list = ["abdbca", "cddpd", "pqr", "abaab", "aaa"]

    # Let's uncomment this to see the benefit of using dynamic programming with tabulation
    # str1_list.append("xkjkqlajprjwefilxgpdpebieswu")

    for i in range(len(str1_list)):
        print(i + 1, ".\tstr1: ", str1_list[i], sep="")
        print("\n\tCount of palindromic substrings:", count_palindromic_substring(str1_list[i]))
        print('-' * 100)