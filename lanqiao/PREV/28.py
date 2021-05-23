import io
import sys

sys.stdin = io.StringIO(
    """2 3 2
1 2 3
2 1 5
"""
)


from functools import lru_cache
from math import comb

n, m, k = map(int, input().split())
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))


def path_count_from_xy(x, y):
    a = m - x - 1
    b = n - y - 1

    # 原理非常好理解：
    # 路径长度固定为a + b，任意从中选取 a 个位置为向右（下）走。
    return comb(a + b, a)


@lru_cache()
def search(x=0, y=0, max_now=-1, more=k):
    if x >= m or y >= n:
        return 0

    # 算上这个点在内，最多还能选 most 个点
    most = (m - x) + (n - y) - 1
    if most < more:
        return 0

    count = 0
    count += search(x + 1, y, max_now, more)
    count += search(x, y + 1, max_now, more)

    if mat[y][x] > max_now:
        more -= 1
        if more == 0:
            count += path_count_from_xy(x, y)
        else:
            count += search(x + 1, y, mat[y][x], more)
            count += search(x, y + 1, mat[y][x], more)

    return count


print(search())
