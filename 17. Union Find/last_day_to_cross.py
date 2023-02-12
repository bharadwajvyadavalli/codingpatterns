from union_find import UnionFind


def last_day_to_cross(row, col, cells):

    # Variables to track the top and bottom rows
    connections = UnionFind(row * col + 2)
    # Left, Right, Top, Bottom neighbours
    neighbours = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    # Subtract -1 from all the values in cells array i.e.
    # 2 -> 1 and 1-> 0
    # to make it 0-based
    cells = [(r - 1, c - 1) for r, c in cells]
    # Initialize a grid with the same dimensions as the matrix
    # and mark all the cells array as being filled with water
    grid = [[1] * col for _ in range(row)]

    # Start backtracking from last cell in cells array
    for i in range(len(cells) - 1, -1, -1):
        r, c = cells[i][0], cells[i][1]
        print("\n\tFor cell: [", r, "][", c, "]", sep="")
        # Make the current cell as land in the given cells array
        grid[r][c] = 0
        for r_neigh, c_neigh in neighbours:
            first_ind = connections.find_index(r + r_neigh, c + c_neigh, col)
            # Verify that traversing is within the limits of the grid
            if r + r_neigh >= 0 and r + r_neigh < row and \
                c + c_neigh >= 0 and c + c_neigh < col and \
                    grid[r + r_neigh][c + c_neigh] == 0:
                # check whether the neighbor is land or water
                # if we can move in any direction then we'll
                # find union of both indices
                print("\tNeighbor: [", r + r_neigh, "][",
                      c + c_neigh, "]", sep="")
                second_ind = connections.find_index(r, c, col)
                print("\tConnecting", first_ind, second_ind, "indices")
                connections.union(first_ind, second_ind)
        if r == 0:
            print("\tConnecting the top row with the "
                  "first index in 1D arry...")
            connections.union(0, connections.find_index(r, c, col))
            print("\n")
        if r == row - 1:
            print("\tConnecting the bottom row with the "
                  "last index in 1D arry...")
            rr = row * col + 1
            cc = connections.find_index(r, c, col)
            print("\tConnecting", rr, cc, "indices")
            connections.union(rr, cc)  # last index and current index
            print("\n")

        f1 = connections.find(0)
        f2 = connections.find(row*col + 1)
        print("\n\tUpdated array after finding the parent of"
              " first and last indices:", connections.parent)
        if f1 == f2:
            return i


def main():

    input = (
                (2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]]),
                (4, 4, [[2, 2], [2, 1], [3, 3], [2, 4],
                        [1, 3], [4, 3], [2, 3]]),
                (3, 3, [[1, 2], [2, 1], [3, 3], [2, 2],
                        [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]),
                (3, 4, [[2, 4], [1, 3], [3, 3], [2, 1], [2, 3],
                        [2, 2], [1, 4], [3, 1], [1, 1], [1, 2],
                        [3, 2], [3, 3]]),
                (5, 5, [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1],
                        [1, 2], [2, 2], [3, 2], [4, 2], [5, 2],
                        [1, 3], [2, 3], [3, 3], [4, 3], [5, 3],
                        [1, 4], [2, 4], [3, 4], [4, 4], [5, 4],
                        [1, 5], [2, 5], [3, 5], [4, 5], [5, 5],
                        ])
    )
    num = 1
    for i in input:
        print(f"{num}.\tNumber of rows : {i[0]}")
        print(f"\tNumber of columns : {i[1]}")
        print(f"\tCells : {i[2]}")
        print("\n\tProcessing...")
        print("\n\tLast day where we can still cross :",
              last_day_to_cross(i[0], i[1], i[2]))
        num += 1
        print("-" * 100, "\n")


if __name__ == "__main__":
    main()


