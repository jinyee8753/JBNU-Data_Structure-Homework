"""BST / AVL 트리의 insert/delete 결과를 bintrees 패키지로 검증."""

from bintrees import BinaryTree, AVLTree


INSERT_SEQ = [5, 3, 7, 8, 2, 9, 1]
DELETE_SEQ = [1, 2, 5, 8, 9]


def collect(tree, order):
    """order: -1=pre, 0=in, +1=post (bintrees foreach 규약)."""
    out = []
    tree.foreach(lambda k, v: out.append(k), order)
    return out


def show(label, tree):
    print(label)
    print(f"In-order   {' '.join(str(k) for k in collect(tree, 0))}")
    print(f"Pre-order  {' '.join(str(k) for k in collect(tree, -1))}")
    print(f"Post-order {' '.join(str(k) for k in collect(tree, 1))}")
    print()


def build(tree_cls, insert_seq):
    tree = tree_cls()
    for k in insert_seq:
        tree.insert(k, None)
    return tree


def delete_all(tree, delete_seq):
    for k in delete_seq:
        tree.remove(k)
    return tree


def main():
    print(f"Insert sequence: {INSERT_SEQ}")
    print(f"Delete sequence: {DELETE_SEQ}")
    print("=" * 50)

    bst = build(BinaryTree, INSERT_SEQ)
    show("1. BST insert (5,3,7,8,2,9,1)", bst)

    delete_all(bst, DELETE_SEQ)
    show("2. BST after delete (1,2,5,8,9)", bst)

    avl = build(AVLTree, INSERT_SEQ)
    show("3. AVL insert (5,3,7,8,2,9,1)", avl)

    delete_all(avl, DELETE_SEQ)
    show("4. AVL after delete (1,2,5,8,9)", avl)


if __name__ == "__main__":
    main()
