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


class Solution:
    def findMode(self, root):
        if root is None:
            return []

        counter_max = 0
        most_nums = []

        current = 0
        counter = 0

        def mid_root_search(node):
            nonlocal counter_max, most_nums, current, counter
            if node is None:
                return
            mid_root_search(node.left)
            if node.val != current:
                if counter == counter_max:
                    most_nums.append(current)
                elif counter > counter_max:
                    most_nums = [current]
                    counter_max = counter
                current = node.val
                counter = 1
            else:
                counter += 1
            mid_root_search(node.right)
            return

        mid_root_search(root)
        if counter == counter_max:
            most_nums.append(current)
        elif counter > counter_max:
            most_nums = [current]
        return most_nums


root = TreeNode.from_heap([1, None, 2])
sln = Solution()
ans = sln.findMode(root)
print(ans)
