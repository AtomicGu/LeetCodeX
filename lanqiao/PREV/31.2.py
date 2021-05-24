import io
import sys

sys.stdin = io.StringIO(
    """3
3 2 1
"""
)

n = int(input())
nums = [[i, 0] for i in map(int, input().split())]


size_max = 1000001
size = 1
while size < size_max:
    size <<= 1
size <<= 1
tree = [0] * size  # 结点保存的是每个身高区间的小朋友数量


def update_tree(p, k=1, l=0, r=size_max):
    if l == r - 1:
        tree[k] += 1
        return

    m = (l + r) >> 1
    if p < m:
        update_tree(p, k << 1, l, m)
    else:
        update_tree(p, k << 1 | 1, m, r)

    tree[k] += 1
    return


def query_tree(L, R, k=1, l=0, r=size_max):
    if L <= l and r <= R:
        return tree[k]

    m = (l + r) >> 1
    if R <= m:
        return query_tree(L, R, k << 1, l, m)
    if m <= L:
        return query_tree(L, R, k << 1 | 1, m, r)

    a = query_tree(L, R, k << 1, l, m)
    b = query_tree(L, R, k << 1 | 1, m, r)

    return a + b


# 从左到右扫描数组，统计比当前位置大的个数
for i in nums:
    update_tree(i[0])
    i[1] += query_tree(i[0] + 1, size_max)

# 从右到左扫描数组，统计比当前位置小的个数
tree = [0] * size
for i in reversed(nums):
    update_tree(i[0])
    i[1] += query_tree(0, i[0])

sum_ = 0
for _, a in nums:
    sum_ += (1 + a) * a // 2

print(sum_)
