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


class DijNode:
    def __init__(self, dist, node):
        self.dist = dist
        self.node = node
        return

    def __lt__(self, other):
        return self.dist < other.dist


import heapq


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        nodes = [None] + [Node(i) for i in range(1, n + 1)]
        for fr, to, dist in edges:
            nodes[fr].link(nodes[to], dist)

        heap = [DijNode(0, nodes[n])]
        while heap:
            dij = heapq.heappop(heap)
            fr = dij.node
            if fr.dtln is not None:
                continue
            fr.dtln = dij.dist
            for to, dist in fr.tos.items():
                heapq.heappush(heap, DijNode(dist + dij.dist, to))
                # 还可以再优化，避免往堆中添加重复结点

        nodes[1].hfljs = 1

        def hfljs(to=nodes[n]) -> int:
            """求点1到to的合法路径数
            """
            if to.hfljs is not None:
                return to.hfljs

            to.hfljs = 0
            for fr in to.tos:
                if fr.dtln > to.dtln:
                    to.hfljs += hfljs(fr)
            return to.hfljs

        return hfljs() % (10**9 + 7)


n = 7
edges = [
    [1, 3, 1],
    [4, 1, 2],
    [7, 3, 4],
    [2, 5, 3],
    [5, 6, 1],
    [6, 7, 2],
    [7, 5, 3],
    [2, 6, 4],
]

sln = Solution()
ans = sln.countRestrictedPaths(n, edges)
print(ans)
