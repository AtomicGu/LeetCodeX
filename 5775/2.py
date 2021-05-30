from fractions import Fraction
from functools import lru_cache
from math import ceil
from typing import List


class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        cost = [Fraction(i, speed) for i in dist]
        remain_cost = [sum(cost[i:]) for i in range(len(cost))]
        most_cost = cost.copy()
        most_cost[-1] = ceil(most_cost[-1])
        for i in range(len(cost) - 2, -1, -1):
            most_cost[i] = ceil(cost[i]) + most_cost[i + 1]

        @lru_cache()
        def recurse(time=Fraction(0), index=0) -> int:
            if time > hoursBefore:
                return -1

            if index == len(cost):
                return 0

            # 剪枝
            if time + remain_cost[index] > hoursBefore:
                return -1
            if time + most_cost[index] <= hoursBefore:
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


sln = Solution()
ans = sln.minSkips(
    [
        40,
        31,
        8,
        31,
        73,
        11,
        11,
        94,
        63,
        9,
        98,
        69,
        99,
        17,
        17,
        85,
        61,
        71,
        22,
        34,
        68,
        78,
        55,
        28,
        70,
        97,
        94,
        89,
        26,
        92,
        40,
        52,
        86,
        84,
        48,
        57,
        67,
        58,
        16,
        32,
        29,
        9,
        44,
        3,
        76,
        71,
        30,
        76,
        29,
        1,
        10,
        91,
        81,
        8,
        30,
        9,
        5,
        43,
        10,
        66,
        31,
        36,
        86,
        63,
        28,
        70,
        17,
        93,
        74,
        74,
        61,
        32,
        61,
    ],
    55,
    96,
)
print(ans)
