import sys
from io import StringIO

sys.stdin = StringIO(
    """10 5 3
67 41
0 34
24 69
58 78
64 62
45 5
27 81
91 61
42 95
36 27
4 91
53 2
82 92
16 21
95 18
"""
)

from math import inf

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
    [((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2) ** 0.5 for j in people]
    for i in post
]


stack = []
min_dist = [inf] * n
min_stack = None


def update_now_dist(now_dist, dist) -> int:
    improment = 0
    for i in range(n):
        if now_dist[i] <= dist[i]:
            continue
        improment += now_dist[i] - dist[i]
        now_dist[i] = dist[i]
    return improment


def combination_ex(begin=0, count=k, now_dist=[inf] * n):
    global min_dist
    global min_stack

    if (m - begin) <= count:
        for i in range(begin, m):
            update_now_dist(now_dist, dists[i])
        if sum(now_dist) < sum(min_dist):
            min_dist = now_dist.copy()
            min_stack = stack.copy()
        return

    for i in range(begin, m):
        now = now_dist.copy()
        improment = update_now_dist(now, dists[i])
        if improment == 0:
            continue
        stack.append(i)
        combination_ex(i + 1, count - 1, now)
        stack.pop()

    return


combination_ex()
print(*[i + 1 for i in min_stack])
