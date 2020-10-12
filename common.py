from typing import List, Optional
from collections import deque


class TreeNode:
    @staticmethod
    def from_heap(heap: List[int]) -> Optional["TreeNode"]:
        def build_tree(index: int) -> Optional["TreeNode"]:
            nonlocal heap
            if index >= len(heap):
                return None

            val = heap[index]
            if val is None:
                return None

            node = TreeNode(val)
            node.left = build_tree(index * 2 + 1)
            node.right = build_tree(index * 2 + 2)
            return node

        return build_tree(0)

    @staticmethod
    def from_leet(leet: List[int]) -> Optional["TreeNode"]:
        if leet == []:
            return None

        leet_iter = iter(leet)
        root = TreeNode(next(leet_iter))
        queue = deque()
        queue.append(root)

        try:
            while queue:
                node = queue.popleft()
                a = next(leet_iter)
                if a is not None:
                    node.left = TreeNode(a)
                    queue.append(node.left)
                a = next(leet_iter)
                if a is not None:
                    node.right = TreeNode(a)
                    queue.append(node.right)
        except StopIteration:
            pass

        return root

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "<TreeNode val={} left={} right={}>".format(
            self.val, self.left.val if self.left else "None",
            self.right.val if self.right else "None")

    def print_subtree(self):
        def print_node(node: TreeNode, indent: int) -> None:
            if node is None:
                print("|   " * indent, "|-", sep="")
                return
            print("|   " * indent, "|---", node.val, sep="")
            indent += 1
            print_node(node.left, indent)
            print_node(node.right, indent)
            return

        print_node(self, 0)
        return
