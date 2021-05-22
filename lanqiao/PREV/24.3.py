"""这题应该是个NP问题，主要就考察组合生成而已

但是 Python 做这种暴力 NP 问题非常容易超时，估计它的计算力应该远没到 5e8
"""

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

from array import array
from copy import copy

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
    array(
        "f", [((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2) ** 0.5 for j in people]
    )
    for i in post
]


def improve_now_dist(now_dist, dist) -> int:
    improment = 0
    for i in range(n):
        if now_dist[i] <= dist[i]:
            continue
        improment += now_dist[i] - dist[i]
        now_dist[i] = dist[i]
    return improment


min_dist = dists[0]
min_stack = [0]


def combination_ex():
    global min_dist
    global min_stack

    if m <= k:
        min_stack = list(range(m))
        return

    stack = []

    def recurse(begin, rest, now_dist):
        global min_dist
        global min_stack

        if rest == 0:
            if sum(min_dist) > sum(now_dist):
                min_dist = now_dist
                min_stack = stack.copy()
            return

        for i in range(begin, m - rest + 1):
            now = copy(now_dist)
            imp = improve_now_dist(now, dists[i])
            if imp == 0:
                continue
            stack.append(i)
            recurse(i + 1, rest - 1, now)
            stack.pop()
        return

    for i in range(m - k + 1):
        stack = [i]
        recurse(i + 1, k - 1, dists[i])

    return


combination_ex()
print(*[i + 1 for i in min_stack])
