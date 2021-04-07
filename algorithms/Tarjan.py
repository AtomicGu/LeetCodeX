"""Tarjan算法

求有向图的强连通分量

复杂度：O(V+E)

除此之外，还能解决双连通分量，割点和桥，求最近公共祖先（LCA）等问题。
"""

from gte import input_graph, Node

graph = input_graph(True)

color = 0
stack = []


def dfs(node: Node, depth: int) -> int:
    global color

    if hasattr(node, "color"):
        # 有color属性 <=> 已经求出所在的强连通分量
        # 所以直接返回，此路不通
        return depth

    if hasattr(node, "depth"):
        # 发现回路
        return node.depth

    stack.append(node)

    node.depth = depth
    low = depth
    for i in node.tos:
        low = min(low, dfs(i, depth + 1))
    delattr(node, "depth")

    if depth == low:
        color += 1
        a = stack.pop()
        while a is not node:
            a.color = color
            a = stack.pop()
        a.color = color  # 给node自身上色

    return low


dfs(graph[0], 0)  # 将求出graph[0]所在连通图的所有连同分量，不在同一连通图的结点将不会被上色

# 打印结果
from collections import defaultdict

color_dict = defaultdict(set)
for i in graph:
    color_dict[getattr(i, "color", None)].add(i.index)
print(color_dict)
