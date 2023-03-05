# This method determines if a queen can be placed at proposed_row, proposed_col
# with current solution i.e. this move is valid only if no queen in current
# solution may attack the square at proposed_row and proposed_col



# Driver code
def main():
    n = [4, 5, 6, 7, 8]
    for i in range(len(n)):
        print(i + 1, ".\t Queens: ",
              n[i], ", Chessboard: (", n[i], "x", n[i], ")", sep="")
        res = solve_n_queens(n[i])
        global tab
        tab = 2
        print("\n\t Total solutions count for ",
              n[i], " queens on a ", n[i], "x", n[i], " chessboard: ", res, sep="")
        print("-" * 100, "\n", sep="")


if __name__ == '__main__':
    main()