class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        # below data members used only for some of the problems
        self.next = None
        self.parent = None
        self.count = 0
        
from binary_tree_node import *

class BinaryTree:
    def __init__(self, *args):
        if len(args) < 1:
            self.root = None
        elif isinstance(args[0], int):
            self.root = BinaryTreeNode(args[0])
        else:
            self.root = None
            for x in args[0]:
                self.insert(x)

    # for BST insertion
    def insert(self, node_data):
        new_node = BinaryTreeNode(node_data)
        if not self.root:
            self.root = new_node
        else:
            parent = None
            temp_pointer = self.root
            while temp_pointer:
                parent = temp_pointer
                if node_data <= temp_pointer.data:
                    temp_pointer = temp_pointer.left
                else:
                    temp_pointer = temp_pointer.right
            if node_data <= parent.data:
                parent.left = new_node
            else:
                parent.right = new_node

    def find_in_bst_rec(self, node, node_data):
        if not node:
            return None
        if node.data == node_data:
            return node
        elif node.data > node_data:
            return self.find_in_bst_rec(node.left, node_data)
        else:
            return self.find_in_bst_rec(node.right, node_data)

    def find_in_bst(self, node_data):
        return self.find_in_bst_rec(self.root, node_data)

    def get_sub_tree_node_count(self, node):
        if not node:
            return 0
        else:
            return 1 + self.get_sub_tree_node_count(node.left) + self.get_sub_tree_node_count(node.right)

    def get_tree_deep_copy_rec(self, node):
        if node:
            new_node = BinaryTreeNode(node.data)
            new_node.left = self.get_tree_deep_copy_rec(node.left)
            new_node.right = self.get_tree_deep_copy_rec(node.right)
            return new_node
        else:
            return None

    def get_tree_deep_copy(self):
        if not self.root:
            return None
        else:
            tree_copy = BinaryTree()
            tree_copy.root = self.get_tree_deep_copy_rec(self.root)
            return tree_copy

from binary_tree import *
from binary_tree_node import *


def rob(root):
    # returns pair: [withRoot, withoutRoot]
    return max(depthfs(root))


def depthfs(root):
    if root == None:  # Empty tree case
        return [0, 0]

    left_children = depthfs(root.left)  # Calculating the amount we can rob from left children of the node
    right_children = depthfs(root.right)  # Calculating the amount we can rob from right children of the node

    not_node = max(left_children) + max(right_children)  # Adding the maximum we can get from both sides
    node = root.data + left_children[1] + right_children[1]  # Calculating value with node

    return [node, not_node]  # Returning both the results, with node and without node.


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