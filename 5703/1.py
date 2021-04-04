from typing import List

import heapq


def gain(p, t):
    return (t - p) / (t**2 + t)


class Solution:
    def maxAverageRatio(self, classes: List[List[int]],
                        extraStudents: int) -> float:
        T = 0
        queue = []
        for p, t in classes:
            heapq.heappush(queue, (-gain(p, t), (p, t)))
            T += p / t

        for _ in range(extraStudents):
            gain_m, (p, t) = heapq.heappop(queue)
            T -= gain_m
            heapq.heappush(queue, (-gain(p + 1, t + 1), (p + 1, t + 1)))

        return T / len(classes)


# classes = [[1, 2], [3, 5], [2, 2]]
# extraStudents = 2
classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
extraStudents = 4
sln = Solution()
ans = sln.maxAverageRatio(classes, extraStudents)
print(ans)
