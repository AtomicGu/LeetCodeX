"""Bellman-Ford 算法是一种单源点最短路径算法

它的复杂度为 O(VM)，V 为边数，M 为点数

除求最短路之外，还可用于图中是否存在负权环的判定
"""

from random import randint
from pprint import pprint


class Node:
    """有权图的结点类
    """
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
graph = [Node(i) for i in range(5)]  # * 这种方式存图实际上就是邻接表
for i in range(randint(0, 30)):
    a = graph[randint(0, 4)]
    b = graph[randint(0, 4)]
    a.link_to(b, randint(-2, 10))

pprint(graph)

# Bellman-Ford 算法（加强）
s = graph[0]  # 源结点
s.d = 0  # 最短估计
s.p = None  # 前驱节点

visited = [s]
for _ in range(len(graph) - 1):
    for i in range(len(visited)):
        i = visited[i]
        for u, v in i.tos:  # ! 只适用于有向图
            if not hasattr(u, "d"):
                visited.append(u)  # * 只对于稀疏图有效，但不妨加上去
                u.d = i.d + v
                u.p = i
            elif u.d > i.d + v:
                u.d = i.d + v
                u.p = i

for i in visited:
    for u, v in i.tos:
        if u.d > i.d + v:
            print("有负环")
            exit(0)

# 输出
for i in graph:
    if hasattr(i, "d"):
        print(i.index, i.d)
    else:
        print(i.index)

# * 总结
# * Bellman-Ford 算法要扫描边，出于简单起见，可以直接用边表的方式存储图
