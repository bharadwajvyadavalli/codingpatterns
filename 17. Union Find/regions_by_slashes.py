from union_find import UnionFind





def main():
    inputs = [["/\\", "\\/"], [" /", "  "], [" /", "/ "],
              [" /\\", "\\/ ", ' \\ '], [' \\/', " /\\", "\\/ "]]
    for i in range(len(inputs)):
        print(i + 1, '.\tInput list of strings: ', inputs[i], sep="")
        print('\tOutput: ', regions_by_slashes(inputs[i]))
        print('-' * 100)


if __name__ == "__main__":
    main()