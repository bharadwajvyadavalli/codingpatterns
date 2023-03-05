from trie_implementation import Trie





# Driver Code
def main():
    test_case_grid = [
        [['B', 'S', 'L', 'I', 'M'],
         ['R', 'I', 'L', 'M', 'O'],
         ['O', 'L', 'I', 'E', 'O'],
         ['R', 'Y', 'I', 'L', 'N'],
         ['B', 'U', 'N', 'E', 'C']],

        [['C', 'S', 'L', 'I', 'M'],
         ['O', 'I', 'B', 'M', 'O'],
         ['O', 'L', 'U', 'E', 'O'],
         ['N', 'L', 'Y', 'S', 'N'],
         ['S', 'I', 'N', 'E', 'C']],

        [['C', 'O', 'L', 'I', 'M'],
         ['I', 'N', 'L', 'M', 'O'],
         ['A', 'L', 'I', 'E', 'O'],
         ['R', 'T', 'A', 'S', 'N'],
         ['S', 'I', 'T', 'A', 'C']],

        [['P', 'S', 'L', 'A', 'M'],
         ['O', 'P', 'U', 'R', 'O'],
         ['O', 'L', 'I', 'E', 'O'],
         ['R', 'T', 'A', 'S', 'N'],
         ['S', 'I', 'T', 'A', 'C']],

        [['O', 'A', 'A', 'N'],
         ['E', 'T', 'A', 'E'],
         ['I', 'H', 'K', 'R'],
         ['I', 'F', 'L', 'V']],

        [['S', 'T', 'R', 'A', 'C'],
         ['I', 'R', 'E', 'E', 'E'],
         ['N', 'G', 'I', 'T', 'C'],
         ['I', 'T', 'S', 'R', 'A']],

        [['A', 'A', 'A'],
         ['A', 'A', 'A'],
         ['A', 'A', 'A']]
    ]

    strings_to_search = [
        ["BUY", "SLICK", "SLIME", "ONLINE", "NOW"],
        ["BUY", "STUFF", "ONLINE", "NOW"],
        ["REINDEER", "IN", "RAIN"],
        ["TOURISM", "DESTINY", "POPULAR"],
        ["OATH", "PEA", "EAT", "RAIN"],
        ["STREET", "STREETCAR", "STRING", "STING", "RING", "RACECAR"],
        ["A", "AA", "AAA", "AAAA"]
    ]

    for i in range(len(test_case_grid)):
        if i > 0:
            print()
        print(i + 1, ".\t2D Grid:\n", sep="")
        print_grid(test_case_grid[i])
        print("\n\tInput list: ", strings_to_search[i])
        print("\n\tOutput: ", find_strings(test_case_grid[i], strings_to_search[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()