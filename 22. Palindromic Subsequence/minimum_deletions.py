


# Driver code
def main():
    strings = ['raddar', 'lleveal', 'aqwrqhanisahinahqwe', 'pqr']

    # Let's uncomment this to see the benefit of using dynamic programming with tabulation

    # strings.append('aeqirradarqwruirrraaadddaqweraarrr')

    for i in range(len(strings)):
        print(i + 1, ". The minimum deletions required to make '", strings[i], "' a palindrome is: ",
              minimum_deletions(strings[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()