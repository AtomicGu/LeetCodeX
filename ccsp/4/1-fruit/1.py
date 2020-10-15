from typing import Tuple, Set

n = int(input())


class Fruit:
    def __init__(self, val: int, index: int, refs=0):
        self.tos: Set[Fruit] = set()
        self.val = val  # 美味度
        self.index = index  # 编号
        self.refs = refs
        return

    def link(self, other):
        self.tos.add(other)
        other.refs += 1
        return

    def __repr__(self):
        return "<Fruit val={} index={}>".format(self.val, self.index)


a_list = [Fruit(int(i), j) for i, j in zip(input().split(), range(2 * n))]
b_list = [int(i) - 1 for i in input().split()]

for i in range(2 * n):
    fr = a_list[i]
    to_i = b_list[i]
    if to_i == -1:
        continue
    to = a_list[to_i]
    fr.link(to)

avaliable_apples = set()
for i in range(n):
    apple = a_list[i]
    if apple.refs == 0:
        avaliable_apples.add(apple)

avaliable_pears = set()
for i in range(n, 2 * n):
    pear = a_list[i]
    if pear.refs == 0:
        avaliable_pears.add(pear)


def select_fruit() -> Tuple[Fruit, Fruit]:
    """
    返回 [苹果，梨子]
    """
    max_val = -1
    maxs = []
    for apple in avaliable_apples:
        for pear in avaliable_pears:
            val = apple.val ^ pear.val
            if val == max_val:
                maxs.append((apple, pear))
            elif val > max_val:
                max_val = val
                maxs = [(apple, pear)]

    def key(x: Tuple[Fruit, Fruit]):
        a, p = x
        return (a.val << 16) | (a.index << 8) | (p.index)

    return max(maxs, key=key)


def package_fruit() -> int:
    apple, pear = select_fruit()

    avaliable_apples.remove(apple)
    for i in apple.tos:
        i: Fruit
        i.refs -= 1
        if i.refs == 0:
            avaliable_apples.add(i)

    avaliable_pears.remove(pear)
    for i in pear.tos:
        i: Fruit
        i.refs -= 1
        if i.refs == 0:
            avaliable_pears.add(i)

    return apple.val ^ pear.val


print(" ".join([str(package_fruit()) for i in range(n)]))
