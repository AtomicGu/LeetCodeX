"""树状数组（二叉索引树）

详解：https://www.cnblogs.com/xenny/p/9739600.html

数组的 0 号结点也是哨兵，结点从 1 开始编号。
"""

size = 10000
tree = [0] * (size + 1)


def lowbit(x):
    return x & (-x)


def add_tree(i, k):
    """将结点 i 增加 k

    不同于线段树，树状数组只适合更新，不适合重设
    """
    while i <= size:
        tree[i] += k
        i += lowbit(i)
    return


def sum_tree_1toi(i):
    """求 1 到 i 的区间和"""
    sum_ = 0
    while i > 0:
        sum_ += tree[i]
        i -= lowbit(i)
    return sum_


def sum_tree(l, r):
    """只能用这种差分的方法求区间和"""
    return sum_tree_1toi(r) - sum_tree_1toi(l)
