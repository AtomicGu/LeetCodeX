import sys
import io

sys.stdin = io.StringIO("""8 9
1 2
2 6
2 3
3 7
3 4
7 8
4 8
4 5
5 6
1 6
""")


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
from collections import deque

# 首先求出uv之间任意一条路径
start = nodes[u]
finish = nodes[v]

queue = deque([start])
while queue:
    node = queue.popleft()
    for to in node.tos:
        if hasattr(to, "prev"):
            continue
        to.prev = node
        if to is finish:
            break
        queue.append(to)

if not hasattr(finish, "prev"):
    print(-1)
    exit()

path = []
a = finish.prev
while a is not start:
    path.append(a)
    a = a.prev

# 然后求出图中所有割点
cutvs = set()
dfn = 0


def dfs(node: Node, come: Node):
    global dfn
    dfn += 1
    node.dfn = dfn

    if len(node.tos) < 2:
        return node.dfn

    low = node.dfn
    is_cut = False
    for i in node.tos:
        if i is come:
            continue
        if hasattr(i, "dfn"):
            low = min(low, i.dfn)
        else:
            a = dfs(i, node)
            if a >= node.dfn:
                is_cut = True
            elif a < low:
                low = a

    if is_cut:
        cutvs.add(node)
    return low


start.dfn = dfn
for i in start.tos:
    dfs(i, start)  # 不在乎start是否是割点
print(sum([i in cutvs for i in path]))
# ! node还不一定是uv之间的割点
