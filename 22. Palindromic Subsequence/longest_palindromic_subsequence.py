


# Driver code to test the above function
if __name__ == '__main__':
    strings = ['cddpd', 'abdbca', 'racecar', 'pqr']

    # Let's uncomment this to see the benefit of using dynamic programming with tabulation

    # strings.append('aeqirradarqwruirrraaadddaqweraarrr')

    for i in range(len(strings)):
        print(str(i + 1) + ". The length of the longest palindromic subsequence in '", strings[i], "' is: ",
              longest_palindromic_subsequence(strings[i]), sep="")
        print("-" * 100)