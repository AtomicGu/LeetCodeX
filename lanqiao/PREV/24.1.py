import sys
from io import StringIO

sys.stdin = StringIO(
    """5 4 2
0 0
2 0
3 1
3 3
1 1
0 1
1 0
2 1
3 2
"""
)

from itertools import combinations

n, m, k = map(int, input().split())

people = []
for i in range(n):
    x, y = map(int, input().split())
    people.append((x, y))

post = []
for j in range(m):
    x, y = map(int, input().split())
    post.append((x, y))

dists = [
    [((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2) ** 0.5 for j in post] for i in people
]

choices = []
for i in combinations(range(m), k):
    # 不要暴力：
    # 假如当前已经选了1 2 3，而 4 相比 1 2 3 没有任何改善，则所有与 4 的组合一定不是最优的。
    cost = sum([min([dists[j][k] for k in i]) for j in range(n)])
    choices.append((cost, i))

# choices.sort(key=lambda x: x[0])
# print(choices)

a = min(choices, key=lambda x: x[0])[1]
print(a[0] + 1, a[1] + 1)
