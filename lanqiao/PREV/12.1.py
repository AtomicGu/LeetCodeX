# import sys
# import io

# sys.stdin = io.StringIO("""7 6
# 1 3
# 2 3
# 3 4
# 3 5
# 4 5
# 5 6
# 1 6
# """)


class Node:
    def __init__(self, index):
        self.index = index
        self.tos = set()
        return

    def link(self, other):
        self.tos.add(other)
        other.tos.add(self)
        return

    def __repr__(self) -> str:
        return f"<{self.index}->{[i.index for i in self.tos]}>"


#
# 读入数据
n, m = list(map(int, input().split()))
nodes = [None] + [Node(i) for i in range(1, n + 1)]
for _ in range(m):
    a, b = list(map(int, input().split()))
    nodes[a].link(nodes[b])
u, v = list(map(int, input().split()))

#
# 开始做题
dfn = 0
cutv_counter = 0


def dfs(node: Node, come: Node):
    global dfn, cutv_counter

    dfn += 1
    node.dfn = dfn
    to_v = node.index == v

    if len(node.tos) <= 1:
        return node.dfn, to_v

    low = node.dfn
    is_cut = False
    for i in node.tos:
        if i is come:
            continue
        if hasattr(i, "dfn"):
            low = min(low, i.dfn)
        else:
            a, b = dfs(i, node)
            if a >= node.dfn:
                is_cut = True
            else:
                low = min(low, a)
            if b:
                to_v = True

    if is_cut and to_v:
        # ! 发现一个错误：node到这里可能是个割点，但不一定是uv之间的割点。
        cutv_counter += 1
    return low, to_v


root = nodes[u]
uv_is_linked = False
for i in root.tos:
    a, b = dfs(i, root)
    if b:
        uv_is_linked = True

if not uv_is_linked:
    print(-1)
else:
    print(cutv_counter)
