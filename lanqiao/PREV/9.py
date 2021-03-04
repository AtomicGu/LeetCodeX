n = int(input())


class Node:
    def __init__(self):
        self.tos = {}
        self.flag = False
        return

    def link(self, other, value):
        self.tos[other] = value
        other.tos[self] = value
        return


nodes = [None] + [Node() for i in range(n)]

for i in range(n - 1):
    P, Q, D = list(map(int, input().split()))
    nodes[P].link(nodes[Q], D)

now_longest = 0


def longest(x: Node) -> int:
    """这个函数返回x其余道路中最长路径的长度
    """
    global now_longest

    x.flag = True

    # 从x出发的所有路径的最深长度
    tos = [j + longest(i) for i, j in x.tos.items() if not i.flag]
    if tos == []:
        return 0

    a, b = 0, 0
    for i in tos:
        if i > a:
            b = a
            a = i
        elif i > b:
            b = i

    # 最长的路径可能并不包括进入x的道路
    if a + b > now_longest:
        now_longest = a + b

    x.flag = False
    return a


longest(nodes[1])
ans = (21 + now_longest) * now_longest // 2
print(ans)
