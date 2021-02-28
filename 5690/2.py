from typing import List
from functools import lru_cache
from math import inf


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int],
                    target: int) -> int:

        lefts = []
        for i in toppingCosts:
            lefts.append(i)
            lefts.append(i)

        @lru_cache(None)
        def dtgh(target, start):
            if target <= 0 or start == len(lefts):
                return target
            delta = target
            for i in range(start, len(lefts)):
                t = lefts[i]
                v = dtgh(target - t, i + 1)
                if abs(v) < abs(delta):
                    delta = v
                elif abs(v) == abs(delta) and v > 0:
                    delta = v
            return delta

        dtgh.cache_clear()
        return target - min(map(lambda x: dtgh(target - x, 0), baseCosts),
                            key=lambda x: (abs(x), -x))


baseCosts = [3, 10]
toppingCosts = [2, 5]
target = 9

sln = Solution()
ans = sln.closestCost(baseCosts, toppingCosts, target)
print(ans)
