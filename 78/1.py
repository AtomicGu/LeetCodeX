"""这是我最开始的想法

就是递归写，因为之前在回溯相关的题目中写过。
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums = [[i, True] for i in nums]

        def foo(start: int) -> None:
            results.append([i for i, flag in nums if flag])
            for index in range(start, len(nums)):
                t = nums[index]
                t[1] = False
                foo(index + 1)
                t[1] = True
            return

        foo(0)
        return results
