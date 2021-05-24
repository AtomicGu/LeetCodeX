import io
import sys

# sys.stdin = io.StringIO(
#     """5 6
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 2 3 L 5
# """
# )

sys.stdin = io.StringIO(
    """3 3
0 0 0
1 1 1
1 1 1
1 1 U 6
"""
)

from collections import defaultdict

m, n = map(int, input().split())

grid = defaultdict(lambda: 0)
for x in range(m):
    for y, i in enumerate(map(int, input().split())):
        grid[(x, y)] = i

x, y, s, k = input().split()
x, y, k = map(int, (x, y, k))

s = "RULD".index(s)
d = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def step():
    global x, y, s
    i = grid[(x, y)]
    if i == 1:
        s = (s - 1) % 4
        grid[(x, y)] = 0
        x += d[s][0]
        y += d[s][1]
    else:
        s = (s + 1) % 4
        grid[(x, y)] = 1
        x += d[s][0]
        y += d[s][1]
    return


for i in range(k):
    step()

print(x, y)
