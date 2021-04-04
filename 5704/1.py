from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = j = k

        now_min = nums[k]
        now_val = nums[k]

        while True:
            # 到头情况
            if i == 0:
                for j in range(j + 1, n):
                    t = nums[j]
                    if t < now_min:
                        now_min = t
                    now_val = max(now_val, (j - i + 1) * now_min)
                break
            if j == n - 1:
                for i in range(i - 1, -1, -1):
                    t = nums[i]
                    if t < now_min:
                        now_min = t
                    now_val = max(now_val, (j - i + 1) * now_min)
                break

            # 一般情况
            if nums[i - 1] < nums[j + 1]:
                j += 1
                if nums[j] < now_min:
                    now_min = nums[j]
                now_val = max(now_val, now_min * (j - i + 1))
            else:
                i -= 1
                if nums[i] < now_min:
                    now_min = nums[i]
                now_val = max(now_val, now_min * (j - i + 1))

        return now_val


nums = [6569, 9667, 3148, 7698, 1622, 2194, 793, 9041, 1670, 1872]
k = 5

sln = Solution()
ans = sln.maximumScore(nums, k)
print(ans)
