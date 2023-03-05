


# Driver code:

def main():
    s1 = ["abd", "abc", "abcdef", "", "xyz", "abcdefghijklmnopqrstuvwxyz"]
    s2 = ["cef", "def", "mnop", "", "abc", "abcdefghijklmnopqrstuvwxyz"]
    s3 = ["adcbef", "abcccf", "mnaobcdepf", "", "abc", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"]

    # Let's uncomment these three lines and check the effect of dynamic programming using tabulation
    # s1.append("abcdefghijklmnopqrstuvwxyz")
    # s2.append("abcdefghijklmnopqrstuvwxyz")
    # s3.append("aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz")
    for i in range(len(s1)):
        print("Test Case #", i + 1)
        print("The strings are:\ns1 = '", s1[i], "'\ns2 = '", s2[i], "'\ns3 = '", s3[i], "'", sep="")
        print("Is s3 a product of interleaving s1 and s2?")
        print(is_interleaving(s1[i], s2[i], s3[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()
