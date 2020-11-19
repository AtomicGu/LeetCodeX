from typing import Dict, Tuple, List, Union
from math import inf

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
graph = [Node(i) for i in range(V)]

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

# [城市编号,总开销,准时概率,出行路线]
Answer = Tuple[int, int, float, List[int]]
# [总开销,准时概率,出行路线]
PathInfo = Tuple[int, float, List[int]]


def best_path_of_spy_centers_iter() -> Answer:
    """依次yield每个领事馆的最优路径
    """
    def search_best_path(fr: Node, to: Node) -> PathInfo:
        if fr is to:
            return 0, 1.0, [to]

        setattr(fr, "walked", None)

        best_poss = 0.0
        best_cost = inf
        best_path = None
        for node, (poss, cost) in fr.tos.items():
            if hasattr(node, "walked"):
                continue
            temp = search_best_path(node, to)
            if temp is None:
                continue
            temp_cost, temp_poss, temp_path = temp
            temp_cost += cost
            temp_poss *= poss

            if ((temp_poss > best_poss)
                    or (temp_poss == best_poss and temp_cost < best_cost)):
                best_poss = temp_poss
                best_cost = temp_cost
                best_path = temp_path

        delattr(fr, "walked")
        if best_path is None:
            return None
        best_path.append(fr)
        return best_cost, best_poss, best_path

    v0 = graph[0]
    for i, j in spy_centers:
        goto_cost, goto_poss, goto_path = search_best_path(v0, i)
        back_cost, back_poss, back_path = search_best_path(i, v0)
        back_path.pop()
        full_path = back_path + goto_path
        full_path.reverse()

        yield i.index, goto_cost + back_cost + j, goto_poss * back_poss, full_path

    return


a, b, c, d = min(best_path_of_spy_centers_iter(), key=lambda x: (x[1], x[2]))

print(a)
print(b)
print(1 - c)
print(" ".join([str(i.index) for i in d]))
