# function to find the maximum number of matching characters subsequence



# Driver code to test the above function
if __name__ == '__main__':
    str1_list = ["pqr", "heap", "passport", "baller", "sam", "bed"]
    str2_list = ["tqr", "pea", "ppsspt", "ball", "samson", "read"]

    # Let's uncomment this to see the benefit of using dynamic programming with tabulation
    # str1_list.append("sjcneiurutvmpdkapbrcapjru")
    # str2_list.append("oidhfwepkxwebyurtunvidqlscmjbg")

    for i in range(len(str1_list)):
        print(i + 1, ".\tstr1: ", str1_list[i], sep="")
        print("\tstr2:", str2_list[i])
        deletions, insertions = min_del_ins(str1_list[i], str2_list[i])
        print("\n\tMinimum deletions required:  ", deletions)
        print("\tMinimum insertions required: ", insertions)
        print('-' * 100)
