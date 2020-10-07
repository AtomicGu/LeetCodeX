from typing import List
from common import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            # 如果这里没有节点构造二叉树了，就结束
            if in_left == in_right:
                return None

            # 选择 postorder 末尾的元素作为当前子树根节点
            val = postorder.pop()
            root = TreeNode(val)

            # 根据 root 所在位置分成左右两棵子树
            index = idx_map[val]

            # 构造右子树
            root.right = helper(index + 1, in_right)
            # 构造左子树
            root.left = helper(in_left, index)

            # 卧槽，左右子树构造的顺序还不能调换，如果是前序遍历和中序遍历，则是先构造左后构造右
            return root

        # 建立（元素，下标）键值对的哈希表
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder))


sln = Solution()
ans = sln.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
print(ans)
