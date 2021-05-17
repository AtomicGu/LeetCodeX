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

stack = [0] * k
min_dist = [2 ** 63] * n


def combination_ex(begin=0, count=k):
    if (m - begin) <= count:
        # 剩下的可选小于要选的数量（可以随便选）
        stack[-count:] = post[begin : begin + count]
        choices.append(stack.copy())
        return

    for i in range(begin, m):
        good = False
        for a, b in zip(post[i], min_dist):
            if a < b:
                good = True

    return
