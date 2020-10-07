from typing import List
from collections import Counter


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0

        counter = Counter(nums)

        for wtf in range(3):
            key = wtf
            value = counter[key]

            for i in range(index, index + value):
                nums[i] = key
            index += value
        return


sln = Solution()
nums = [2, 0, 2, 1, 1, 0]
sln.sortColors(nums)
print(nums)
