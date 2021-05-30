from fractions import Fraction
from math import ceil
from bisect import bisect_right  # 注意这里要用right！
from typing import List, Tuple


class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        cost = [Fraction(i, speed) for i in dist]

        def calc_grade_table(begin=0) -> Tuple[List[Fraction], List[int]]:
            """求出达成 cost[begin:] 的档次表

            返回价目列表和对应的服务列表，已按时间开销升序排序，且服务内容去重。
            """
            if begin == len(cost) - 1:
                return [cost[-1]], [0]

            prices, grades = calc_grade_table(begin + 1)

            p0 = cost[begin]  # 套餐1：不休息
            if p0.denominator == 1:
                return [i + p0 for i in prices], grades

            p1 = ceil(p0)  # 套餐2：休息

            ite = iter(zip(prices, grades))
            price, grade = next(ite)
            new_prices = [p0 + price, p1 + price]
            new_grades = [grade + 1, grade]

            for price, grade in ite:
                a = p0 + price
                if a < new_prices[-1]:
                    new_prices[-1] = a
                new_prices.append(p1 + price)
                new_grades.append(grade)

            return new_prices, new_grades

        prices, grades = calc_grade_table()
        my = bisect_right(prices, hoursBefore) - 1
        if my == -1:
            return -1
        return grades[my]


sln = Solution()
ans = sln.minSkips([7, 3, 5, 5], 2, 10)
print(ans)
