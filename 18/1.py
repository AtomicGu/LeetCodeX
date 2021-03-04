from typing import *


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []

        nums.sort()
        n = len(nums)
        last_a = None
        for i in range(n):
            a = nums[i]
            if a == last_a:
                continue
            last_a = a
            last_b = None
            for j in range(i + 1, n):
                b = nums[j]
                if b == last_b:
                    continue
                last_b = b
                p = j + 1
                q = n - 1
                try:
                    while p < q:
                        c = nums[p]
                        d = nums[q]
                        t = a + b + c + d
                        if t > target:
                            while nums[q] == d:
                                q -= 1
                        elif t < target:
                            while nums[p] == c:
                                p += 1
                        else:
                            ret.append((a, b, c, d))
                            while nums[q] == d:
                                q -= 1
                            while nums[p] == c:
                                p += 1
                except IndexError:
                    pass

        return ret


nums = [-2, -1, -1, 1, 1, 2, 2]
target = 0

slu = Solution()
ans = slu.fourSum(nums, target)
print(ans)
