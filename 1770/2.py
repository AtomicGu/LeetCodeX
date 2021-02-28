from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        arr = []
        for j in range(m):
            arr.append(
                max(
                    nums[j] * multipliers[-1],
                    nums[j - m] * multipliers[-1],
                ))
        for i in range(m - 2, -1, -1):
            last = arr
            arr = []
            for j in range(i + 1):
                arr.append(
                    max(
                        nums[j] * multipliers[i] + last[j + 1],
                        nums[j - i - 1] * multipliers[i] + last[j],
                    ))
        return arr[0]


# nums = [1, 2, 3]
nums = [-5, -3, -3, -2, 7, 1]
# multipliers = [3, 2, 1]
multipliers = [-10, -5, 3, 4, 6]
sln = Solution()
ans = sln.maximumScore(nums, multipliers)
print(ans)
