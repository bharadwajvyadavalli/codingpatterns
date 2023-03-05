from trie_node import *




def main():
    obj = WordDictionary()
    # Adding words
    words = ["add", "hello", "answer", "add"]
    i = 1
    for w in words:
        print(i, ".\tAdding word: ", w, sep="")
        obj.add_word(w)
        print("-"*100, "\n", sep="")
        i += 1

    # Searching words
    wordSearch = ["hello", "xyz", ".lo", "...lo"]
    for v in wordSearch:
        print(i, ".\tSearching word: ", v, sep="")
        print("\t", obj.search_word(v), sep="")
        print("-" * 100, "\n", sep="")
        i += 1

    # Getting all words
    print(i, ".\tGetting all words: ", obj.get_words(), sep="")
    print("-"*100, "\n", sep="")


if __name__ == "__main__":
    main()