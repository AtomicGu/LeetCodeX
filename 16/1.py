from typing import *

from bisect import bisect_right
from math import inf


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.append(-inf)
        nums.append(inf)
        nums.sort()

        now = target - sum(nums[1:4])
        now_val = abs(now)
        for i in range(1, len(nums) - 1):
            for j in range(i + 1, len(nums) - 1):
                rest = target - nums[i] - nums[j]
                k = bisect_right(nums, rest)

                if k != i and k != j:
                    p = target - nums[i] - nums[j] - nums[k]
                    q = abs(p)
                    if q < now_val:
                        now_val = q
                        now = p

                k -= 1
                if k != i and k != j:
                    p = target - nums[i] - nums[j] - nums[k]
                    q = abs(p)
                    if q < now_val:
                        now_val = q
                        now = p

        return target - now


nums = [-111, -111, 3, 6, 7, 16, 17, 18, 19]
target = 13

slu = Solution()
ans = slu.threeSumClosest(nums, target)
print(ans)
