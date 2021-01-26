# Merge two binary search trees into a single binary search
# tree of minimal height
5
78
/  \ / \
    4
7
64
98

Wrong:
78
/ \
    64
98
/
5
/ \
    4
7

from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # def __traversal__(self):

    def add(value):
        queue = deque()
        queue.append(self.root)
        while queue:
            current = queue.popleft()
            if value <= current.value:
                if current.left is None:
                    current.left = Node(value)
                    break
                queue.append(current.left)
            else:
                if current.right is None:
                    current.right = Node(value)
                    break
                queue.append(current.right)


def inorder_traversal(tree):
    return_values = []

    def get_values(t):
        if t is None:
            return
        get_values(t.left)
        return_values.append(t.value)
        get_values(t.right)

    return get_values(tree)


def get_mid(values):
    if len(values) % 2 == 0:
        mid = len(values) / 2
    else:
        mid = len(values) // 2 + 1
    return mid


def merge_trees(treea, treeb):
    tree_a_values = inorder_traversal(treea)
    # 4 5 7
    tree_a_values.sort()
    tree_a_mid = get_mid(tree_a_values)
    tree_b_values = inorder_traversal(treeb)
    tree_b_values.sort()
    tree_b_mid = get_mid(tree_b_values)

    bt = BinaryTree()
    max_mid = max(tree_a_values, tree_b_mid)
    bt.add(max_mid)
    already_added = []
    already_added.append(max_mid)

    for value in sorted_trees:
        bt.add(value)