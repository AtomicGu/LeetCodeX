import io
import sys

sys.stdin = io.StringIO(
    """3
17 0
17 17
"""
)

from functools import lru_cache

peano1_index = [
    (
        (0, 1, 2),
        (5, 4, 3),
        (6, 7, 8),
    ),
    (
        (6, 7, 8),
        (5, 4, 3),
        (0, 1, 2),
    ),
    (
        (8, 7, 6),
        (3, 4, 5),
        (2, 1, 0),
    ),
    (
        (2, 1, 0),
        (3, 4, 5),
        (8, 7, 6),
    ),
]  # 不同方向的一阶曲线序号表
peano_direction = [
    (
        (0, 1, 0),
        (3, 2, 3),
        (0, 1, 0),
    ),
    (
        (1, 0, 1),
        (2, 3, 2),
        (1, 0, 1),
    ),
    (
        (2, 3, 2),
        (1, 0, 1),
        (2, 3, 2),
    ),
    (
        (3, 2, 3),
        (0, 1, 0),
        (3, 2, 3),
    ),
]  # 不同方向曲线的低阶曲线方向


@lru_cache()
def peano_index(x, y, rank, dir):
    if rank == 1:
        return peano1_index[dir][x][y]

    a = 3 ** (rank - 1)
    xd = x // a
    yd = y // a
    # 这么计算得到的是 (xd, yd) 格子处起始位置的序号
    index = peano1_index[dir][xd][yd] * 9 ** (rank - 1)

    xm = x % a
    ym = y % a
    next_dir = peano_direction[dir][xd][yd]

    return index + peano_index(xm, ym, rank - 1, next_dir)


def calc_distance(x0, y0, x1, y1, rank):
    a = peano_index(x0, y0, rank, 0)
    b = peano_index(x1, y1, rank, 0)
    return abs(a - b)


k = int(input())
x0, y0 = map(int, input().split())
x1, y1 = map(int, input().split())

print(calc_distance(x0, y0, x1, y1, k))
