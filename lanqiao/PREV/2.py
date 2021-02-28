n = int(input())
# n = 1

k = n * 2 + 2
m = 2 * k + 1
mat = [[False for i in range(m)] for j in range(m)]


def set_pos(x, y, val):
    mat[k - y][x + k] = val
    return


def hline(x0, x1, y):
    if x0 > x1:
        t = x0
        x0 = x1
        x1 = t
    for x in range(x0, x1 + 1):
        set_pos(x, y, True)
    return


def vline(y0, y1, x):
    if y0 > y1:
        t = y0
        y0 = y1
        y1 = t
    for y in range(y0, y1 + 1):
        set_pos(x, y, True)
    return


hline(-2, 2, 0)
vline(-2, 2, 0)

for i in range(1, n + 1):
    b = 2 * i, 2 * i
    a = b[0], b[1] + 2
    c = b[0] + 2, b[1]

    vline(a[1], b[1], b[0])
    hline(b[0], c[0], b[1])

    vline(-a[1], -b[1], b[0])
    hline(-b[0], -c[0], b[1])

    vline(a[1], b[1], -b[0])
    hline(b[0], c[0], -b[1])

    vline(-a[1], -b[1], -b[0])
    hline(-b[0], -c[0], -b[1])

    vline(c[1], -c[1], c[0])
    hline(-a[0], a[0], a[1])
    vline(c[1], -c[1], -c[0])
    hline(-a[0], a[0], -a[1])

for row in mat:
    for c in row:
        if c:
            print("$", end="")
        else:
            print(".", end="")
    print()
