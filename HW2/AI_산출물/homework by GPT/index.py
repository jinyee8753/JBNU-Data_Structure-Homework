"""Verify BST and AVL insertion/deletion results with bintrees."""

from bintrees import AVLTree, BinaryTree


INSERT_SEQ = (5, 3, 7, 8, 2, 9, 1)
DELETE_SEQ = (1, 2, 5, 8, 9)


def traversal(tree, order):
    """bintrees foreach order: -1=pre-order, 0=in-order, 1=post-order."""
    result = []
    tree.foreach(lambda key, value: result.append(key), order)
    return result


def print_traversals(problem_number, tree):
    print(f"{problem_number}.")
    print("In-order  " + " ".join(map(str, traversal(tree, 0))))
    print("Pre-order " + " ".join(map(str, traversal(tree, -1))))
    print("Post-order " + " ".join(map(str, traversal(tree, 1))))


def build_tree(tree_type):
    tree = tree_type()
    for key in INSERT_SEQ:
        tree.insert(key, None)
    return tree


def delete_sequence(tree):
    for key in DELETE_SEQ:
        tree.remove(key)


def main():
    bst = build_tree(BinaryTree)
    print_traversals(1, bst)

    delete_sequence(bst)
    print_traversals(2, bst)

    avl = build_tree(AVLTree)
    print_traversals(3, avl)

    delete_sequence(avl)
    print_traversals(4, avl)


if __name__ == "__main__":
    main()
