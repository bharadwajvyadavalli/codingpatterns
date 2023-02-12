from trie_node import *

class Trie():
    def __init__(self):
        self.root = TrieNode()

    # inserting string in trie
    def insert(self, word):
        node = self.root
        j = 0
        for c in word:
            j += 1
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children.get(c)
        node.is_word = True

    # searching for a string
    def search(self, word):
        node = self.root
        j = 0
        for c in word:
            if c not in node.children:
                return False
            node = node.children.get(c)
            j += 1
        return node.is_word

    def search_prefix(self, prefix):
        node = self.root
        j = 0
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children.get(c)
            j += 1
        return True


# Driver Code
def main():
    keys = ["the", "a", "there", "answer"]
    trie_for_keys = Trie()
    num = 1
    for x in keys:
        print(num, ".\tInserting key: ", x, sep="")
        trie_for_keys.insert(x)
        num += 1
        print("-"*100, "\n", sep="")

    search = ["a", "answer", "xyz", "an"]
    for y in search:
        print(num, ".\tSearching key: ", y, sep="")
        print("\t", trie_for_keys.search(y), sep="")
        num += 1
        print("-"*100, "\n", sep="")

    searchPrefix = ["b", "an"]
    for z in searchPrefix:
        print(num, ".\tSearching prefix: ", z, sep="")
        print("\t", trie_for_keys.search_prefix(z), sep="")
        num += 1
        print("-"*100, "\n", sep="")


if __name__ == "__main__":
    main()