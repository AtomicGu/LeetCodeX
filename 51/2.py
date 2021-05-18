"""八皇后问题的关键不在于怎么对解空间进行搜索，而是怎么对棋盘进行编码

怎么快速地判断一个位置上是不是会冲突才是问题的关键

问题是：怎么想到这些编码方法呢？

答案是：
有一个非常可靠的方法去想编码方法，就是借助解析几何的参数方程
这个思想也在霍夫变换中被用于直线检测体现了出来

详细来说，写出图形类的参数解析式，
然后解析式中的所有参数的值域的笛卡尔积就构成了参数空间，
每个确定的图形就对应参数空间中的一个点。
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        horizontal = [False] * n
        vertical = [False] * n
        lt2rb = [False] * (n + n)
        lb2rt = [False] * (n + n)

        def set_at(x, y, place=True):
            horizontal[y] = place
            vertical[x] = place
            lt2rb[x + y] = place
            lb2rt[x - y] = place
            return

        def get_at(x, y):
            return horizontal[y] or vertical[x] or lt2rb[x + y] or lb2rt[x - y]

        ans = []
        stack = []

        def wtf(x=0):
            if x == n:
                ans.append(stack.copy())
                return

            for y in range(n):
                if not get_at(x, y):
                    set_at(x, y)
                    stack.append((x, y))
                    wtf(x + 1)
                    set_at(x, y, False)
            return

        wtf()
        return ans


sln = Solution()
print(sln.solveNQueens(3))
