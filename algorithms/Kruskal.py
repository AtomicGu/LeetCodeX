"""最小生成树——Kruskal算法

适合稀疏图

复杂度：O(E*log(E))
"""

from random import randint
from pprint import pprint

# 随机生成图
max_node = 5
edges = set()
for i in range(10):
    edges.add((
        randint(0, max_node - 1),
        randint(0, max_node - 1),
        randint(0, 10),  # 权重
    ))
print(edges)

# Kruskal算法
ufds = list(range(max_node))  # 最小生成树


def ufds_find(i) -> int:
    a = ufds[i]
    if a == i:
        return i
    b = ufds_find(a)
    ufds[i] = b
    return b


def ufds_join(i, j):
    a = ufds_find(i)
    b = ufds_find(j)
    ufds[a] = b
    return


def ufds_same(i, j) -> bool:
    return ufds_find(i) == ufds_find(j)


edges = sorted(edges, key=lambda x: x[2])
tree_edges = []
for u, v, w in edges:
    if ufds_same(u, v):
        continue
    tree_edges.append((u, v, w))
    ufds_join(u, v)

print(tree_edges)
