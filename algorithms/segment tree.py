"""线段树

详解：https://www.cnblogs.com/xenny/p/9801703.html

要注意线段树数组的 0 位置是哨兵，结点从 1 开始标号。
"""

nums = [1, 8, 6, 4, 3, 5]

size = 1
while size < len(nums):
    size <<= 1
size <<= 1
tree = [0] * size


def build_tree(k=1, l=0, r=len(nums)):
    """
    k: 要构建的结点
    [l, r): 结点对应的区间
    """
    if l == r - 1:
        tree[k] = nums[l]
        return

    m = (l + r) >> 1
    build_tree(k << 1, l, m)
    build_tree(k << 1 | 1, m, r)  # 如果不用哨兵，这里就会变成 k << 1 + 2，很不简洁
    # ! 如果是四叉树，不使用哨兵，第 i 个结点的子节点为 4i+1、4i+2、4i+3、4i+4，很有规律，
    # ! 如果用哨兵，就是 4i-2、4i-1、4i、4i+1，反而用哨兵就会很丑陋。

    tree[k] = max(tree[k << 1], tree[k << 1 | 1])
    return


build_tree()


def update_tree(p, v, k=1, l=0, r=len(nums)):
    """
    将 nums 的 p 处设为 v
    k: 线段树下标
    [l, r): 结点 k 对应的区间
    """
    if l == r - 1:
        tree[k] = nums[p] = v
        return

    m = (l + r) >> 1
    if p < m:
        update_tree(p, v, k << 1, l, m)
    else:
        update_tree(p, v, k << 1 | 1, m, r)

    tree[k] = max(tree[k << 1], tree[k << 1 | 1])
    return


update_tree(2, 13)


def query_tree(L, R, k=1, l=0, r=len(nums)):
    """
    查询 [L, R) 上的目标值
    k: 线段树下标
    [l, r): 结点 k 对应的区间
    """
    if L <= l and r <= R:
        return tree[k]

    m = (l + r) >> 1
    if R <= m:
        return query_tree(L, R, k << 1, l, m)
    if m <= L:
        return query_tree(L, R, k << 1 | 1, m, r)

    a = query_tree(L, R, k << 1, l, m)
    b = query_tree(L, R, k << 1 | 1, m, r)

    return max(a, b)


print(query_tree(2, 6))
