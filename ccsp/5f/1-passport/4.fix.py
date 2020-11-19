import sys

# sys.stdin = open(
#     r"E:\WAS\Works\LeetCodeX\ccsp\5f\1-passport\materials\data\1-1.in")

import bisect
from collections import UserList, namedtuple
from math import inf, isclose
from typing import Dict, List, Tuple, Optional

EdgeData = Tuple[float, int]  # 边数据，[准时概率,代价]


class Node:
    def __init__(self, index: int) -> None:
        self.index = index
        self.tos: Dict[Node, EdgeData] = {}
        return

    def link(self, other: "Node", poss: float, cost: int) -> None:
        self.tos[other] = (poss, cost)  # poss -> possibility
        return

    def __repr__(self) -> str:
        return "<Node[{}] tos={}>".format(
            self.index, {i.index: j
                         for i, j in self.tos.items()})


# 1 读入图
V, U, E, C = map(int, input().split())
# !妈的，连图都没都进去就挂了！
# graph = [Node(i) for i in range(V)]
graph = [Node(i) for i in range(V + 1)]

spy_centers: List[Tuple[Node, int]] = []
for i in range(1, U + 1):
    spy_centers.append((graph[i], int(input())))

for i in range(E):
    s, e, p, c = input().split()
    s = graph[int(s)]
    e = graph[int(e)]
    p = 1 - float(p)
    c = int(c)
    s.link(e, p, c)


# 2 搜索
class PathMenu(UserList):
    PathInfo = namedtuple("PathInfo", ("cost", "poss", "path"))

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.sort(key=lambda x: (x[1], -x[0]))

        now_poss = None
        for i in range(len(self) - 1, -1, -1):
            cost, poss, path = self[i]
            if now_poss != poss:
                now_poss = poss
                continue
            del self[i]

        now_cost = inf
        for i in range(len(self) - 1, -1, -1):
            cost, poss, path = self[i]
            if cost < now_cost:
                now_cost = cost
                continue
            del self[i]

        self.bisect_index = [i[0] for i in self]
        self.insert(0, None)
        return

    def select_best(self, budget: int) -> Optional[PathInfo]:
        i = bisect.bisect_right(self.bisect_index, budget)
        return self[i]


def build_path_menu(fr: Node, to: Node) -> None:
    def search_node(fr: Node) -> None:
        nonlocal to

        if fr is to:
            fr.menu = PathMenu([(0, 1.0, [to])])
            return

        if hasattr(fr, "menu"):
            return fr.menu

        setattr(fr, "walked", None)

        menu = []
        for node, (poss, cost) in fr.tos.items():
            if hasattr(node, "walked"):
                continue
            search_node(node)
            menu_iter = iter(node.menu)
            next(menu_iter)
            for ncost, nposs, npath in menu_iter:
                path = npath.copy()
                path.append(fr)
                menu.append((ncost + cost, nposs * poss, path))

        delattr(fr, "walked")
        setattr(fr, "menu", PathMenu(menu))
        return

    search_node(fr)
    return


def clean_path_menu() -> None:
    for node in graph:
        if hasattr(node, "menu"):
            delattr(node, "menu")
    return


def best_path_of_spy_centers_iter():
    """依次yield每个领事馆的最优路径
    """
    v0 = graph[0]
    for vx, vcost in spy_centers:
        clean_path_menu()
        build_path_menu(v0, vx)
        goto_menu: PathMenu = v0.menu

        clean_path_menu()
        build_path_menu(vx, v0)
        back_menu: PathMenu = vx.menu

        budget = C - vcost
        best_poss = 0
        best_cost = inf
        best_path = []
        goto_menu_iter = iter(goto_menu)
        next(goto_menu_iter)
        for goto_cost, goto_poss, goto_path in goto_menu_iter:
            budget_left = budget - goto_cost
            check = back_menu.select_best(budget_left)
            if check is None:
                continue
            back_cost, back_poss, back_path = check

            cost = goto_cost + back_cost + vcost
            poss = goto_poss * back_poss

            if poss > best_poss or (isclose(poss, best_poss)
                                    and cost < best_cost):
                best_poss = poss
                best_cost = cost

                path = back_path.copy()
                path.pop()
                path.extend(goto_path)
                path.reverse()
                best_path = path

        yield vx.index, best_poss, best_cost, best_path
    return


options = list(best_path_of_spy_centers_iter())
a, b, c, d = min(options, key=lambda x: (-x[1], x[2]))

print(a)
print(c)
print("{:.6f}".format(1 - b))
print(" ".join([str(i.index) for i in d]))
