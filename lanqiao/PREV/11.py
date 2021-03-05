# import sys
# import io

# sys.stdin = io.StringIO("10 8 5 7 12 4")

nums = list(map(int, input().split()))


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        return

    def __repr__(self) -> str:
        return f"<Node {self.val}>"


if nums == []:
    print()
    exit()

ite = iter(nums)
root = Node(next(ite))
nodes = [root]


def insert(val, node=root):
    if val < node.val:
        if node.left is None:
            new_node = Node(val)
            node.left = new_node
            nodes.append(new_node)
        else:
            insert(val, node.left)
    else:
        if node.right is None:
            new_node = Node(val)
            node.right = new_node
            nodes.append(new_node)
        else:
            insert(val, node.right)
    return


for val in ite:
    insert(val)

# class Matrix:
#     def __init__(self, w, h):
#         self.mat = [[None] * w for i in range(h)]
#         return
#
#     def __getitem__(self, index):
#         if isinstance(index[0], slice):
#             sx, sy = index
#             m = Matrix(0, 0)
#             m.mat = [
#                 row[sx.start:sx.stop:sx.step]
#                 for row in self.mat[sy.start:sy.stop:sy.step]
#             ]
#             return m
#         return self.mat[index[1]][index[0]]
#
#     def __setitem__(self,)

canvas = [[None] * 1000 for i in range(200)]

from typing import Tuple


def plot_tree(root: Node, left=0, top=0) -> Tuple[int, int]:
    """返回下边界y坐标和树根的y坐标
    """
    strval = str(root.val)
    next_level_left = left + len(strval) + 3

    if root.right is not None:
        a, b = plot_tree(root.right, next_level_left, top)
        canvas[b][next_level_left - 1] = "-"

        center = a + 1
        for i in range(b, center):
            canvas[i][next_level_left - 2] = "|"

        canvas[center][next_level_left - 2] = "|"
        canvas[center][next_level_left - 3] = "-"
    else:
        center = top

    for i in range(len(strval)):
        canvas[center][left + i] = strval[i]

    if root.left is not None:
        a, b = plot_tree(root.left, next_level_left, center + 1)
        canvas[b][next_level_left - 1] = "-"
        for i in range(b, center, -1):
            canvas[i][next_level_left - 2] = "|"

        canvas[center][next_level_left - 2] = "|"
        canvas[center][next_level_left - 3] = "-"
        bottom = a
    else:
        bottom = center
    return bottom, center


a, b = plot_tree(root)

for i in range(a + 1):
    row = canvas[i]
    j = len(row) - 1
    while row[j] is None:
        j -= 1

    for j in range(j + 1):
        char = row[j]
        if char is None:
            print(".", end="")
        else:
            print(char, end="")
    print()
