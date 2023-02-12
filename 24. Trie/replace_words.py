from trie_implementation import Trie


def replace_words(sentence, dictionary):
    trie = Trie()
    # iterate over the dictionary words, and
    # insert them as prefixes into the trie
    for prefix in dictionary:
        trie.insert(prefix)
    # split and assign each word from the sentence to new_list
    # this new_list is intended to return the final sentence
    # after all possible replacements have been made
    new_list = sentence.split()

    # iterate over all the words in the sentence
    for i in range(len(new_list)):
        # replace each word in the new_list with the
        # smallest word from dictionary
        new_list[i] = trie.replace(new_list[i])

    # after replacing each word with the matching dictionary word,
    # join them with a space in between them to reconstruct the sentence
    return " ".join(new_list)


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