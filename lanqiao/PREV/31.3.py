import io
import sys

sys.stdin = io.StringIO(
    """10
1 3 9 5 10 0 3 1 4 4
"""
)

n = int(input())
nums = [
    [i + 1, 0] for i in map(int, input().split())
]  # 树状数组索引从1开始，所以这里必须+1规避零


size_max = 1000001

size = size_max
tree = [0] * (size + 1)


def lowbit(x):
    return x & (-x)


def add_tree(i, k):
    """将结点 i 增加 k

    不同于线段树，树状数组只适合更新，不适合重设
    """
    while i <= size:
        tree[i] += k
        i += lowbit(i)  # 如果i==0则此处会陷入死循环
    return


def sum_tree_1toi(i):
    """求 1 到 i 的区间和"""
    sum_ = 0
    while i > 0:
        sum_ += tree[i]
        i -= lowbit(i)
    return sum_


def sum_tree(l, r):
    """只能用这种差分的方法求区间 [l, r) 的和"""
    return sum_tree_1toi(r - 1) - sum_tree_1toi(l - 1)


# 从左到右扫描数组，统计比当前位置大的个数
for i in nums:
    add_tree(i[0], 1)
    i[1] += sum_tree(i[0] + 1, size_max)

# 从右到左扫描数组，统计比当前位置小的个数
tree = [0] * size
for i in reversed(nums):
    add_tree(i[0], 1)
    i[1] += sum_tree(0, i[0])

sum_ = 0
for _, a in nums:
    sum_ += (1 + a) * a // 2

print(sum_)
