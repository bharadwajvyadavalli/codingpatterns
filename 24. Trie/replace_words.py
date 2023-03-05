from trie_implementation import Trie





# driver code
def main():

    # input array of sentences
    sentence = ["where there is a will there is a way",
                "the quick brown fox jumps over the lazy dog",
                "oops there is no matching word in this sentence",
                "i was born on twenty ninth february",
                "i dont know where you are but i will find you eventually"]

    # input array of dictionary words to search in sentences
    dictionary = [["wi", "wa", "w"],
                  ["qui", "f", "la", "d"],
                  ["oops", "there", "is", "no", "matching", "word", "in", "this", "sentence"],
                  ["wa", "w", "a", "ty", "nint", "nin", "n", "feb", "februa", "f"],
                  ["cool", "how", "sunday", 'sun', "x"]]

    for i in range(len(sentence)):
        print(i + 1, ".\t Input sentence: '", sentence[i], "'", sep="")
        print("\t Dictionary words: ", dictionary[i], sep="")
        print("\t After replacing words: '",
              replace_words(sentence[i], dictionary[i]), "'", sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()