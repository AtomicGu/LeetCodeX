from fractions import Fraction
from functools import lru_cache
from math import ceil
from typing import List


class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        cost = [Fraction(i, speed) for i in dist]

        @lru_cache()
        def recurse(time=Fraction(0), index=0) -> int:
            if time > hoursBefore:
                return -1

            if index == len(cost):
                return 0

            # 如果正好是整点，就不休息
            if time.denominator == 1:
                return recurse(time + cost[index], index + 1)

            # 否则使用动态规划

            # 休息
            a = recurse(Fraction(ceil(time) + cost[index]), index + 1)
            # 不休息
            b = recurse(time + cost[index], index + 1)

            if a == -1:
                if b == -1:
                    return -1
                return b + 1

            return min(a, b + 1)

        return recurse()
