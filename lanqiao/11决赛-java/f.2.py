"""这题让我学会了 LIS（最长递增子序列）的 O(n*log(n)) 算法

操，其实非常简单，怎么没想到？
想出 DP 后，思维就固化在 DP 了

https://blog.csdn.net/u012505432/article/details/52228945
"""
import io
import sys

sys.stdin = io.StringIO(
    """VsNWkDuWfnfoVsrtXgg
"""
)

from bisect import bisect_left

s = input()

names = []
buf = []
for i in s:
    if i.isupper():
        names.append("".join(buf))
        buf = []
    buf.append(i)
names.append("".join(buf))

tails = [""]  # 哨兵（-inf）
incseq = []
for index, i in enumerate(names):
    j = bisect_left(tails, i)
    if j == len(tails):
        incseq.append(tails[-1])
        tails.append(i)
    else:
        if i < tails[j]:
            tails[j] = i
incseq.append(tails[-1])  # 补上最后一个

print(incseq)  # * 这种方法可以获得 LIS 中下标最小的一个子序列，但不是顺序最小
