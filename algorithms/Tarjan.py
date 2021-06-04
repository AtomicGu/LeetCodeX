"""Tarjan算法

求有向图的强连通分量、双连通分量、割点、割边

复杂度：O(V+E)

除此之外，还能解决求最近公共祖先（LCA）等问题。
"""

from typing import List, Tuple

from gte import Graph_t, Node


def strongly_connected_color(graph: Graph_t):
    """将 graph 中所有强连通分量中的点上同一种颜色（.color）"""

    def dfs(node: Node) -> int:
        """返回从node出发所能到达结点的最小dfn值"""
        nonlocal color, dfn

        if hasattr(node, "color"):
            # 有color属性 <=> 已经求出所在的强连通分量
            # 所以直接返回，此路不通
            return dfn

        if hasattr(node, "dfn"):
            # 发现回路
            return node.dfn

        # 给结点上号
        node.dfn = dfn
        stack.append(node)
        dfn += 1

        # 求出最小dfn值
        low = node.dfn
        for i in node.tos:
            low = min(low, dfs(i))

        # low等于dfn说明发现了新的联通分量
        if low == node.dfn:
            while True:
                a = stack.pop()
                a.color = color
                if a is node:
                    break
            color += 1

        return low

    dfn = 0  # DFS搜索序
    color = 0
    stack = []
    dfs(graph[0])  # 将求出graph[0]所在连通图的所有连同分量，不在同一连通图的结点将不会被上色
    return


def biconnected_color(graph: Graph_t):
    """将无向图 graph 中所有的双连通分量中的点上同一种颜色（.color）"""

    # 和强连通分量区别（一）：come 参数
    def dfs(node: Node, come: Node) -> int:
        nonlocal color, dfn

        if hasattr(node, "color"):
            return dfn

        if hasattr(node, "dfn"):
            return node.dfn

        node.dfn = dfn
        stack.append(node)
        dfn += 1

        low = node.dfn
        for i in node.tos:
            if i is come:
                continue  # 和强连通分量区别（二）：跳过来时边
            low = min(low, dfs(i))

        if low == node.dfn:
            while True:
                a = stack.pop()
                a.color = color
                if a is node:
                    break
            color += 1

        return low

    dfn = 0  # DFS搜索序
    color = 0
    stack = []
    dfs(graph[0])  # 将求出graph[0]所在连通图的所有连同分量，不在同一连通图的结点将不会被上色
    return


def cut_vertex(graph: Graph_t) -> List[Node]:
    """返回 graph 中的所有割点

    求出无向图中所有的割点，是Tarjan算法变种之一

    注意割点一般都定义在无向图中，有向图中不大有类似概念
    """

    def dfs(node: Node, come: Node) -> int:
        """返回从node出发所能到达结点的最小dfn值"""
        nonlocal dfn

        dfn += 1  # 第一个号被根用了
        node.dfn = dfn

        low = node.dfn
        is_cut = False
        for i in node.tos:
            if i is come:
                continue  # 跳过进入时的边，如果 node 只有一条边，就会退出循环，返回 node.dfn

            if hasattr(i, "dfn"):  # ! 实用时记得清理残留的信息
                low = min(low, i.dfn)
                continue
                # 如果i.dfn比node.dfn小，说明发现回路，应当更新low值
                # 如果大，说明从node出发一定有另外一条路到i，那条路和这条路构成了回路，这时什么都不做
                # 如果等于，说明是自环，也什么都不做

            t = dfs(i, node)
            if t < low:
                low = t
                continue  # 当 t 比 low 还小时不可能比 node.dfn 更大

            if t >= node.dfn:
                is_cut = True  # 任何一个子树不满足，node就是一个割点

        if is_cut:
            cuts.append(node)
        return low

    cuts = []
    dfn = 0
    root = graph[0]
    root.dfn = dfn

    subtree = 0
    for i in root.tos:
        if i is root:
            continue  # 跳过根上的自环

        if not hasattr(i, "dfn"):
            subtree += 1
            dfs(i, root)

    if subtree > 1:
        # DFS起点（树根）的判定和一般结点不一样
        cuts.append(root)
    return cuts


def cut_edge(graph: Graph_t) -> List[Tuple[Node, Node]]:
    """返回 graph 中的所有割边"""

    def dfs(node: Node, come: Node) -> int:
        """返回从node出发所能到达结点的最小dfn值"""
        nonlocal dfn

        dfn += 1
        node.dfn = dfn

        low = node.dfn
        for i in node.tos:
            if i is come:
                continue

            if hasattr(i, "dfn"):  # ! 实用时记得清理残留的信息
                low = min(low, i.dfn)
                continue

            t = dfs(i, node)
            if t < low:
                low = t
                continue

            if t > node.dfn:  # 和割点的区别（一）：dfn 严格大于
                cuts.append((node, come))
        return low

    cuts = []
    dfn = 0
    dfs(graph[0])  # 和割点的区别（二）：起点和其它结点一样
    return cuts
