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
# 直接暴力搜给它干出来
from collections import defaultdict

start = nodes[u]
finish = nodes[v]

visit_counter = defaultdict(int)
path = []


def dfs(node: Node):
    if node is finish:
        for i in path:
            visit_counter[i] += 1
        visit_counter[finish] += 1

    node.walked = True
    path.append(node)
    for i in node.tos:
        if not hasattr(i, "walked"):
            dfs(i)
    path.pop()
    delattr(node, "walked")
    return


dfs(start)
cutv_counter = -2  # 去掉起点和终点
for i in nodes[1:]:
    if visit_counter[i] == visit_counter[finish]:
        cutv_counter += 1
print(cutv_counter)
