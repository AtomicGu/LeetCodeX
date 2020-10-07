from typing import List
from common import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        results = []
        if root is None:
            return results

        stack = []

        def dfs(node, current_sum):
            nonlocal sum, stack

            stack.append(node.val)
            current_sum += node.val

            if node.left is None and node.right is None:
                if current_sum == sum:
                    results.append(stack.copy())
            else:
                if node.left is not None:
                    dfs(node.left, current_sum)
                if node.right is not None:
                    dfs(node.right, current_sum)

            stack.pop()
            return

        dfs(root, 0)

        return results


sln = Solution()
ans = sln.pathSum(
    TreeNode.from_heap([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22)
print(ans)
