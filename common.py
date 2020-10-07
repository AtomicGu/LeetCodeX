from typing import List, Optional


class TreeNode:
    @staticmethod
    def from_heap(heap: List[int]):
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

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "<TreeNode val={} left={} right={}>".format(
            self.val, self.left.val if self.left else "None",
            self.right.val if self.right else "None")
