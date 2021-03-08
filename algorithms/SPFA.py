"""SPFA 是一种改进后的 Bellman-Ford 算法

它的复杂度与 Bellman-Ford 相同，只不过可以在一般情况下节省无用的松弛操作
"""

from random import randint
from pprint import pprint


class Node:
    def __init__(self, index):
        self.index = index
        self.tos = []
        return

    def __repr__(self) -> str:
        edges = {}
        for u, v in self.tos:
            a = edges.setdefault(u.index, [])
            a.append(v)
        return f"<{self.index} -> {edges}"

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

# SPFA 算法
from collections import deque, defaultdict

s = graph[0]  # 源结点
s.d = 0  # 最短估计
s.p = None  # 前驱节点

queue = deque([s])
counter = defaultdict(int)
while queue:
    i = queue.popleft()
    if counter[i] > len(graph):  # ! 对负环的判定有点滞后，可以通过预处理判定负环
        print("有负环")
        exit(0)
    for u, v in i.tos:
        if not hasattr(u, "d") or u.d > i.d + v:
            u.d = i.d + v
            u.p = i
            queue.append(u)
            counter[u] += 1

# 输出
for i in graph:
    if hasattr(i, "d"):
        print(i.index, i.d)
    else:
        print(i.index)
