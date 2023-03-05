

def main():
    num_nodes = [3, 5, 5, 3, 2]
    node_values = [
        [[0, 5], [0, 1], [2, 3], [1, 10]],
        [[4, 1],  [2, 21]],
        [[4, 12], [2, 61]],
        [[0, 15], [0, 5], [2, 13], [1, 100]],
        [[0, 32], [0, 6], [1, 2]]
    ]
    values_to_get = [
        [[0, 0], [0, 1], [1, 0]],
        [[4, 1], [2, 1], [3, 1]],
        [[4, 1], [2, 1], [3, 1]],
        [[0, 1], [1, 1]],
        [[0, 0]]
    ]

    for i in range(len(num_nodes)):
        print(i + 1, ".\tInitializing a data structure with ", num_nodes[i], " nodes", sep = "")
        snapshot_arr = SnapshotArray(num_nodes[i])
        for j in node_values[i]:
            print("\t\tSetting the value of node ", j[0], " to ", j[1], sep = "")
            snapshot_arr.set_value(j[0], j[1])
            print("\t\tSnap id:", snapshot_arr.snapshot(), "\n", sep = "")
        for x in values_to_get[i]:
            print("\t\tNode value at index ", x[0], " with snapID: ", x[1], \
                    " is: ", snapshot_arr.get_value(x[0], x[1]), sep = "")
        print("\n", "-"*100, sep = "")


if __name__ == '__main__':
    main()