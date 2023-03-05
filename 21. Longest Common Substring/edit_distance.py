


# Driver code to test the above function
if __name__ == '__main__':

    str1 = ["sunday", "sam", "110011010110001", "cat", "ball"]
    str2 = ["saturday", "samson", "1100101111110010", "cut", "baller"]

    # Let's uncomment this to see the benefit of using dynamic programming with tabulation

    # str1.append("iaetnxijfofxwnzfitssulvepiengehcaibfaorvraugndnurjfgixjljuibiaetnxijfofxwnzfitssulvepiengehcaibfaorvraugndnurjfgixjljuib")
    # str2.append("raetnsijfoyxwnzcitssolveppengeqcaibnaorveaugnvnurjmgixjljuibabcdraetnsijfoyxwnzcitssolveppengeqcaibnaorveaugnvnurjmgixjljuib")

    for i in range(len(str1)):
        print(i + 1, ".\tstr1: ", str1[i], sep="")
        print("\tstr2:", str2[i])
        print("\n\tMinimum Edit Distance:", min_edit_dist(str1[i], str2[i]))
        print('-' * 100)
