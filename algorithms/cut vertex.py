"""求出图上所有的割点
"""

from gte import input_graph, Node

graph = input_graph()

# graph = [Node(i) for i in range(6)]
# graph[0].link(graph[1])
# graph[0].link(graph[2])
# graph[1].link(graph[2])
# graph[2].link(graph[3])
# graph[3].link(graph[4])
# graph[3].link(graph[5])


def dfs(node: Node, depth: int, come: Node):
    setattr(node, "depth", depth)

    setattr(node, "walked", True)
    min_depth = depth
    is_cut_vertex = False
    for i in node.tos:
        if i is come:
            continue
        if hasattr(i, "walked"):
            min_depth = min(min_depth, i.depth)
        else:
            if hasattr(node, "min_depth_can_go"):
                a = node.min_depth_can_go
            else:
                a = dfs(i, depth + 1, node)
            if a >= depth:
                is_cut_vertex = True
            min_depth = min(min_depth, a)
    delattr(node, "walked")

    setattr(node, "min_depth_can_go", min_depth)
    if is_cut_vertex:
        print(node.index)
    return min_depth


def find_cut_vertex(node: Node):
    setattr(node, "depth", 0)

    setattr(node, "walked", True)
    node_is_cut_vertex = False
    for i in node.tos:
        if dfs(i, 1, node) > 0:
            node_is_cut_vertex = True
    delattr(node, "walked")
    if len(node.tos) >= 2 and node_is_cut_vertex:
        print(node.index)
    return


find_cut_vertex(graph[0])
