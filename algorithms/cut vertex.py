"""求出无向图中所有的割点

是Tarjan算法变种之一

注意割点一般都定义在无向图中，有向图中不大有类似概念
"""

from gte import input_graph, Node

dfn = 0


def dfs(node: Node, come: Node) -> int:
    """返回从node出发所能到达结点的最小dfn值"""
    global dfn

    dfn += 1
    node.dfn = dfn

    if len(node.tos) <= 1:
        # 只有一个边的结点不可能是割点
        return node.dfn

    low = node.dfn
    is_cut = False
    for i in node.tos:
        if i is come:
            continue  # 跳过进入时的边

        if hasattr(i, "dfn"):
            low = min(low, i.dfn)
            # 如果i.dfn比node.dfn小，说明发现回路，应当更新low值
            # 如果大，说明从node出发一定有另外一条路到i，那条路和这条路构成了回路，这时什么都不做
            # 如果等于，说明是自环，也什么都不做
        else:
            t = dfs(i, node)
            if t >= node.dfn:
                is_cut = True  # 任何一个子树不满足，node就是一个割点

            elif t < low:  # 当t比node.dfn还大时不可能比low更小
                low = t

    if is_cut:
        print(node.index)

    return low


def dfs_root(root: Node):
    global dfn

    dfn = 0
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
        print(root.index)
    return


graph = input_graph()
dfs_root(graph[0])
