


def main():
    input1 = [10, 9, 20, 15, 7]
    tree1 = BinaryTree(input1)

    input2 = [7, 9, 10, 15, 20]
    tree2 = BinaryTree(input2)

    input3 = [8, 2, 17, 1, 4, 19, 5]
    tree3 = BinaryTree(input3)

    input4 = [7, 3, 4, 1, 3]
    tree4 = BinaryTree(input4)

    input5 = [9, 5, 7, 1, 3]
    tree5 = BinaryTree(input5)

    inputTrees = [tree1.root, tree2.root, tree3.root, tree4.root, tree5.root]
    x = 1
    for i in inputTrees:
        print(x, ".\tInput Tree:", sep="")
        display_tree(i)
        x += 1
        print("\tMaximum amount we can rob without getting caught: ", rob(i), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()