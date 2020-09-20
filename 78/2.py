"""但是没想到还有更牛逼的写法

根本不需要递归！
"""


class Solution(object):
    def subsets(self, nums):
        res = [[]]
        for i in range(0, len(nums)):
            for j in range(0, len(res)):
                res.append(res[j] + [nums[i]])
        return res
