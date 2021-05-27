"""Tarjan算法

求有向图的强连通分量

复杂度：O(V+E)

除此之外，还能解决双连通分量，割点和桥，求最近公共祖先（LCA）等问题。
"""

from gte import input_graph, Node

graph = input_graph(True)

color = 0
dfn = 0  # DFS搜索序
stack = []


def dfs(node: Node) -> int:
    """返回从node出发所能到达结点的最小dfn值"""
    global color, dfn

    if hasattr(node, "color"):
        # 有color属性 <=> 已经求出所在的强连通分量
        # 所以直接返回，此路不通
        return dfn

    if hasattr(node, "dfn"):
        # 发现回路
        return node.dfn
    dfn += 1
    node.dfn = dfn

    # 求出最小dfn值
    low = dfn
    stack.append(node)
    for i in node.tos:
        low = min(low, dfs(i))

    # low等于dfn说明发现了新的联通分量
    if low == node.dfn:
        color += 1
        node.color = color
        a = stack.pop()
        while a is not node:
            a.color = color
            a = stack.pop()

    return low


dfs(graph[0])  # 将求出graph[0]所在连通图的所有连同分量，不在同一连通图的结点将不会被上色

# 打印结果
from collections import defaultdict

color_dict = defaultdict(set)
for i in graph:
    color_dict[getattr(i, "color", None)].add(i.index)
print(color_dict)
