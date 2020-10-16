"""多有序数组中顺序统计量通用算法

未通过（别用）
"""

from typing import List


def solution(k: int, *args: List[List[int]]) -> int:

    while k > 1:
        n = len(lists)
        kn = k // n

        a, l = min([(l[lists[l] + kn], l) if lists[l] + kn < len(l) else
                    (l[-1], l) for l in lists],
                   key=lambda x: x[0])

        temp = lists[l] + kn
        if temp >= len(l):
            lists.pop(l)
        else:
            lists[l] = temp

    return min([i[lists[i]] for i in lists])


ans = solution(5, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6])
