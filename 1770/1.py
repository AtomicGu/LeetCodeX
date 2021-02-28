from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        primid = [[] for i in range(m)]
        arr = primid[m - 1]
        for j in range(m):
            # arr.append(max(nums[j], nums[j - m]) * multipliers[-1])
            # 不放在里面，当最后一个数是负数，就错！
            arr.append(
                max(
                    nums[j] * multipliers[-1],
                    nums[j - m] * multipliers[-1],
                ))
        for i in range(m - 2, -1, -1):
            arr = primid[i]
            for j in range(i + 1):
                arr.append(
                    max(
                        nums[j] * multipliers[i] + primid[i + 1][j + 1],
                        nums[j - i - 1] * multipliers[i] + primid[i + 1][j],
                    ))
        return primid[0][0]


# nums = [1, 2, 3]
nums = [-5, -3, -3, -2, 7, 1]
# multipliers = [3, 2, 1]
multipliers = [-10, -5, 3, 4, 6]
sln = Solution()
ans = sln.maximumScore(nums, multipliers)
print(ans)
