# import sys
# from io import StringIO

# sys.stdin = StringIO("""5
# 3 4 2 5 1
# """)


def up2mod(n):
    n -= 1
    t = n >> 1
    while t:
        n |= t
        t >>= 1
    return n


N = int(input())
P = list(map(int, input().split()))

tree_size = (up2mod(N) + 1) << 1

max_tree = [None] * tree_size


def build_max_tree(k, l, r):
    if l == r:
        val = P[l]
        max_tree[k] = val
        return val

    m = (l + r) >> 1  # 如果采用左闭右开准则，此处处理就非常不优雅
    a = build_max_tree(k << 1, l, m)  # 下标m划给左子树
    b = build_max_tree(k << 1 | 1, m + 1, r)
    val = max(a, b)
    max_tree[k] = val
    return val


build_max_tree(1, 0, len(P) - 1)


def get_max(L, R):
    def _(l, r, k):
        if L <= l and r <= R:
            return max_tree[k]

        m = (l + r) >> 1
        if L <= m:
            a = _(l, m, k << 1)
            if R > m:  # 必须严格大于m，因为下标为m的点被划给了左子树
                b = _(m + 1, r, k << 1 | 1)
                return max(a, b)
            return a
        b = _(m + 1, r, k << 1 | 1)
        return b

    return _(0, len(P) - 1, 1)


def build_min_tree(k, l, r):
    if l == r:
        val = P[l]
        min_tree[k] = val
        return val

    m = (l + r) >> 1
    a = build_min_tree(k << 1, l, m)
    b = build_min_tree(k << 1 | 1, m + 1, r)
    val = min(a, b)
    min_tree[k] = val
    return val


min_tree = [None] * tree_size
build_min_tree(1, 0, len(P) - 1)


def get_min(L, R):
    def _(l, r, k):  # min_tree中下标k存访区间[l,r]的最小值
        if L <= l and r <= R:
            return min_tree[k]
        m = (l + r) >> 1
        if L <= m:
            a = _(l, m, k << 1)
            if R > m:
                b = _(m + 1, r, k << 1 | 1)
                return min(a, b)
            return a
        b = _(m + 1, r, k << 1 | 1)
        return b

    return _(0, len(P) - 1, 1)


counter = len(P)
for i in range(len(P)):
    for j in range(i + 1, len(P)):
        maxer = get_max(i, j)
        miner = get_min(i, j)
        if (maxer - miner) == (j - i):
            counter += 1

print(counter)
