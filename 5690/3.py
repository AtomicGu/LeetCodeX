"""档次算法
"""
from math import inf
from typing import List, Tuple

from sortedcontainers import SortedDict


class GradeTable:
    def __init__(self, path0=[]):
        self.table = SortedDict()
        self.table[0] = 0, path0
        return

    def decide(self, m):
        i = self.table.bisect_right(m) - 1
        return self.table.items()[i]

    def add_grade(self, cost, gain, path=[]):
        i = self.table.bisect_right(cost) - 1
        g, p = self.table.values()[i]
        if g >= gain:
            return False  # 现有的比新档次还好
        self.table[cost] = gain, path
        return True

    def __repr__(self):
        return repr(self.table)


Options_t = List[Tuple[int, int]]  # 成本, 收益


def filter_inferior(options: Options_t):
    options.sort(key=lambda x: (x[0], -x[1]))
    superior = []
    inferior = []
    max_x = 0
    max_y = 0
    for x, y in options:
        if x > max_x:
            max_x = x
            if y > max_y:
                max_y = y
                superior.append((x, y))
            else:
                inferior.append((x, y))
        else:
            if y == max_y:
                superior.append((x, y))
            else:
                inferior.append((x, y))
    return superior, inferior


def build_grade_table(superior: Options_t, budget=inf):
    gt = GradeTable()
    for x, y in superior:
        buf = []
        for x_, (y_, p_) in gt.table.items():
            cost = x + x_
            if cost > budget:
                break
            buf.append((cost, y + y_, p_ + [x]))
        for i in buf:
            gt.add_grade(*i)
    return gt


def build_multi_grade_table(options: Options_t, budget=inf):
    superior, inferior = filter_inferior(options)
    gt = build_grade_table(superior, budget)
    ret = [gt]
    while inferior:
        superior, inferior = filter_inferior(inferior)
        gt = build_grade_table(superior, budget)
        ret.append(gt)
    return ret


ret = build_multi_grade_table([
    [10, 1],
    [10, 1],
    [10, 1],
    [20, 3],
    [20, 2],
    [20, 1],
    [30, 3],
    [30, 4],
    [40, 5],
    [40, 6],
    [70, 9],
    [70, 9],
    [80, 10],
    [100, 12],
    [90, 10],
    [50, 8],
])
