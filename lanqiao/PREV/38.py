import io
import sys

sys.stdin = io.StringIO(
    """4
0 0 3 3
1 3 2 4
2 2 4 4
3 3 5 5
"""
)

from array import array

space = 5
size = 1
while size < space * 2:
    size <<= 1
size = ((size ** 2 - 1) // 3 >> 2) + 1
tree = array("B", [0]) * size


def get_2bit(i) -> bool:
    shift = (i & 3) * 2
    return (tree[i >> 2] & (3 << shift)) >> shift


def set_2bit(i, v: int) -> int:  # 白-0，黑-1，灰-2
    shift = (i & 3) * 2
    tree[i >> 2] &= ~(3 << shift)
    tree[i >> 2] |= v << shift
    return


def set_area(x0, y0, x1, y1, i=0, l=0, r=space, t=0, b=space):
    if get_2bit(i) == 1:
        return  # ! 如果当前块都已经全部涂黑了，(x0-y0,x1-y1)这个子区域肯定已经黑过了

    if x0 <= l and r <= x1 and y0 <= t and b <= y1:
        set_2bit(i, 1)
        return

    mx = (l + r) // 2
    my = (t + b) // 2
    lt = (i << 2) + 1, l, mx, t, my
    rt = (i << 2) + 2, mx + 1, r, t, my
    lb = (i << 2) + 3, l, mx, my + 1, b
    rb = (i << 2) + 4, mx + 1, r, my + 1, b

    if x0 <= mx:
        if y0 <= my:
            if x1 <= mx:
                if y1 <= my:
                    set_area(x0, y0, x1, y1, *lt)
                else:
                    set_area(x0, y0, x1, my, *lt)
                    set_area(x0, my + 1, x1, y1, *lb)
            else:
                if y1 <= my:
                    set_area(x0, y0, mx, y1, *lt)
                    set_area(mx + 1, y0, x1, y1, *rt)
                else:
                    set_area(x0, y0, mx, my, *lt)
                    set_area(mx + 1, y0, x1, my, *rt)
                    set_area(x0, my + 1, mx, y1, *lb)
                    set_area(mx + 1, my + 1, x1, y1, *rb)
        else:
            if x1 <= mx:
                set_area(x0, y0, x1, y1, *lb)
            else:
                set_area(x0, y0, mx, y1, *lb)
                set_area(mx + 1, y0, x1, y1, *rb)
    else:
        if y0 <= my:
            if y1 <= my:
                set_area(x0, y0, x1, y1, *rt)
            else:
                set_area(x0, y0, x1, my, *rt)
                set_area(x0, my + 1, x1, y1, *rb)
        else:
            set_area(x0, y0, x1, y1, *rb)

    if all([get_2bit(j[0]) == 1 for j in [lt, rt, lb, rb]]):
        set_2bit(i, 1)
    else:
        set_2bit(i, 2)
    return


def get_area(i=0, l=0, r=space, t=0, b=space) -> int:
    a = get_2bit(i)
    if a == 0:
        return 0
    if a == 1:
        return (r + 1 - l) * (b + 1 - t)

    # a == 2
    mx = (l + r) // 2
    my = (t + b) // 2
    lt = (i << 2) + 1, l, mx, t, my
    rt = (i << 2) + 2, mx + 1, r, t, my
    lb = (i << 2) + 3, l, mx, my + 1, b
    rb = (i << 2) + 4, mx + 1, r, my + 1, b
    return get_area(*lt) + get_area(*rt) + get_area(*lb) + get_area(*rb)


n = int(input())
for i in range(n):
    x0, y0, x1, y1 = map(int, input().split())
    x0, x1 = min(x0, x1), max(x0, x1) - 1
    y0, y1 = min(y0, y1), max(y0, y1) - 1
    set_area(x0, y0, x1, y1)

print(get_area())
