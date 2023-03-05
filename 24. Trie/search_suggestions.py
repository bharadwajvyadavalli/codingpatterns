from trie_node import *




# Driver code
def main():
    products = ["bat", "bag", "bassinet", "bread", "cable",
                "table", "tree", "tarp"]
    search_word_list = ["ba", "in", "ca", "t"]
    for i in range(len(search_word_list)):
        print(i + 1, ".\tProducts:", products, sep="")
        print("\tSearch keyword: '", search_word_list[i], "'", sep="")
        print("\tSuggested Products: ", suggested_products(
            products, search_word_list[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()