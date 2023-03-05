


# Driver code
def main():
    strings = ['abcbda', 'tworacecars', 'pqrssrqp', 'mnop', 'bbbbbbbbbbbbbbbbbbbb']

    # Let's uncomment this to see the benefit of using dynamic programming with tabulation
    # strings.append('mwusjunybvgafxuhloqwfoizqkkqzilltjw')

    for i in range(len(strings)):
        print(i + 1, ".\t Input string: '", strings[i], "'", sep="")
        result = find_lps_length(strings[i])
        print("\t Length of the longest palindromic substring: ", result, sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()