"""没想到 Fractions 运算起来还挺慢的
"""

from bisect import bisect_right  # 注意这里要用right！
from typing import List


class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        costs = dist
        hoursBefore *= speed

        def ceil(x):
            return (x + speed - 1) // speed * speed

        # 上界剪枝
        cost_lower_bounds = costs.copy()
        price_lower_bounds = cost_lower_bounds
        for i in range(len(price_lower_bounds) - 2, -1, -1):
            price_lower_bounds[i] += price_lower_bounds[i + 1]

        # 下界剪枝
        cost_upper_bounds = [ceil(i) for i in costs]
        price_upper_bounds = cost_upper_bounds.copy()
        for i in range(len(price_upper_bounds) - 2, -1, -1):
            price_upper_bounds[i] += price_upper_bounds[i + 1]

        # ! 递归转循环
        prices = [costs[0]]
        grades = [0]

        for i, cost in enumerate(costs[1:], 1):
            ite = iter(zip(prices, grades))

            # 首个特殊处理
            price, grade = next(ite)
            ceil_price = ceil(price)
            if price == ceil_price:
                new_prices = [price + cost]
                new_grades = [grade]
            else:
                new_prices = [price + cost, ceil_price + cost]
                new_grades = [grade + 1, grade]

            price_lower_bound = price_lower_bounds[i]
            price_upper_bound = price_upper_bounds[i]

            # 剩下的一般处理
            for j, (price, grade) in enumerate(ite, 1):
                # 价格过高，剪枝
                if price > hoursBefore - price_lower_bound:
                    break

                # 价格过低，剪枝（不危险）
                ceil_price = ceil(price)
                if (
                    ceil_price < hoursBefore - price_upper_bound
                    and j != len(prices) - 1  # ! 不能是最后一个档次
                ):
                    continue

                if price == ceil_price:
                    new_prices.append(price + cost)
                    new_grades.append(grade)
                else:
                    a = price + cost
                    if a < new_prices[-1]:
                        new_prices[-1] = a  # grade+1
                    new_prices.append(ceil_price + cost)
                    new_grades.append(grade)

            prices = new_prices
            grades = new_grades

        my = bisect_right(prices, hoursBefore) - 1
        if my == -1:
            return -1
        return grades[my]


sln = Solution()
ans = sln.minSkips([7, 6, 5, 3, 4, 6, 2, 2, 7, 2], 5, 17)
print(ans)
