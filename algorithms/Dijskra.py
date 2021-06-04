"""Dijskra算法

无负权边图上的单源最短路算法

复杂度：
无优化：O(V^2)
堆优化：？
斐波那契堆优化，O(E+VlgV)
"""

from random import randint
from pprint import pprint


class Node:
    """有权图的结点类"""

    def __init__(self, index):
        self.index = index
        self.tos = []
        return

    def __repr__(self) -> str:
        edges = {}
        for u, v in self.tos:
            a = edges.setdefault(u.index, [])
            a.append(v)
        return f"{self.index} -> {edges}"

    def link_to(self, other, weight):
        self.tos.append((other, weight))
        return


# 随机生成图
graph = [Node(i) for i in range(5)]
for i in range(randint(0, 30)):
    a = graph[randint(0, 4)]
    b = graph[randint(0, 4)]
    a.link_to(b, randint(0, 10))
pprint(graph)

# Dijskra算法（堆优化版）
import heapq


class DijNode:
    def __init__(self, dist, node):
        self.dist = dist
        self.node = node
        return

    def __lt__(self, other):
        return self.dist < other.dist


start = graph[0]
heap = [DijNode(0, start)]

while heap:
    a = heapq.heappop(heap)
    if hasattr(a.node, "dist"):
        continue
    a.node.dist = a.dist
    for i, weight in a.node.tos:
        heapq.heappush(heap, DijNode(a.dist + weight, i))

pprint({i.index: getattr(i, "dist", None) for i in graph})
