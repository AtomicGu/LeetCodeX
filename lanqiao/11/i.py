from fractions import Fraction

N = int(input())

lines = set()
for i in range(N):
    a, b = input().split()
    lines.add((int(a), int(b)))

ks = {}
cross_points = {}  # 交点字典


def calc_cross(a, b, a_, b_):
    return Fraction(b_ - b, a - a_), Fraction(a * b_ - a_ * b, a - a_)


line_set = set()
ans = 1
for a, b in lines:
    ans += len(line_set) + 1

    # 平行
    t = ks.get(a)
    if t is None:
        ks[a] = 1
    else:
        ans -= t
        ks[a] += 1

    # 公共交点
    crosses = set()
    for a_, b_ in line_set:
        if a == a_:
            continue

        # 计算交点
        cross = calc_cross(a, b, a_, b_)
        crosses.add(cross)

    for cross in crosses:
        t = cross_points.get(cross)
        if t is None:
            cross_points[cross] = 1
        else:
            ans -= t
            cross_points[cross] += 1

    line_set.add((a, b))

print(ans)
