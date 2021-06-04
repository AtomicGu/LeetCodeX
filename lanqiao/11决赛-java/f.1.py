import io
import sys

sys.stdin = io.StringIO(
    """VsNWkDuWfnfoVsrtXgg
"""
)

from functools import lru_cache

s = input()

names = []
buf = []
for i in s:
    if i.isupper():
        names.append("".join(buf))
        buf = []
    buf.append(i)
names.append("".join(buf))  # ! shit，千万别忘了最后一个！


@lru_cache()
def longest_incseq(i=0):
    """计算 names 从第 i 处开始最长的递增子序列"""
    seq = [names[i]]

    longest = []
    for j in range(i + 1, len(names)):
        if names[j] > names[i]:
            a = longest_incseq(j)
            if (
                len(a) > len(longest) or len(a) == len(longest) and a < longest
            ):  # ! fuck，别忘了相等情况取较优！
                longest = a

    seq.extend(longest)
    return seq


print("".join(longest_incseq()))

# * 这种算法（基本的动态规划）在最坏情况下复杂度为 O(n**2)
