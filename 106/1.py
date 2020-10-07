from typing import List, Optional
from common import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build_tree(inorder_head: int, inorder_tail: int,
                       postorder_head: int,
                       postorder_tail: int) -> Optional[TreeNode]:
            nonlocal inorder, postorder

            if inorder_head == inorder_tail:
                return None

            mid = postorder[postorder_tail - 1]
            mid_index_inorder = inorder.index(mid, inorder_head, inorder_tail)

            left_tail_postorder = (postorder_head + mid_index_inorder -
                                   inorder_head)

            t = TreeNode(mid)
            t.left = build_tree(inorder_head, mid_index_inorder,
                                postorder_head, left_tail_postorder)
            t.right = build_tree(mid_index_inorder + 1, inorder_tail,
                                 left_tail_postorder, postorder_tail - 1)
            return t

        return build_tree(0, len(inorder), 0, len(postorder))


sln = Solution()
ans = sln.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
print(ans)
