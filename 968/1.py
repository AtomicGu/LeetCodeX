from typing import Tuple
from common import TreeNode

null = None
inf = 10000


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def wtf(node: TreeNode) -> Tuple[int, int, int]:
            """
            当前结点的子树都被覆盖时：
                状态0：当前结点有摄像头
                状态1：当前结点没有摄像头，但已经被子结点覆盖
                状态2：当前结点没有摄像头，且没被子结点覆盖

            返回三个值分别对应各状态下、以该结点为根的子树最少摄像头值
            """
            if node is None:
                return inf, 0, inf

            l0, l1, l2 = wtf(node.left)
            r0, r1, r2 = wtf(node.right)

            # 状态0时的最少摄像头数
            s0 = 1 + min(l0, l1, l2) + min(r0, r1, r2)

            # 状态1时的最少摄像头数
            s1 = min(l0 + r0, l0 + r1, l1 + r0)

            # 状态2时的最少摄像头数
            s2 = l1 + r1
            return s0, s1, s2

        a, b, c = wtf(root)
        return min(a, b)


root = TreeNode.from_leet([0, 0, null, 0, null, 0, null, null, 0])
sln = Solution()
ans = sln.minCameraCover(root)
print(ans)
