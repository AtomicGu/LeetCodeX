from typing import List
from common import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, total: int) -> List[List[int]]:
        results = []
        stack = []

        def dfs(root: TreeNode, total: int):
            if not root:
                return

            stack.append(root.val)
            total -= root.val

            if not root.left and not root.right and total == 0:
                results.append(stack.copy())

            dfs(root.left, total)
            dfs(root.right, total)

            stack.pop()
            return

        dfs(root, total)
        return results


sln = Solution()
ans = sln.pathSum(
    TreeNode.from_heap([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22)
print(ans)
