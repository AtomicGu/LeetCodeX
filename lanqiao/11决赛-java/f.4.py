"""这题让我学会了 LIS（最长递增子序列）的 O(n*log(n)) 算法

操，其实非常简单，怎么没想到？
想出 DP 后，思维就固化在 DP 了

https://blog.csdn.net/u012505432/article/details/52228945
"""
import io
import sys

sys.stdin = io.StringIO(
    """AZBZCZDZEZFZ
"""
)

from bisect import bisect_left


class Node:
    def __init__(self, v=None, p=None) -> None:
        self.v = v
        self.p = p
        return


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
tails_seq = [Node("")]  # * 这个数组记录了，到目前为止，长度从0~n的、字典序最小的子序列
for index, i in enumerate(names):
    j = bisect_left(tails, i)
    if j == len(tails):
        tails.append(i)
        tails_seq.append(Node(i, tails_seq[j - 1]))
    else:
        if i < tails[j]:
            tails[j] = i
            tails_seq[j] = Node(i, tails_seq[j - 1])

decseq = []
i = tails_seq[-1]
while i:
    decseq.append(i.v)
    i = i.p
print("".join(reversed(decseq)))
