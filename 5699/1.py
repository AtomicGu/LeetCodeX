from typing import *


class Node:
    def __init__(self, index):
        self.tos = {}
        self.index = index
        self.dtln = None  # distanceToLastNode
        self.hfljs = None  # 合法路径数
        return

    def __repr__(self) -> str:
        return f"<{self.index}->{[i.index for i in self.tos]}>"

    def link(self, other, dist):
        self.tos[other] = dist
        other.tos[self] = dist
        return


from collections import deque


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        nodes = [None] + [Node(i) for i in range(1, n + 1)]
        for fr, to, dist in edges:
            nodes[fr].link(nodes[to], dist)

        nodes[n].dtln = 0
        queue = deque([nodes[n]])
        while queue:
            fr = queue.popleft()
            for to, dist in fr.tos.items():
                dist += fr.dtln
                if to.dtln is None:
                    queue.append(to)
                    to.dtln = dist
                else:
                    if dist < to.dtln:
                        to.dtln = dist

        counter = 0

        def find_road(fr=nodes[1]):
            nonlocal counter
            if fr is nodes[n]:
                counter += 1
                return

            for to in fr.tos:
                if to.dtln < fr.dtln:
                    find_road(to)
            return

        find_road()
        return counter % (10**9 + 7)


# n = 5
# edges = [
#     [1, 2, 3],
#     [1, 3, 3],
#     [2, 3, 1],
#     [1, 4, 2],
#     [5, 2, 2],
#     [3, 5, 1],
#     [5, 4, 10],
# ]

# n = 7
# edges = [
#     [1, 3, 1],
#     [4, 1, 2],
#     [7, 3, 4],
#     [2, 5, 3],
#     [5, 6, 1],
#     [6, 7, 2],
#     [7, 5, 3],
#     [2, 6, 4],
# ]

sln = Solution()
ans = sln.countRestrictedPaths(n, edges)
print(ans)
