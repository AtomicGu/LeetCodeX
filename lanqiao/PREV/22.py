n, m = map(int, input().split())

edges = []
for i in range(m):  # 妈的，第二次这里m写成了n，而测试样例刚好是n==m！
    a, b, t = map(int, input().split())
    edges.append((a, b, -t))

ufds = list(range(n + 1))


def ufds_find(i):
    a = ufds[i]
    if a == i:
        return i
    b = ufds_find(a)
    ufds[i] = b
    return b


def ufds_join(i, j):
    a = ufds_find(i)
    b = ufds_find(j)
    ufds[a] = b
    return


def ufds_same(i, j):
    return ufds_find(i) == ufds_find(j)


edges.sort(key=lambda x: x[2])
weights = set()
for a, b, w in edges:
    if ufds_same(a, b):
        continue
    ufds_join(a, b)  # 第一次
    weights.add(w)

print(len(weights))
