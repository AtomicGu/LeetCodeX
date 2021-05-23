"""线段树
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
    build_tree(k << 1 | 1, m, r)

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
