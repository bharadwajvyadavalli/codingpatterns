


# Driver Code
def main():
    s = ["vegancookbook", "catsanddog", "highwaycrash",
         "pineapplepenapple", "screamicecream", "educativecourse"]
    word_dict = ["oghi", "ncoo", "kboo", "inea",
                 "icec", "ghway", "tsand", "anco", "eame", "ghigh", "hi", "way", "wa"
                                                                                 "amic", "mi", "ed", "cecre", "pple",
                 "reamicecreamed", "ena", "tsa", "ami", "hwaycrashpineapplepenapplescreamicecreamed", "lepen", "okca",
                 "highway", "ples", "atsa", "oghig", "ookb", "epe", "ookca", "nea", "cra", "lepe",
                 "vegancookbookcatsandd"
                 "kc", "ra", "le", "ay", "crashpineapple", "ycras",
                 "vegancookbookcatsanddoghighwaycrashpineapplepenapplescre", "doghi", "nddo", "hway",
                 "vegancookbookcatsanddoghi", "vegancookbookcatsanddoghighwaycr", "at", "mice", "nc", "d",
                 "enapplescreamicecreamed", "h"
                                            "ecrea", "nappl", "shp", "kbo", "yc",
                 "vegancookbookcatsanddoghighwaycrashpineapplepenapplescream", "cat",
                 "waycrashpineapplepenapplescreamicecreamed", "tsan", "vegancookbookcatsanddoghighwaycrashpineap",
                 "ganco", "lescr", "sand", "applescreamicecreamed", "vegancookbookcatsanddoghig", "pi",
                 "vegancookbookcatsanddoghighwaycrashpineapp", "cookb", "okcat", "neap", "nap",
                 "oghighwaycrashpineapplepenapplescreamicecreamed", "crashpineapplepenapplescreamicecreamed",
                 "ashpi", "ega", "escreamicecreamed", "hwa", "rash", "cre", "micecreamed", "plepe", "coo", "epen",
                 "napp", "wayc", "vegancookbookcatsanddoghighwaycrashpinea", "vegancookbookcatsanddogh", "plep", "ice",
                 "ple", "gh", "ghw", "cook", "pl", "app", "ic", "pinea", "hello", "dog", "vegancookbookcat", "eamed",
                 "ook", "lesc", "ddog", "ca", "vegancookbookcatsanddoghighwaycrashpineapplepenapplescreamice", "c",
                 "escr", "penap", "boo", "eami", "ecreamed", "vegancookbookcatsanddoghighwaycrashpi", "igh", "mic",
                 "ganc", "vegancookbookcatsanddoghighwaycrashpineapplepenap",
                 "eappl", "vegancookbookcatsanddoghighway", "ep", "penapple", "b",
                 "ycrashpineapplepenapplescreamicecreamed", "pin", "book", "p", "sa", "okb", "andd", "ayc", "sh",
                 "vegan", "cookbook"]

    # Let's uncomment this to see the benefit of using dynamic programming with tabulation
    # s.append("vegancookbookcatsanddoghighwaycrashpineapplepenapplescream")

    print("The list of words we can use to break down the strings are:\n\n", word_dict, "\n")
    print("-" * 100)
    for i in range(len(s)):
        print("Test Case #", i + 1, "\n\nThe possible strings from the string '" +
              str(s[i]) + "' are the following combinations:", sep="")
        print("\n" + str(word_break(str(s[i]), word_dict)))
        print("-" * 100)


if __name__ == '__main__':
    main()