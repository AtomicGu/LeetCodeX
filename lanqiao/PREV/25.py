"""这题的关键就是一个“超空间传送结点”
"""

import io
import sys

sys.stdin = io.StringIO(
    """5 10
5 2 8
4 5 8
2 5 10
1 4 4
5 3 5
1 2 9
1 5 8
5 1 2
1 3 5
4 3 12
-1 -1 -1 18 11
"""
)

n, m = map(int, input().split())

edges = []
for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

holes = list(map(int, input().split()))


def ufds_find(i):
    if ufds[i] == i:
        return i
    j = ufds_find(ufds[i])
    ufds[i] = j
    return j


def ufds_join(i, j):
    ufds[ufds_find(i)] = ufds_find(j)
    return


def ufds_same(i, j):
    return ufds_find(i) == ufds_find(j)


# 计算不建一个码头时的方案
ufds = list(range(n + 1))
edges.sort(key=lambda x: x[2])
cost = 0
count = 0
for a, b, c in edges:
    if c <= 0:
        ufds_join(a, b)
        cost += c
        continue
    if ufds_same(a, b):
        continue
    ufds_join(a, b)
    cost += c
    count += 1
    if count == n - 1:
        break

# ! 第一次错在这里
# ! 去掉码头之后，图可能是不连通的！
for i in range(1, n):
    if not ufds_same(i, i + 1):
        cost_no_harbor = 1 << 63
        break
else:
    cost_no_harbor = cost

# 计算建码头时的方案，假设存在一个连接所有港口的超空间结点 n + 1
for i in range(n):
    if holes[i] != -1:
        edges.append((i + 1, n + 1, holes[i]))
ufds = list(range(n + 2))
edges.sort(key=lambda x: x[2])
cost = 0
count = 0
for a, b, c in edges:
    if c <= 0:
        ufds_join(a, b)
        cost += c
        continue
    if ufds_same(a, b):
        continue
    ufds_join(a, b)
    cost += c
    count += 1
    if count == n:
        break
cost_with_harbor = cost

# 取两者较小者
print(min(cost_no_harbor, cost_with_harbor))
