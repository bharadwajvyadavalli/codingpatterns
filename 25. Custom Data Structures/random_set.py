


# Driver code
def main():

    commands = [["I", "G", "I", "I", "R", "G"],
                ["I", "I", "R", "G", "R", "I"]]
    values = [[10, -1, 100, 1000, 200, -1], [30, 60, 10, -1, 30, 90]]
    for i in range(len(commands)):
        dataset = RandomSet()
        print(i+1, ". Starting operations:")
        for j in range(len(commands[i])):
            if commands[i][j] == "I":
                print("\tInsert (", values[i][j], ") returns ",
                      dataset.insert(values[i][j]))
            elif commands[i][j] == "R":
                print("\tDelete (", values[i][j], ") returns ",
                      dataset.delete(values[i][j]))
            elif commands[i][j] == "G":
                print("\tGenerate Random() returns ",
                      dataset.get_random())
        print("-"*98)


if __name__ == '__main__':
    main()