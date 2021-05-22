"""这题就是暴力，估计也是个NP（难）

不过复习了一下最大子数组解法，还学到了前n行累加和这种节省重复计算的方法

如果要频繁计算 i 到 j 区间的累加和，
可以先求出前 k(k=1...i...n) 个元素之和，
然后每次要求的时候求对应级的之差（怎么感觉像积分？）
"""

import io
import sys

sys.stdin = io.StringIO(
    """3 3
-1 -4 3
3 4 -1
-5 -2 8
"""
)

n, m = map(int, input().split())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))

B = [[0] * m]
for i in range(n):
    B.append([B[-1][j] + A[i][j] for j in range(m)])

from itertools import combinations

max_ = -1 << 63

for i, j in combinations(range(n + 1), 2):
    arr = [B[j][k] - B[i][k] for k in range(m)]

    now = -1 << 63
    sum_ = 0
    for i in arr:
        sum_ += i
        if sum_ > now:
            now = sum_
        if sum_ < 0:
            sum_ = 0

    if now > max_:
        max_ = now

print(max_)
